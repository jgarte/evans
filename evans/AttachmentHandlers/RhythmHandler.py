import abjad


class RhythmHandler:
    def __init__(self, rmaker, continuous=False, state=None, name="Rhythm Handler"):
        self.rmaker = rmaker
        self.continuous = continuous
        self.state = self.rmaker.state
        self.name = name

    def __call__(self, durations):
        return self._make_music(durations)

    def _make_basic_rhythm(self, durations):
        if self.continuous == True:
            selections = self.rmaker(durations, previous_state=self.rmaker.state)
            self.state = self.rmaker.state
        else:
            selections = self.rmaker(durations)
        return selections

    def _make_music(self, durations):
        selections = self._make_basic_rhythm(durations)
        return selections

    def name(self):
        return self.name

    def state(self):
        return self.rmaker.state
