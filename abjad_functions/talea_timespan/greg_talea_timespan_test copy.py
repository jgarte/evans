import abjad
from abjadext import rmakers
import timespan_functions


# Rhythm cells
def rhythm_cell(duration, rtm):
    rtm_parser = abjad.rhythmtrees.RhythmTreeParser()
    selection = abjad.select(rtm_parser(rtm)[0](duration))
    for tuplet in abjad.select(selection).components(abjad.Tuplet):
        tuplet.normalize_multiplier()
    return selection

rmodel_one = lambda duration: rhythm_cell(duration, '(1 (3 (2 (1 2 -1 1)) 3))')
rmodel_two = lambda duration: rhythm_cell(duration, '(1 (1 (4 (1 -1 1 -1 1))))')
rmodel_three = lambda duration: rhythm_cell(duration, '(1 (1 (1 (1 -2 1 3))))')
silence_maker = rmakers.NoteRhythmMaker(
    division_masks=[
        rmakers.SilenceMask(
            pattern=abjad.index([0], 1),
        ),
    ],
)
rmakers_cycle = timespan_functions.cyc([rmodel_one, rmodel_two, rmodel_three])

talea = rmakers.Talea(
    counts=[5, 3, -1, 6, -7, 2],
    denominator=8,
)

# Timespan list
dummy_list = []
for i in range(0, 3):
    timespan_list = timespan_functions.talea_timespans(talea=talea, advancement=((i*4)+1)%len(talea))
    for timespan in timespan_list:
        if isinstance(timespan, abjad.AnnotatedTimespan):
            timespan.annotation = timespan_functions.TimespanSpecifier(
                voice_name = 'Voice ' + str(i),
                rhythm_maker = next(rmakers_cycle),
            )
        else:
            timespan.annotation = timespan_functions.TimespanSpecifier(
                voice_name = 'Voice ' + str(i),
                rhythm_maker = silence_maker,
            )
    timespan_list.sort()
    dummy_list.append(timespan_list)

master_length = len(dummy_list)
voices = ['Voice ' + str(i+1) for i in range(master_length)]
all_timespans = {voice : timespan_list for voice, timespan_list in zip(voices, dummy_list)}
time_signatures = [
    abjad.TimeSignature(pair) for pair in [timespan.duration.pair for timespan in all_timespans['Voice 1']]
]
offsets = abjad.mathtools.cumulative_sums(
    [abjad.Offset(t_s.duration) for t_s in time_signatures]
    )

master_list = []
for i in range(0, 3):
    timespan_list = timespan_functions.talea_timespans(talea=talea, advancement=((i*4)+1)%len(talea))
    split_list = timespan_functions.make_split_list(timespan_list, offsets)
    for timespan in split_list:
        if isinstance(timespan, abjad.AnnotatedTimespan):
            timespan.annotation = timespan_functions.TimespanSpecifier(
                voice_name = 'Voice ' + str(i),
                rhythm_maker = next(rmakers_cycle),
            )
        else:
            timespan.annotation = timespan_functions.TimespanSpecifier(
                voice_name = 'Voice ' + str(i),
                rhythm_maker = silence_maker,
            )
    split_list.sort()
    master_list.append(split_list)

master_length = len(master_list)
voices = ['Voice ' + str(i+1) for i in range(master_length)]
all_timespans = {voice : timespan_list for voice, timespan_list in zip(voices, master_list)}

silence_specifier = timespan_functions.TimespanSpecifier(rhythm_maker=silence_maker)
timespan_functions.add_silences_to_timespan_dict(all_timespans, silence_specifier)


# Score
voice_staff_names = [['Voice ' + str(i+1), 'Staff ' + str(i+1)] for i in range(master_length)]
score = abjad.Score([
    abjad.Staff(lilypond_type='TimeSignatureContext', name='Global Context'),
    abjad.StaffGroup(
        [
            abjad.Staff([abjad.Voice(name=voice_name)],
                        name=staff_name, lilypond_type='RhythmicStaff')
                        for voice_name, staff_name in voice_staff_names
        ],
        name='Staff Group'
    )
])


# Timespan -> Rhythm
for voice_name, timespan_list in all_timespans.items():
    for timespan in timespan_list:
        container = abjad.Container([])
        durations = [timespan.duration]
        selections = timespan.annotation.rhythm_maker(durations)
        container.extend(selections)
        specifier = rmakers.BeamSpecifier(beam_each_division=True, beam_rests=True)
        specifier(abjad.select(container))
        voice = score[voice_name]
        voice.append(container)


# Time Signatures
for time_signature in time_signatures:
    skip = abjad.Skip(1, multiplier=(time_signature))
    abjad.attach(time_signature, skip)
    score['Global Context'].append(skip)


# Label staves
for i, staff in enumerate(abjad.iterate(score['Staff Group']).components(abjad.Staff)):
    markup_label = str(i+1)
    name_abbrev = [
        abjad.StartMarkup(markup=abjad.Markup(markup_label)),
        abjad.MarginMarkup(markup=abjad.Markup(markup_label))]
    for label in name_abbrev:
        abjad.attach(label, abjad.select(staff).leaves()[0])

#The rewriting won't work because it must partition exactly.
# for voice in abjad.iterate(score['Staff Group']).components(abjad.Voice):
#     for i , shard in enumerate(abjad.mutate(voice[:]).split(time_signatures)):
#         time_signature = time_signatures[i]
#         abjad.mutate(shard).rewrite_meter(time_signature)

# Lilyfile
lilyfile = abjad.LilyPondFile.new(
    score,
    includes=[
        timespan_functions.rhythm_stylesheet,
        timespan_functions.abjad_stylesheet,
    ],
)

abjad.show(lilyfile)