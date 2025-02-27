from collections import defaultdict

def if_contains_anagrams(words):

    def normalize(word):
        return sorted(word.lower())
    anagrams_count = 0
    anagram_groups = defaultdict(list)
    for word in words:
        if len(word) >= 3:
            normalized = normalize(word)
            anagram_groups[normalized].append(word)
    for group in anagram_groups.values():
        anagrams_count += len(group) * (len(group) - 1) // 2
    return anagrams_count >= 65