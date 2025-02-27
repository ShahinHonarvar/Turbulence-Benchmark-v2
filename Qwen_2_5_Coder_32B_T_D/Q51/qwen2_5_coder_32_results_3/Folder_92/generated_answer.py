from collections import defaultdict

def if_contains_anagrams(words):
    anagram_count = defaultdict(int)
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagram_count[sorted_word] += 1
    pairs_of_anagrams = sum((comb - 1 for comb in anagram_count.values() if comb > 1))
    return pairs_of_anagrams <= 34