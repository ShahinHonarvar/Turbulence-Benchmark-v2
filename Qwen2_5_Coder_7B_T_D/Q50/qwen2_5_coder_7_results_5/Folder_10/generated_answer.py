from collections import defaultdict

def if_contains_anagrams(lst):
    anagram_dict = defaultdict(list)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        if len(sorted_word) >= 3:
            anagram_dict[sorted_word].append(word.lower())
    for anagrams in anagram_dict.values():
        if len(anagrams) > 1:
            if len(anagrams) * (len(anagrams) - 1) // 2 >= 52:
                return True
    return False