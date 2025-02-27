from collections import Counter

def if_contains_anagrams(lst):
    lst = [word.lower() for word in lst]
    anagram_dict = {}
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            sorted_word = ''.join(sorted(word))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word)
            else:
                anagram_dict[sorted_word] = [word]
    anagram_count = sum((len(words) - 1 for words in anagram_dict.values()))
    return anagram_count <= 69