from collections import Counter

def if_contains_anagrams(lst):
    lst = [word.lower() for word in lst if len(word) >= 3]
    anagram_counter = Counter((tuple(sorted(word)) for word in lst))
    return sum((count >= 2 for count in anagram_counter.values())) >= 36