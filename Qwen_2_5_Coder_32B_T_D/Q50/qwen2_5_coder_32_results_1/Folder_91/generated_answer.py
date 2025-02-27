from collections import defaultdict

def if_contains_anagrams(words):
    anagrams = defaultdict(list)
    for word in words:
        w = word.lower()
        if len(w) >= 3:
            sorted_word = ''.join(sorted(w))
            anagrams[sorted_word].append(w)
    return sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values())) >= 6