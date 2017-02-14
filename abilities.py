import statlist


class Ability:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class StatBase:
    def __add__(self, other):
        if isinstance(other, StatBase):
            return Stategory(self.get_stats() + other.get_stats())
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, StatBase):
            here, there = self.get_stats(), other.get_stats()
            return Stategory([x for x in here if x not in there])
        else:
            return NotImplemented

    def get_stats(self):
        raise NotImplementedError


class Stat(StatBase):
    def __init__(self, name):
        assert name in statlist.stats
        self.name = name

    def get_stats(self):
        return [self.name]


class Stategory(StatBase):
    def __init__(self, *names):
        if len(names) == 1 and type(names[0]) == list:
            self.names = names[0]
        else:
            self.names = names
        for name in self.names:
            assert name in statlist.stats

    def get_stats(self):
        return list(self.names)


all_stats = Stategory(*statlist.stats)
no_stats = Stategory()
