from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            anagrams[sorted_word].append(word)
    count = 0
    for group in anagrams.values():
        n = len(group)
        count += n * (n - 1) // 2
    return count <= 30