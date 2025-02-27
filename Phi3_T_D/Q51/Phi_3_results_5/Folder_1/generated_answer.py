from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower()) and len(s1) >= 3
    anagram_dict = defaultdict(list)
    for s in strings:
        anagram_dict[''.join(sorted(s.lower()))].append(s)
    anagram_pairs = 0
    for anagrams in anagram_dict.values():
        n = len(anagrams)
        if n > 1:
            anagram_pairs += n * (n - 1) // 2
    return anagram_pairs <= 30