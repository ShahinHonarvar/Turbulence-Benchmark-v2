from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = 0
    anagrams = defaultdict(list)
    for word in words:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = ''.join(sorted(word_lower))
            anagrams[sorted_word].append(word_lower)
    for group in anagrams.values():
        n = len(group)
        if n > 1:
            anagram_count += n * (n - 1) // 2
    return anagram_count <= 255