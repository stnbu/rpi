
class Axis(object):

    _defaults = {
        'name': None,
        'min': 0,
        'max': 0,
        'center': None,
        'reversed': False,
    }

    def __init__(self, **kwargs):
        if set(kwargs) - set(self._defaults):
            raise ValueError('Unsupported argument(s): {}'.format(', '.join(set(kwargs) - set(self._defaults))))
        for name, value in self._defaults.iteritems():
            setattr(self, name, value)
        for name, value in kwargs.iteritems():
            setattr(self, name, value)

    @property
    def range(self):
        return self.max - self.min

    def get_normalized_position(self, raw_position):
        # return value between -1 and +1
        return 2 * (float(raw_position - self.min) / float(self.max - self.min)) - 1

data = {
    0: Axis(name='throttle', min=159, max=869, center=516),
    1: Axis(name='aileron', min=174, max=755, center=499, reversed=True),
    2: Axis(name='elevator', min=191, max=844, center=511, reversed=True),
    3: Axis(name='rudder', min=175, max=857, center=511),
    4: Axis(name='gear', min=173, max=869),
    5: Axis(name='flaps', min=164, max=725),
    6: Axis(name='UNUSED', min=164, max=725),
}

