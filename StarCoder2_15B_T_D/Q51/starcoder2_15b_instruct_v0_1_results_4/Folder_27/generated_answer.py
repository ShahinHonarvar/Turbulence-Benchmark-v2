from collections import defaultdict

def if_contains_anagrams(words):
    anagram_groups = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        anagram_groups[sorted_word].append(word)
    anagram_counts = [len(group) for group in anagram_groups.values() if len(group) > 2]
    return len(anagram_counts) <= 113