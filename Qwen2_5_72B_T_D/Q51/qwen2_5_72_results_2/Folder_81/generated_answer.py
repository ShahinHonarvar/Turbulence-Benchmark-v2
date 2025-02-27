from collections import Counter

def if_contains_anagrams(strings):
    anagram_pairs = 0
    string_list = [s.lower() for s in strings if len(s) >= 3 and s.isalpha()]
    sorted_strings = [''.join(sorted(s)) for s in string_list]
    count = Counter(sorted_strings)
    for value in count.values():
        anagram_pairs += value * (value - 1) // 2
    return anagram_pairs <= 79