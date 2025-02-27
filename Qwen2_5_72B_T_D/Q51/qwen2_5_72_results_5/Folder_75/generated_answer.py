from collections import Counter

def if_contains_anagrams(lst):
    lst = [word.lower() for word in lst if len(word) >= 3 and word.isalpha()]
    anagram_pairs = 0
    seen = {}
    for word in lst:
        sorted_word = ''.join(sorted(word))
        if sorted_word in seen:
            anagram_pairs += seen[sorted_word]
            seen[sorted_word] += 1
        else:
            seen[sorted_word] = 1
    return anagram_pairs <= 55