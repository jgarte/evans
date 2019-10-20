import abjad
from evans.AttachmentHandlers.CyclicList import CyclicList


class GlissandoHandler:
    def __init__(
        self,
        glissando_style=None,
        line_style=None,
        boolean_vector=[0],
        continuous=True,
        count=-1,
        name="Glissando Handler",
    ):
        self.glissando_style = glissando_style
        self.line_style = line_style
        self._count = count
        self.continuous = continuous
        self.boolean_vector = CyclicList(boolean_vector, self.continuous, self._count)
        self.name = name

    def __call__(self, selections):
        self.add_glissando(selections)

    def add_glissando(self, selections):
        runs = abjad.select(selections).runs()
        if self.glissando_style == "hide_middle_note_heads":
            if self.line_style != None:
                for run in runs:
                    if self.boolean_vector(r=1)[0] is 0:
                        if len(run) > 1:
                            abjad.glissando(
                                run[:],
                                abjad.tweak(self.line_style).style,
                                hide_middle_note_heads=True,
                            )
                        else:
                            continue
                    else:
                        continue
            else:
                for run in runs:
                    if self.boolean_vector(r=1)[0] is 0:
                        if len(run) > 1:
                            abjad.glissando(run[:], hide_middle_note_heads=True)
                        else:
                            continue
                    else:
                        continue
        elif self.glissando_style == "hide_middle_stems":
            if self.line_style != None:
                for run in runs:
                    if self.boolean_vector(r=1)[0] is 0:
                        if len(run) > 1:
                            abjad.glissando(
                                run[:],
                                abjad.tweak(self.line_style).style,
                                hide_middle_note_heads=True,
                                hide_middle_stems=True,
                            )
                        else:
                            continue
                    else:
                        continue
            else:
                for run in runs:
                    if self.boolean_vector(r=1)[0] is 0:
                        if len(run) > 1:
                            abjad.glissando(
                                run[:],
                                hide_middle_note_heads=True,
                                hide_middle_stems=True,
                            )
                        else:
                            continue
                    else:
                        continue
        else:
            if self.line_style != None:
                for run in runs:
                    if self.boolean_vector(r=1)[0] is 0:
                        if len(run) > 1:
                            abjad.glissando(
                                run[:],
                                abjad.tweak(self.line_style).style,
                                allow_repeats=True,
                                allow_ties=False,
                            )
                        else:
                            continue
                    else:
                        continue
            else:
                for run in runs:
                    if self.boolean_vector(r=1)[0] is 0:
                        if len(run) > 1:
                            abjad.glissando(
                                run[:], allow_repeats=True, allow_ties=False
                            )
                        else:
                            continue
                    else:
                        continue

    def name(self):
        return self.name

    def state(self):
        return self._count
