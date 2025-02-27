from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if s.isalpha() and len(s) >= 3]
    anagram_pairs = 0
    seen = {}
    for string in strings:
        sorted_string = ''.join(sorted(string))
        if sorted_string in seen:
            anagram_pairs += seen[sorted_string]
            seen[sorted_string] += 1
        else:
            seen[sorted_string] = 1
    return anagram_pairs <= 15