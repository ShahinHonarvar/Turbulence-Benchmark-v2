from collections import Counter

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = 0
    counter = Counter()
    for string in strings:
        if len(string) >= 3:
            normalized = normalize(string)
            if normalized:
                anagram_pairs += counter[normalized]
                counter[normalized] += 1
    return anagram_pairs <= 35