from itertools import combinations

def all_substring_of_size_n(s):
    result = set()
    for i in combinations(s, 33):
        if len(set(i)) == len(i):
            result.add(''.join(i))
    return list(result)