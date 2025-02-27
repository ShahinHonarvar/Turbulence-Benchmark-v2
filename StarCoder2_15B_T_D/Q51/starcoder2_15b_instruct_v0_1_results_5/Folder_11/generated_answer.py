import collections

def if_contains_anagrams(words):
    anagram_groups = collections.defaultdict(list)
    for word in words:
        word = word.lower()
        if len(word) >= 3 and all((c.isalpha() for c in word)):
            anagram_groups[tuple(sorted(word))].append(word)
    return len(words) - sum((len(group) - 1 for group in anagram_groups.values())) <= 41