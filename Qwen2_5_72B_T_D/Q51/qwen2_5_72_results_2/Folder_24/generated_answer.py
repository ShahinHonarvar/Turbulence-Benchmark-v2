from collections import Counter

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_dict = {}
    for word in words:
        if len(word) >= 3:
            normalized_word = normalize(word)
            if normalized_word in anagram_dict:
                anagram_dict[normalized_word] += 1
            else:
                anagram_dict[normalized_word] = 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return anagram_pairs <= 96