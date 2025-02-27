from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(int)
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = tuple(sorted(word))
            anagrams[sorted_word] += 1
    count = sum((v * (v - 1) // 2 for v in anagrams.values()))
    return count >= 189