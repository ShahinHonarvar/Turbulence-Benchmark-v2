import itertools
import collections

def if_contains_anagrams(strings):
    count = 0
    for pair in itertools.combinations(strings, 2):
        if len(pair[0]) >= 3 and len(pair[1]) >= 3 and (pair[0].lower() != pair[1].lower()) and (collections.Counter(pair[0].lower()) == collections.Counter(pair[1].lower())):
            count += 1
        if count > 68:
            return False
    return True