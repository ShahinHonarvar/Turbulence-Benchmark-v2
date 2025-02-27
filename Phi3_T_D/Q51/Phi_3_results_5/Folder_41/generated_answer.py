from collections import defaultdict
import itertools

def if_contains_anagrams(strings):
    count = 0
    for grouper in (frozenset(itertools.compress(string, map(str.isalpha, string.lower()))) for string in strings if len(string) >= 3):
        anagram_groups = defaultdict(list)
        for word in strings:
            if len(word) >= 3 and all((c.isalpha() for c in word.lower())):
                key = frozenset(itertools.compress(word, map(str.isalpha, word.lower())))
                anagram_groups[key].append(word)
        for group in anagram_groups.values():
            if len(group) > 2:
                count += len(list(itertools.combinations(group, 2)))
    return count <= 52