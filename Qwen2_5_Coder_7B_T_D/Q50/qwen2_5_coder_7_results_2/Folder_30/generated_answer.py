from collections import defaultdict

def if_contains_anagrams(words):

    def count_anagrams(word):
        return sorted(word.lower())
    anagram_map = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            anagram_map[count_anagrams(word)].append(word)
    pairs = 0
    for group in anagram_map.values():
        n = len(group)
        pairs += n * (n - 1) // 2
    return pairs >= 78