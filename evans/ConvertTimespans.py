from collections import defaultdict

import abjad
import abjadext.rmakers
from tsmakers.PerformedTimespan import PerformedTimespan

from . import timespan
from .handlers import RhythmHandler
from .sequence import CyclicList

silence_maker_ = abjadext.rmakers.stack(
    abjadext.rmakers.NoteRhythmMaker(),
    abjadext.rmakers.force_rest(abjad.select().leaves(pitched=True)),
)

silence_maker = RhythmHandler(rmaker=silence_maker_, name="silence maker")


class ConvertTimespans(object):
    def __init__(
        self,
        materials,
        ts_list,
        bounds,
        persist=False,
        segment_name=None,
        current_directory=None,
        fill_gaps=True,
    ):
        self.materials = materials
        self.ts_list = ts_list
        self.bounds = bounds
        self.persist = persist
        self.segment_name = segment_name
        self.current_directory = current_directory
        self.fill_gaps = fill_gaps

    def __call__(self):
        self.convert_timespans(self.materials, self.ts_list, self.bounds)

    def __str__(self):
        return abjad.storage(self)

    def __repr__(self):
        return abjad.storage(self)

    @staticmethod
    def convert_timespans(
        materials,
        ts_list,
        bounds,
        segment_name,
        current_directory,
        add_silence=True,
        fill_gaps=True,
        split=False,
        is_global=False,
    ):
        cyclic_materials = CyclicList(materials, continuous=True)

        master_list = []

        groups = [timespan_.voice_name for timespan_ in ts_list]
        input = [(span, group) for span, group in zip(ts_list, groups)]
        res = defaultdict(list)
        for v, k in input:
            res[k].append(v)
        voice_dict_list = [
            {"voice": k, "items": abjad.TimespanList(v)} for k, v in res.items()
        ]

        item_list = [x["voice"] for x in voice_dict_list]
        item_list.sort(key=timespan.sorted_keys)
        sorted_voice_dict_list = []
        for key in item_list:
            for span_dict in voice_dict_list:
                if span_dict["voice"] == key:
                    sorted_voice_dict_list.append(span_dict)

        for i, timespan_dict in enumerate(sorted_voice_dict_list):
            ts_list = abjad.TimespanList()
            for timespan_ in timespan_dict["items"]:
                if isinstance(timespan_, abjad.AnnotatedTimespan):
                    if is_global is False:
                        timespan_.annotation = timespan.TimespanSpecifier(
                            voice_name=f"Voice {i}", handler=cyclic_materials(r=1)[0]
                        )
                        ts_list.append(timespan_)
                    else:
                        timespan_.annotation = timespan.TimespanSpecifier(
                            voice_name="Global Context",
                            handler=cyclic_materials(r=1)[0],
                        )
                        ts_list.append(timespan_)
                elif isinstance(timespan_, PerformedTimespan):
                    if is_global is False:
                        timespan_ = abjad.AnnotatedTimespan(
                            start_offset=timespan_.start_offset,
                            stop_offset=timespan_.stop_offset,
                            annotation=timespan.TimespanSpecifier(
                                voice_name=f"Voice {i}",
                                handler=cyclic_materials(r=1)[0],
                            ),
                        )
                        ts_list.append(timespan_)
                    else:
                        timespan_ = abjad.AnnotatedTimespan(
                            start_offset=timespan_.start_offset,
                            stop_offset=timespan_.stop_offset,
                            annotation=timespan.TimespanSpecifier(
                                voice_name="Global Context",
                                handler=cyclic_materials(r=1)[0],
                            ),
                        )
                        ts_list.append(timespan_)
                else:
                    if fill_gaps is True:
                        if add_silence is True:
                            timespan_.annotation = timespan.TimespanSpecifier(
                                voice_name=f"Voice {i}", handler=silence_maker
                            )
                            ts_list.append(timespan_)
                        else:
                            timespan_.annotation = timespan.TimespanSpecifier(
                                voice_name=f"Voice {i}",
                                handler=cyclic_materials(r=1)[0],
                            )
                            ts_list.append(timespan_)
                    else:
                        continue
            ts_list.sort()
            master_list.append(ts_list)

        showable_list = abjad.TimespanList()
        for x in master_list:
            for y in x:
                new_span = abjad.AnnotatedTimespan(
                    start_offset=y.start_offset,
                    stop_offset=y.stop_offset,
                    annotation=y.annotation.voice_name,
                )
                showable_list.append(new_span)

        if split is True:
            split_timespans = [timespan.make_split_list(x, bounds) for x in master_list]
        else:
            split_timespans = [x for x in master_list]

        master_list = split_timespans

        master_length = len(master_list)
        if is_global is False:
            voices = [f"Voice {i + 1}" for i in range(master_length)]
        else:
            voices = ["Global Context"]
        final_timespan_dict = {
            voice: timespan_list for voice, timespan_list in zip(voices, master_list)
        }
        if add_silence is True:
            silence_specifier = timespan.TimespanSpecifier(handler=silence_maker)
            timespan.add_silences_to_timespan_dict(
                final_timespan_dict, silence_specifier
            )

        directory = (current_directory).resolve()
        pdf_path = abjad.Path(f"""{directory}/{segment_name}.pdf""")
        if pdf_path.exists():
            pdf_path.unlink()
        result = abjad.persist(showable_list).as_pdf(
            pdf_path,
            scale=0.70,
            key="annotation",
            sort_callable=timespan.human_sorted_keys,
        )
        success = result[3]
        if success is False:
            print("LilyPond failed!")

        return final_timespan_dict
