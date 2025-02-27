from collections import Counter

def if_contains_anagrams(words):
    words = [word.lower() for word in words]
    words = [word for word in words if len(word) >= 3]
    anagram_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_dict:
            anagram_dict[sorted_word].append(word)
        else:
            anagram_dict[sorted_word] = [word]
    anagram_pairs = 0
    for anagram_group in anagram_dict.values():
        n = len(anagram_group)
        if n > 1:
            anagram_pairs += n * (n - 1) // 2
    return anagram_pairs <= 318