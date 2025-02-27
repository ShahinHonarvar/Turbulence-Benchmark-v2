from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagram_dict[sorted_word] += 1
    anagram_pairs = sum((count >= 2 for count in anagram_dict.values()))
    return anagram_pairs <= 4