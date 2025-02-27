from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if s.isalpha() and len(s) >= 3]
    anagram_pairs = 0
    string_counter = Counter([''.join(sorted(s)) for s in strings])
    for count in string_counter.values():
        anagram_pairs += count * (count - 1) // 2
    return anagram_pairs <= 35