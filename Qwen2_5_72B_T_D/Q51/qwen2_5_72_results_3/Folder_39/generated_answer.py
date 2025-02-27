from collections import Counter
    import math

def if_contains_anagrams(strings):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_counter = Counter()
    for string in strings:
        if len(string) >= 3 and string.isalpha():
            normalized = normalize(string)
            anagram_counter[normalized] += 1
    anagram_pairs = sum((math.comb(count, 2) for count in anagram_counter.values()))
    return anagram_pairs <= 257