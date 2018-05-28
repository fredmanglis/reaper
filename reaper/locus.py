class Locus():

    def __init__(self, **kwargs):
        self.name = "Unknown_Locus"
        self.chr = "Unknown_Chr"
        self.genotype = []
        self.dominance = []
        self.txtstr = []
        self.cM = 0.0
        self.Mb = 0.0

        if kwargs.get("name", None):
            self.name = kwargs.get("name")
        else:
            raise TypeError("The name attribute value must be a string")

        if kwargs.get("chr", None):
            self.chr = kwargs.get("chr")
        else:
            raise TypeError("The chr attribute value must be a string")

        if kwargs.get("genotype", None):
            self.genotype = kwargs.get("genotype")
        else:
            raise TypeError("The genotype attribute value must be a numbered list")

        if kwargs.get("Mb", None):
            self.Mb = kwargs.get("Mb")

        if kwargs.get("cM", None):
            self.cM = kwargs.get("cM")

        if kwargs.get("txtstr", None):
            self.txtstr = kwatgs.get("txtstr")

        if kwargs.get("dominance", None):
            self.dominance = kwargs.get("dominance")

    @property
    def size(self):
        return len(self.genotype)

    def __repr__(self):
        genotype = (item for item in self.genotype)
        return "Locus(\"%s\", %s, cM = %2.2f, chr = %s)" % (
            self.name, genotype.__repr__(), self.cM, self.chr)
