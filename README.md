# Reaper

## Introduction

This is an attempt to translate https://github.com/pjotrp/QTLReaper into a pure
Python3 library.

## Usage

reaper.Dataset is the main class you'll use often. You can use this by doing something like:

    import reaper

Once you have done that, you initialise the dataset by reading in a file in the following way:

    import reaper
    dataset = reaper.Dataset() # or simply Dataset() if you used the from method
    dataset.read("/path/to/geno/file.geno")

That should load and parse the geno file into python objects.

## Running tests

You can run tests by doing something like:

    python tests/runtests.py

to run the same tests in QTLReaper.
To display the parsed data, do:

    python tests/print_data.py

## TODOs

- [x] Enable Parsing
- [ ] Fix any errors with parsing

The permutations and regression features are not being ported at this moment.