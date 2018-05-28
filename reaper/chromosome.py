class Chromosome():

    def __init__(self, **kwargs):
        self.name = "Unknown_Chr")
        self.loci = []

        if kwargs.get("name", None):
            self.name = name
        else:
            raise TypeError("The name attribute value must be a string")

        if kwargs.get("loci", None):
            self.loci = loci
        else:
            raise TypeError("The item attribute value must be a Locus list")

    @property
    def size(self):
        return len(self.loci)

    def __repr__(self):
        loci = (item for item in self.loci)
        return "Chr(\"{}\", {})".format(self.name, loci.__repr__())
