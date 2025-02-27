from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    anagram_dict = {}
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word] += 1
                count += 1
            else:
                anagram_dict[sorted_word] = 1
    return count <= 16