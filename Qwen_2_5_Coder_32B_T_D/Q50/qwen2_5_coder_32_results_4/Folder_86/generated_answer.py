from collections import Counter
    from itertools import combinations

def if_contains_anagrams(words):
    anagram_dict = {}
    for word in words:
        word_lower = word.lower()
        if len(word_lower) >= 3:
            sorted_word = ''.join(sorted(word_lower))
            if sorted_word in anagram_dict:
                anagram_dict[sorted_word].append(word_lower)
            else:
                anagram_dict[sorted_word] = [word_lower]
    anagram_count = sum((len(list(combinations(group, 2))) for group in anagram_dict.values() if len(group) > 1))
    return anagram_count >= 115