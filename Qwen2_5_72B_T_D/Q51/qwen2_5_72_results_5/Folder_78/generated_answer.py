from collections import Counter

def if_contains_anagrams(lst):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_pairs = 0
    anagram_map = {}
    for word in lst:
        if len(word) >= 3 and word.isalpha():
            normalized = normalize(word)
            if normalized in anagram_map:
                anagram_pairs += len(anagram_map[normalized])
                anagram_map[normalized].append(word)
            else:
                anagram_map[normalized] = [word]
    return anagram_pairs <= 70