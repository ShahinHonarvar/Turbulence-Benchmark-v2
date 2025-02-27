from collections import Counter

def if_contains_anagrams(lst):
    lst = [word.lower() for word in lst if len(word) >= 3 and word.isalpha()]
    anagram_counter = Counter((tuple(Counter(word).items()) for word in lst))
    pairs = sum((count * (count - 1) // 2 for count in anagram_counter.values()))
    return pairs <= 55