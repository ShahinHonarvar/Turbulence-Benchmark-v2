from collections import defaultdict
import itertools
import math

def create_key(s):
    return ''.join(sorted(s.lower()))

def string_generator(lst):
    for L in range(3, math.ceil(math.log(len(lst), 2)) + 1):
        for subset in itertools.combinations(lst, L):
            yield tuple(sorted(subset))

def if_contains_anagrams(lst):
    counter = defaultdict(int)
    for tup in string_generator(lst):
        k = create_key(tup)
        counter[k] += 1
        if counter[k] > 92:
            return False
    return True