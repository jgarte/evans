import abjad


class Command:
    def __init__(
        self,
        command=None,
        indicator=None,
        selector=None,
        voice=None,
    ):
        """
        Initializes Command.
        """
        self.command = command
        self.indicator = indicator
        self.selector = selector
        self.voice = voice

    def __call__(self, score):
        """
        Calls command on Score.

        >>> score = abjad.Score([abjad.Staff("c'4 c'4 c'4 c'4", name="staff one")])
        >>> command = evans.Command(
        ...     command="attach",
        ...     indicator=abjad.Markup("*", direction="up"),
        ...     selector=abjad.select().leaves(pitched=True).get([1])[0],
        ...     voice="staff one"
        ... )
        ...
        >>> command(score)
        >>> abjad.f(score)
        \new Score
        <<
            \context Staff = "staff one"
            {
                c'4
                c'4
                ^ \markup { * }
                c'4
                c'4
            }
        >>

        """
        location = score[self.voice]
        if self.command == "attach":
            abjad.attach(self.indicator, self.selector(location))
        if self.command == "detach":
            abjad.detach(self.indicator, self.selector(location))