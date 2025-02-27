from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagrams[sorted_word].append(word)
    anagram_pairs = 0
    for group in anagrams.values():
        if len(group) > 1:
            anagram_pairs += len(group) * (len(group) - 1) // 2
    return anagram_pairs >= 177