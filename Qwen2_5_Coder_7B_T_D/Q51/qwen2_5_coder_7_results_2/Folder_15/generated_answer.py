from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            word_sorted = ''.join(sorted(word.lower()))
            anagrams[word_sorted].append(word)
    anagram_pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values() if len(v) > 1))
    return anagram_pairs <= 20