from collections import Counter

def if_contains_anagrams(strings):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    count = Counter((normalize(s) for s in strings if len(s) >= 3))
    anagram_pairs = sum((v * (v - 1) // 2 for v in count.values()))
    return anagram_pairs >= 21