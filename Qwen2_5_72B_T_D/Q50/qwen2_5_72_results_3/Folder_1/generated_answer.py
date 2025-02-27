from collections import Counter

def if_contains_anagrams(words):
    words = [word.lower() for word in words if len(word) >= 3]
    anagram_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        anagram_dict[sorted_word] = anagram_dict.get(sorted_word, 0) + 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return anagram_pairs >= 96