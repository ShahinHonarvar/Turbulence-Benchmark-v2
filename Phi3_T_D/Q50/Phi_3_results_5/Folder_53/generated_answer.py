from itertools import combinations

def if_contains_anagrams(word_list):

    def is_anagram(w1, w2):
        return len(w1) >= 3 and sorted(w1.lower()) == sorted(w2.lower())
    anagram_pairs = [(w1, w2) for w1, w2 in combinations(word_list, 2) if is_anagram(w1, w2)]
    return len(anagram_pairs) >= 11