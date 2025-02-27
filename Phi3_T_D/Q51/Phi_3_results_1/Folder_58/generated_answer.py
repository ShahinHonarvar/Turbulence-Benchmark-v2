from collections import Counter

def if_contains_anagrams(strings):

    def count_anagrams(s):
        char_count = Counter(s.lower())
        return sum([1 for k, v in char_count.items() if v >= 2])
    potential_anagrams = {}
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            potential_anagrams.setdefault(sorted_string, []).append(string)
    anagrams_count = sum((1 for group in potential_anagrams.values() if len(group) > 1))
    return anagrams_count <= 60