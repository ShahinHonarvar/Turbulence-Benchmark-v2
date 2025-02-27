from collections import Counter

def if_contains_anagrams(lst):
    lst = [word.lower() for word in lst if len(word) >= 3]
    anagram_dict = {}
    for word in lst:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    anagram_counts = [len(words) for words in anagram_dict.values() if len(words) > 1]
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts))
    return anagram_pairs >= 94