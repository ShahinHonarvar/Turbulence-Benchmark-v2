from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        word_sorted = ''.join(sorted(word.lower()))
        if len(word_sorted) >= 3:
            anagrams[word_sorted].append(word)
    count = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values()))
    return count <= 29