
class Term:
    def __init__(self, value, weight, count):
        self.value = value
        self.weight = weight
        self.count = count

    @property
    def format(self):
        r = 'value:  ' + self.value + '\nweight:  ' + self.weight + '\ncount:  ' + self.count
        return r
