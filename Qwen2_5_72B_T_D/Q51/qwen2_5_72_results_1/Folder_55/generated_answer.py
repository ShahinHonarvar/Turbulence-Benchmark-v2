from collections import Counter

def if_contains_anagrams(lst):
    lst = [word.lower() for word in lst if len(word) >= 3 and word.isalpha()]
    anagram_count = 0
    anagram_groups = {}
    for word in lst:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagram_groups:
            anagram_groups[sorted_word].append(word)
        else:
            anagram_groups[sorted_word] = [word]
    for group in anagram_groups.values():
        anagram_count += len(group) * (len(group) - 1) // 2
    return anagram_count <= 44