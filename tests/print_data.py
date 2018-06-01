from context import reaper

def run_test():
    dataset = reaper.Dataset()
    dataset.read("tests/data/input/AXB.geno")
    print("Dataset:", dataset)

if __name__ == "__main__":
    run_test()
