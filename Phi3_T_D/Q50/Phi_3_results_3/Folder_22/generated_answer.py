import itertools

def if_contains_anagrams(strings):
    string_lengths = [len(s) for s in strings]
    minimum_length = max(min(string_lengths), 3)
    anagrams = {}
    for s in strings:
        s_lower = s.lower()
        sorted_s = ''.join(sorted(s_lower))
        if len(s) >= minimum_length:
            anagrams[sorted_s] = anagrams.get(sorted_s, 0) + 1
    anagram_count = sum((count for count in anagrams.values() if count > 1))
    return anagram_count // 2 >= 72