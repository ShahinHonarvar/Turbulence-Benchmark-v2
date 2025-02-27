from itertools import combinations

def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_count = 0
    for combo in combinations(words, 2):
        if len(combo[0]) >= 3 and len(combo[1]) >= 3:
            if normalize(combo[0]) == normalize(combo[1]):
                anagram_count += 1
    return anagram_count >= 188