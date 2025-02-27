from itertools import islice

def all_substring_of_size_n(s):
    n = 120
    substrs = set()
    for i in range(len(s) - n + 1):
        substr = ''.join(sorted(islice(s, i, i + n)))
        if len(set(substr)) == n:
            substrs.add(substr)
    return list(substrs)