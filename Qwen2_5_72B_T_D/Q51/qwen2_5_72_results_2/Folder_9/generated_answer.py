from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3 and s.isalpha()]
    anagram_pairs = 0
    string_count = Counter([''.join(sorted(s)) for s in strings])
    for count in string_count.values():
        anagram_pairs += count * (count - 1) // 2
    return anagram_pairs <= 475