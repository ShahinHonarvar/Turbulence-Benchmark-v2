from collections import Counter
    from itertools import combinations

def if_contains_anagrams(lst):
    lst = [word.lower() for word in lst if len(word) >= 3]
    anagrams = set()
    for word in lst:
        sorted_word = ''.join(sorted(word))
        if sorted_word in anagrams:
            return False
        anagrams.add(sorted_word)
    return len(list(combinations(lst, 2))) <= 17