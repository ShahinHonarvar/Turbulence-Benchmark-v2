from collections import defaultdict

def if_contains_anagrams(words):
    anagram_dict = defaultdict(int)
    for word in words:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagram_dict[sorted_word] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in anagram_dict.values()))
    return anagram_pairs <= 30