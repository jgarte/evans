import abjad
from evans.AttachmentHandlers.CyclicList import CyclicList


class BendHandler:
    r"""
    >>> staff = abjad.Staff("c'4 c'4 c'4 c'4")
    >>> handler = evans.BendHandler(
    ...     bend_amounts=[1, 1.5],
    ...     bend_continuous=True,
    ...     boolean_vector=[1, 1, 0, 1],
    ...     vector_continuous=True,
    ... )
    >>> handler(staff)
    >>> abjad.f(staff)
    \new Staff
    {
        c'4
        - \bendAfter #'1
        c'4
        - \bendAfter #'1.5
        c'4
        c'4
        - \bendAfter #'1.5
    }

    """

    def __init__(
        self,
        bend_amounts=[1],
        bend_continuous=True,
        boolean_vector=[0],
        vector_continuous=True,
        bend_count=-1,
        vector_count=-1,
        name="Bend Handler",
    ):
        self._bend_count = bend_count
        self._vector_count = vector_count
        self.bend_continuous = bend_continuous
        self.vector_continuous = vector_continuous
        self.bend_amounts = CyclicList(
            bend_amounts, self.bend_continuous, self._bend_count
        )
        self.boolean_vector = CyclicList(
            boolean_vector, self.vector_continuous, self._vector_count
        )
        self.name = name

    def __call__(self, selections):
        self.add_bend(selections)

    def add_bend(self, selections):
        ties = abjad.select(selections).logical_ties(pitched=True)
        vector = self.boolean_vector(r=len(ties))
        amounts = self.bend_amounts(r=len(ties))
        for tie, bool, amount in zip(ties, vector, amounts):
            if bool == 1:
                abjad.attach(abjad.BendAfter(amount), tie[-1])
            else:
                continue

    def name(self):
        return self.name

    def state(self):
        return abjad.OrderedDict(
            [
                ("bend_count", self.bend_amounts.state()),
                ("vector_count", self.boolean_vector.state()),
            ]
        )
