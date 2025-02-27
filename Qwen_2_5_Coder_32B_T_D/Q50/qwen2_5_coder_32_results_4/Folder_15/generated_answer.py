from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            anagrams[sorted_word].append(word)
    count = sum((len(v) >= 2 for v in anagrams.values()))
    return count >= 4