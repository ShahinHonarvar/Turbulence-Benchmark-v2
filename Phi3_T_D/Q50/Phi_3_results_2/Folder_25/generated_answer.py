from itertools import combinations

def if_contains_anagrams(strings_list):
    min_len = 3
    count = 0
    strings_list = [s.lower() for s in strings_list if len(s) >= min_len]
    for pair in combinations(strings_list, 2):
        if sorted(pair[0]) == sorted(pair[1]):
            count += 1
        if count >= 14:
            return True
    return False