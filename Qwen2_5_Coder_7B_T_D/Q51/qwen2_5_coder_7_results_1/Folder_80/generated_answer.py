from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word].append(word)
    pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values()))
    return pairs <= 255