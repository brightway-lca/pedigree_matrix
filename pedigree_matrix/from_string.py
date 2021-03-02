import re

expression = r"""^\([ ]?
([1-5]|[na\.]{1,4}|[\-])?[ ]?,[ ]?
([1-5]|[na\.]{1,4}|[\-])?[ ]?,[ ]?
([1-5]|[na\.]{1,4}|[\-])?[ ]?,[ ]?
([1-5]|[na\.]{1,4}|[\-])?[ ]?,[ ]?
([1-5]|[na\.]{1,4}|[\-])?
[ ]?,?[ ]?
([1-5]|[na\.]{1,4}|[\-])?[ ]?
\)"""
compiled = re.compile(expression, re.IGNORECASE | re.VERBOSE)


def as_integer(x):
    try:
        return int(x)
    except:
        return 1


def find_pedigree_matrix(string):
    if compiled.search(string):
        if len(compiled.findall(string)) > 1:
            raise ValueError("Multiple Pedigree Matrix strings found")
        return tuple([as_integer(x) for x in compiled.search(string).groups()])
    else:
        return False
