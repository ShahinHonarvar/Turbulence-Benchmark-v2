import itertools

def sort_string(s):
    return ''.join(sorted(s.lower()))

def if_contains_anagrams(str_list):
    sorted_strings = [sort_string(s) for s in str_list if len(s) >= 3]
    anagram_pairs = 0
    seen = set()
    for item in sorted_strings:
        if item in seen:
            anagram_pairs += 1
        else:
            seen.add(item)
    return anagram_pairs <= 181