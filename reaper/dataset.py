from . import Chromosome, Locus

MAX_MARKERNAME_SIZE = 256
MAX_GENONAME_SIZE = 256
MAX_CHROMOSOMES = 100
MAX_MARKERS = 100000
GENOSYMBOL = "BHDU"

class Dataset():

    def __init__(self, **kwargs):
        self.name = "Unknown_Dataset"
        self.mat = "mat"
        self.pat = "pat"
        self.type = "riset"

        self.chromosome = []
        self.prgy = []
        self.parentsf1 = 0
        self.dominance = 0
        self.Mb = 0
        self.interval = 0

        if kwargs.get("name", None):
            self.name = kwargs.get("name")
        else:
            raise TypeError("reaper: The name attribute value must be a string")

        if kwargs.get("chromosome", None):
            self.chromosome = kwargs.get("chromosome")
        else:
            raise TypeError("reaper: The chromosome attribute value must be a Chromosome list")

    @property
    def size(self):
        return len(self.chromosome)

    @property
    def nprgy(self):
        return len(self.prgy)

    def addinterval(self):
        """Add interval map"""
        if self.interval == 1:
            raise RuntimeError("reaper: This dataset already contains intervals")

        # if not parse_tuple(args, "|d", interval):
        #     return None

        if self.interval < 1.0:
            self.interval = 1.0

    def add(self, **kwargs):
        """Add parents/F1 genotypes, return new object"""
        i = 0
        n = 0
        strains = []
        values = []

        if self.parentsf1 == 1:
            raise RuntimeError("reaper: Parents and F1 have already been added")

        if self.dominance == 1:
            raise RuntimeError("reaper: Parents and F1 cannot be added to F2 set")

        if kwargs.get("F1", None):
            strains[n] = GENOSYMBOL[2]
            values[n] = 0.0
            n = n + 1
            self.prgy.append(kwargs.get("F1"))

        if kwargs.get("mat", None):
            strains[n] = GENOSYMBOL[0]
            values[n] = -1.0
            n = n + 1
            self.prgy.append(kwargs.get("mat"))

        if kwargs.get("pat", None):
            strains[n] = GENOSYMBOL[1]
            values[n] = 1.0
            n = n + 1
            self.prgy.append(kwargs.get("pat"))

        # This method might need more work

        if n > 0:
            self.parentsf1 = 1;

    def read(self, filename):
        """Read genotypes from a file"""
        header=False
        genStartPos = 3
        mat = ""
        pat = ""
        het = "H"
        unk = "U"
        chromosomes = {}

        # I have no idea what this is doing in the C
        # if (! PyArg_ParseTuple(args,"O", &file))
        #   return NULL;
        fp = open(filename, "rb")
        lSize = fp.seek(0, 2) # Get file size
        fp.seek(0,0) # rewind
        self.clearChromosome()

        decode = lambda s: s.decode("utf-8")
        all_lines = [decode(line) for line in fp.readlines() if not (
            decode(line)[0] == "#" or decode(line)[0] == "\0")]
        chr_lines = [line for line in all_lines() if not line[0] == "@"]
        tabCount = len(chr_lines[0].split("\t"))
        if not all(len(items.split("\t")) == tabCount for items in chrlines):
            raise "reaper: Each line should have the same number of Tabs"

        chr_lines2 = [decode(line) for line in fp.readlines() if not (
            decode(line)[0] == "#" or decode(line)[0] == "\0" or decode(line)[0] == "@")]
        for line in all_lines:
            if line[0] == "@":
                parts = line.split(":")
                if parts[0] == "@type":
                    self.type = parts[1].strip()
                    if self.type == "intercross":
                        self.dominance = 1
                elif parts[0] == "@mat":
                    self.mat = parts[1].strip()
                    mat = self.mat
                elif parts[0] == "@pat":
                    self.pat = parts[1].strip()
                    pat = self.pat
                elif parts[0] == "@het":
                    het = parts[1].strip()
                elif parts[0] == "@unk":
                    unk = parts[1].strip()
                elif parts[0] == "@name":
                    self.name = parts[1].strip()
                else:
                    pass
            elif line.startswith("Chr\tLocus\tcM"):
                parts = list(map(lambda s: s.strip(), line.split("\t")))
                self.prgy = []

                if "Mb" in parts:
                    self.Mb = 1
                    genStartPos += 1

                self.prgy = parts[genStartPos:]
                header = True
                continue
            elif len(line) > 0:
                if not header:
                    raise SystemError("reaper: Header row is not located")

                setGenotypeValue = lambda g: -1.0 if g == GENOSYMBOL[0] else (
                    1.0 if g == GENOSYMBOL[1] else (0.0 if g == GENOSYMBOL[2] else g))
                setDominanceValue = lambda g: 0 if (g == mat and self.dominance == 1) else (
                    0 if (g == pat and self.dominance == 1) else (
                        1 if (g == het and self.dominance == 1) else (
                            1 if (g == unk and self.dominance ==1) else self.dominance)))
                
                parts = list(map(lambda s: s.strip(), line.split("\t")))
                txtstr = [gen for gen in parts[genStartPos:]]
                genotypes = [setGenotypeValue(gen) for gen in textstr]
                dominance = [setDominanceValue(gen) for gen in textstr]
                Mb = atof(parts[genStartPos-1]) if genStartPos > 3 else 0.0
                
                locus = Locus(name=parts[1], chr=parts[0], cM=atof(parts[2]),
                              Mb=Mb, genotype=genotypes, txtstr=txtstr,
                              dominance=dominance)

                chromosome = chromosomes.get(parts[0], None)
                if(chromosome):
                    chromosome.loci.append(locus)
                else:
                    chromosome = Chromosome(name=parts[0], loci=[locus])

                chromosomes[parts[0]] = chromosome
            else:
                pass # do nothing

        fp.close()
        self.chromosome = list(chromosomes.values())

    def regression(self):
        """regression using input values"""
	# {"regression", (PyCFunction)Dataset_regression,
	# METH_KEYWORDS, "regression using input values"},
        pass

    def permutation(self):
        """Permutation test"""
	# {"permutation", (PyCFunction)Dataset_permutation,
	# METH_KEYWORDS, "Permutation test"},
        pass

    def bootstrap(self):
        """Bootstrap test"""
	# {"bootstrap", (PyCFunction)Dataset_bootstrap,
	# METH_KEYWORDS, "Bootstrap test"},
        pass

    def clearChromosome(self):
        self.chromosome = []
        self.prgy = []
        self.parentsf1 = 0
        self.dominance = 0
        self.Mb = 0
        self.interval = 0

    def __repr__(self):
        prgy = (item for item in self.nprgy)
        chromosome = (item for item in self.chromosome)
        return "Dataset(\"{}\", prgy{}, {})".format(
            self.name, prgy.__repr__(), chromosome.__repr__())
