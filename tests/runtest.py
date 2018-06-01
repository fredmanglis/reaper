import os
from context import reaper
geno = reaper.Dataset()
geno.read("tests/data/input/AXB.geno")
print(geno.type)
print(list(geno.prgy))
