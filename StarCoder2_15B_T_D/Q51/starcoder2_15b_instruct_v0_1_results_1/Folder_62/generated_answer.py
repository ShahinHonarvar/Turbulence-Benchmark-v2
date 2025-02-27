import itertools

def if_contains_anagrams(lst):
    anagrams = {}
    for word1, word2 in itertools.combinations(lst, 2):
        if sorted(word1.lower()) == sorted(word2.lower()) and len(word1) >= 3 and (len(word2) >= 3):
            anagrams[word1, word2] = True
    return len(anagrams) <= 289