from .location import Location
from .errors import GenesNotFunctional


class HumanBase:
    def __init__(
            self,
            dna: dict,
            location: Location,
    ):
        self._dna = dna
        self.location = location

    def make_on_dna(self, genes):
        if genes and self._dna:
            return True

    @property
    def leg(self):
        # bone , skin , muscle
        try:
            bone_dict = {
                'bones': {
                    'fibula': self.make_on_dna(self._dna.get('fibula_bone')),
                    'tibia': self.make_on_dna(self._dna.get('tibia_bone')),
                    'femur': self.make_on_dna(self._dna.get('femur_bone'))
                },
                'muscle': self.make_on_dna(self._dna.get('leg_muscle'))

            }
        except GenesNotFunctional:
            bone_dict = None
        if bone_dict:
            bone_dict['skin'] = self.make_on_dna(self._dna.get('skin_base'))
            return bone_dict
        else:
            return None

    @property
    def maximum_movement_on_leg(self):
        if self.leg:
            return self.leg.get('size_in_m') * 2
        else:
            return None

    @staticmethod
    def mucosal_folds(mucosal, i_t='i'):
        if i_t == 'i':
            pass
        else:
            pass

    @property
    def throat(self):
        try:
            throat = {
                'vocal_cord': self.mucosal_folds(self.make_on_dna(self._dna.get('cords_mucosal'))),
                'epiglottis': self.make_on_dna('epiglottis'),
            }
        except GenesNotFunctional:
            throat = None
        return throat

    @property
    def mouth(self):
        try:
            mouth = {
                'teeth': self.make_on_dna(self._dna.get('teeth')),
                'tongue': self.make_on_dna(self._dna.get('tongue')),
            }
        except GenesNotFunctional:
            mouth = None
        mouth['lips'] = self.make_on_dna(self._dna.get('lips'))
        return mouth

    def talk(self, txt, pitch, lang='fa'):
        p = 'girl' if pitch == 'high' else 'boy'
        if self.mouth and self.throat:
            if lang == 'fa':
                print(f'{p}:{txt}')
        else:
            pass

    def walk(self, route, percent):
        # not complete should be written again to be evaluated in 3d aspect
        if self.leg:
            pass
