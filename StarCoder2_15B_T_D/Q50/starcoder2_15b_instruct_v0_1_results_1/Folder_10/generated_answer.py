import collections

def if_contains_anagrams(words):
    if len(words) < 52:
        return False
    anagram_groups = collections.defaultdict(list)
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagram_groups[sorted_word].append(word)
    return any((len(group) >= 2 for group in anagram_groups.values()))