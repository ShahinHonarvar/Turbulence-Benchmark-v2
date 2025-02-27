from collections import defaultdict

def if_contains_anagrams(words):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_groups = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            anagram_groups[''.join(sorted(word.lower()))].append(word)
    anagram_pairs = 0
    for group in anagram_groups.values():
        n = len(group)
        anagram_pairs += n * (n - 1) // 2
    return anagram_pairs <= 54