from collections import Counter

def if_contains_anagrams(lst):
    lst = [word.lower() for word in lst if len(word) >= 3 and word.isalpha()]
    anagram_dict = {}
    for word in lst:
        sorted_word = ''.join(sorted(word))
        anagram_dict[sorted_word] = anagram_dict.get(sorted_word, 0) + 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return anagram_pairs <= 42