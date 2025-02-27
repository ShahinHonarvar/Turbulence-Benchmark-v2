from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = ''.join(sorted(word_lower))
            anagrams[sorted_word].append(word_lower)
    anagram_count = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values()))
    return anagram_count <= 81