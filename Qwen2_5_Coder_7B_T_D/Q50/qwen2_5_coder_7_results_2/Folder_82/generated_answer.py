from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            anagrams[sorted_word].append(word)
    count = 0
    for words in anagrams.values():
        n = len(words)
        count += n * (n - 1) // 2
    return count >= 276