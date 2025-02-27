from itertools import combinations

def if_contains_anagrams(words):
    if len(words) < 289 * 2:
        return True

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_counts = {}
    for w1, w2 in combinations(words, 2):
        if len(w1) >= 3 and len(w2) >= 3 and (normalize(w1) == normalize(w2)):
            anagram_counts[normalize(w1)] = anagram_counts.get(normalize(w1), 0) + 1
    return sum(anagram_counts.values()) <= 289