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
violence = Stategory("Strength", "Foreclosure", "Quips", "Scrub", "Intimidation", "Level", "Hammer", "Punchpoints",
                     "Defenestration", "Fisticuffs", "Jerk", "Power Level", "Ball", "Shark", "Physicality")
stamina = Stategory("Lung Capacity", "Flux Retention", "Constitution", "Composure", "Hitpoints", "Structural Integrity",
                    "Abs", "Fisticuffs", "Humors", "Homeostasis", "Plot Armor", "Genre-Savviness", -"Arachnophobia",
                    "Regenerations")
hacking = Stategory("Perception", "Trenchcoat", "Aspestos", -"Credit Rating", "Defenestration", "Duplicity",
                    "Min-Maxing", "Arachnophobia", "Luminosity", "Decryption", "Faults", "Hairtie", "Ingress")
mentality = Stategory("Psychological Logic Analyzer", "Gruntle", -"Whelm", -"Alcohol by Volume", "Denial",
                      "Reading Comprehension", "Characterization", -"Consecutive All-Nighters", "Humor",
                      "Remaining Drive Space", -"Hunger", "Active Instances", "Dramatic Pauses", "Liminality",
                      "Reality")
ideology = Stategory("Communism", "Capitalism", "Sickle-Cell Anemia", "Post-Structuralism", "Equity", "Martyrdom",
                     "Objectivity", "Moral Fiber", "Amoral Fiber", "Liminality", "Constitution", "State", "Google",
                     "Shakespeare", "Globe", "Interrogation", "Polyamorous Ticking", "Globalism", "Technocracy")
wealth = Stategory("Security Clearance", "Equity", "Avarice", "Amoral Fiber", "Duplicity", "Hair Width", "Haberdashery",
                   "Foreclosure", "Cheesemaking", "State", "Fizzbuzz", "Faults", "Shark", "Whiteboard Dry-Erase Marker",
                   "Regional Transfer Rate", "Student ID", "Materialism", "Gender", "Capitalism")
individuality = Stategory("Impurity Score", "Backstory", "Characterization", "Larval Stages", "Insolence", "Edginess",
                          -"Active Instances", -"Dissociation", "Blindness", "Liminality", "Intertextuality",
                          -"Reality", "Gender", "Silly Hats", "Indie Cred")
construction = Stategory("Dexterity", "Flux Retention", "Voltmeter", "Composer", "Instantiation", "Instigation",
                         "Mechanic", "Civility", "Materialism", "Electricity", )
incapability = Stategory("Blindness", "Arachnophobia", "Reality", "dril", "Headphones", "Apology", "Capitalism",
                         "Technocracy", "Comfort", "Discomfort", "Remaining Download Time", "Tetanus")
farming = Stategory("Flora", "Fauna", "Bird", "Atmosthetic", "Communism", "Squids per Hour")
magic = Stategory("Orb", "Sphere", "Ball", "Globe", "Sodium", "Physicality", "Cognition", "Avuncular Charm",
                  "Consecutive Vowels", "Rhythm", "Penalty Kicks")
consumption = Stategory(-"Hunger", "Total Carbohydrates", "Service Size")
