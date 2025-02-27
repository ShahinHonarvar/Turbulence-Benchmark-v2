from collections import Counter

def if_contains_anagrams(lst):
    anagrams = set()
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in anagrams:
                anagrams.remove(sorted_word)
            else:
                anagrams.add(sorted_word)
    return len(anagrams) <= 10