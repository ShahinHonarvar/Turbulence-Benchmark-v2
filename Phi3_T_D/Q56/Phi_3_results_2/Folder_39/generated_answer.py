from itertools import combinations

def all_substring_of_size_n(s):
    n = 94
    result = []
    all_combinations = combinations(set(s), n)
    for combination in all_combinations:
        substring = ''.join(combination)
        if substring not in result:
            result.append(substring)
    return result