from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = defaultdict(int)
    for word in words:
        w_sorted = ''.join(sorted(word.lower()))
        if len(w_sorted) >= 3:
            anagram_count[w_sorted] += 1
    pairs_of_anagrams = sum((v * (v - 1) // 2 for v in anagram_count.values()))
    return pairs_of_anagrams <= 318