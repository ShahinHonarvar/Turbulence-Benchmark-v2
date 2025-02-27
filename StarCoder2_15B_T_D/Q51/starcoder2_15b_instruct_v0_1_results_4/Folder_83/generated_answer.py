import collections

def if_contains_anagrams(words):
    anagram_groups = collections.defaultdict(list)
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagram_groups[sorted_word].append(word)
    for group in anagram_groups.values():
        if len(group) > 1:
            return True
    return False