from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            anagrams[sorted_word].append(word)
    pairs = 0
    for key in anagrams:
        if len(anagrams[key]) > 1:
            pairs += 1
    return pairs <= 4