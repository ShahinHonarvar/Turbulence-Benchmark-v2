import collections

def if_contains_anagrams(words):
    anagram_groups = collections.defaultdict(list)
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagram_groups[sorted_word].append(word)
    anagram_counts = [len(group) for group in anagram_groups.values() if len(group) >= 2]
    return len(anagram_counts) <= 14