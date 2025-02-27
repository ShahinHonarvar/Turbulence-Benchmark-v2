from collections import Counter

def if_contains_anagrams(lst):
    words = [word.lower() for word in lst if len(word) >= 3]
    anagram_groups = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word]
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in anagram_groups.values()))
    return anagram_pairs <= 96