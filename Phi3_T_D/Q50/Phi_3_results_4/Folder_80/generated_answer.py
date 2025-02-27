from itertools import combinations

def get_sorted_tuple(s):
    return tuple(sorted(s.lower()))

def if_contains_anagrams(string_list):
    length_three_strings = [s for s in string_list if len(s) >= 3]
    sorted_tuples = [get_sorted_tuple(s) for s in length_three_strings]
    count = sum((1 for pair in combinations(sorted_tuples, 2) if pair[0] == pair[1]))
    return count >= 19