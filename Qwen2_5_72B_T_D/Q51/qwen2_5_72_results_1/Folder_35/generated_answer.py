from collections import Counter

def if_contains_anagrams(lst):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_pairs = 0
    anagram_count = {}
    for item in lst:
        if len(item) >= 3 and item.isalpha():
            normalized = normalize(item)
            if normalized in anagram_count:
                anagram_pairs += anagram_count[normalized]
                anagram_count[normalized] += 1
            else:
                anagram_count[normalized] = 1
    return anagram_pairs <= 210