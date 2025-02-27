from collections import defaultdict

def if_contains_anagrams(lst):
    lowercase_lst = [word.lower() for word in lst]
    anagram_map = defaultdict(int)
    for word in lowercase_lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word] += 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in anagram_map.values()))
    return anagram_pairs <= 88