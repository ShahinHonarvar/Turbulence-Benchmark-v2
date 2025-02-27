from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            anagrams[word].append(word)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values()))
    return anagram_pairs <= 423