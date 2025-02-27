from collections import Counter

def if_contains_anagrams(lst):
    anagram_dict = {}
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word] += 1
            else:
                anagram_dict[sorted_word] = 1
    pairs = sum([v * (v - 1) // 2 for v in anagram_dict.values() if v > 1])
    return pairs <= 55