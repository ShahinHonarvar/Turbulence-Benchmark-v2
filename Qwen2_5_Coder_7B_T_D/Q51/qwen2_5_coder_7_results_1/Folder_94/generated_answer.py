from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word].append(word)
    anagram_pairs = 0
    for words in anagram_dict.values():
        n = len(words)
        anagram_pairs += n * (n - 1) // 2
    return anagram_pairs <= 181