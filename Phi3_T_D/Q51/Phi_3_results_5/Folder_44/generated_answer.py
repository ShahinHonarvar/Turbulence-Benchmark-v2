from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    def string_length(_str):
        return len(_str)
    anagrams_count = defaultdict(int)
    for s in strings:
        if string_length(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        anagrams_count[sorted_str] += 1
    pairs = sum((v * (v - 1) // 2 for v in anagrams_count.values()))
    return pairs <= 75