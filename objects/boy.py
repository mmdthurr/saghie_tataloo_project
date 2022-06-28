from .humanbase import HumanBase
from .errors import GenesNotFunctional


class Boy(HumanBase):
    def __init__(
            self,
            dna,
            location,

    ):
        super().__init__(dna, location)

        self.cheater = None
        self.partner: list = list()

    @property
    def penis(self):
        try:
            return {'penis': self.make_on_dna(self._dna.get('penis'))}
        except GenesNotFunctional:
            return None

    def sex(self, partner: list):
        if self.penis:
            if len(partner) > 1:
                self.cheater = True
            elif len(partner) == 1:
                pass
            else:
                self.brain = 'pure_shit'
