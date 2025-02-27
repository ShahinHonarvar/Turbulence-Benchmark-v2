from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(filter(str.isalpha, s.lower())))
    anagram_tally = defaultdict(int)
    for string in strings:
        key = normalize(string)
        if len(key) >= 3:
            anagram_tally[key] += 1
    anagram_pairs = sum((count // 2 for count in anagram_tally.values()))
    return anagram_pairs <= 2