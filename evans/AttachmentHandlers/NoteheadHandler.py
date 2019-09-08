import abjad
from evans.AttachmentHandlers.CyclicList import CyclicList


class NoteheadHandler:
    def __init__(
        self,
        notehead_list=None,
        transition=False,
        head_boolean_vector=[0],
        head_vector_continuous=True,
        transition_boolean_vector=[0],
        transition_vector_continuous=True,
        continuous=False,
    ):
        self.notehead_list = notehead_list
        self.transition = transition
        self.head_vector_continuous = head_vector_continuous
        self._head_vector_count = -1
        self.head_boolean_vector = CyclicList(
            head_boolean_vector, self.head_vector_continuous, self._head_vector_count
        )
        self.transition_vector_continuous = transition_vector_continuous
        self._transition_vector_count = -1
        self.transition_boolean_vector = CyclicList(
            transition_boolean_vector,
            self.transition_vector_continuous,
            self._transition_vector_count,
        )
        self.continuous = continuous
        self._count = -1
        self._cyc_noteheads = CyclicList(notehead_list, self.continuous, self._count)

    def __call__(self, selections):
        self.add_noteheads(selections)

    def add_noteheads(self, selections):
        ties = abjad.select(selections).logical_ties(pitched=True)
        heads = self._cyc_noteheads(r=len(ties))
        head_vector = self.head_boolean_vector(r=len(ties))
        trans_vector = self.transition_boolean_vector(r=len(ties))
        if self.notehead_list != None:
            for tie, head, bool in zip(ties, heads, head_vector):
                string = str(r"""\once \override Staff.NoteHead.style = #'""")
                full_string = string + head
                style = abjad.LilyPondLiteral(full_string, format_slot="before")
                if bool1 is 0:
                    for leaf in abjad.select(tie).leaves(pitched=True):
                        abjad.attach(style, leaf)
                else:
                    continue
        if self.transition == True:
            transition_arrow = abjad.LilyPondLiteral(
                r"""
                - \tweak arrow-length #2
                - \tweak arrow-width #0.5
                - \tweak bound-details.right.arrow ##t
                - \tweak thickness #2.5
                \glissando
            """,
                "absolute_after",
            )
            for tie, bool1, bool2 in zip(ties, heads, head_vector, trans_vector):
                if bool1 is 0:
                    if bool2 is 0:
                        abjad.attach(transition_arrow, tie[-1])
                    else:
                        continue
                else:
                    continue
            for run in abjad.select(selections).runs():
                last_tie = abjad.select(run).logical_ties(pitched=True)[-1]
                abjad.detach(transition_arrow, last_tie[-1])


# - \tweak arrow-length #2
# - \tweak arrow-width #0.5
# - \tweak bound-details.right.arrow ##t
# - \tweak thickness #3
# \glissando