from .humanbase import HumanBase
from .errors import GenesNotFunctional
from .boy import Boy


class Girl(HumanBase):
    def __init__(
            self,
            dna,
            location,
            brain='pure_shit',

    ):
        super().__init__(dna, location)
        self.brain = brain
        self.cheater = None
        self.slut = None
        self.partner: list = list()

    @property
    def vagina(self):
        try:
            return {'vagina': self.make_on_dna(self._dna.get('vagina'))}
        except GenesNotFunctional:
            return None

    def sex(self):
        if self.vagina:
            if len(self.partner) > 1:
                self.cheater = True
                self.slut = True
            elif len(self.partner) == 1:
                pass
            else:
                self.brain = 'pure_shit'

    def tempting_other_boys(self, boy: [Boy]):
        if len(self.partner) > 0:
            self.cheater = True
            self.slut = True
        else:
            if len(boy) > 1:
                self.slut = True
            else:
                if len(boy[0].partner) > 0:
                    self.slut = True
