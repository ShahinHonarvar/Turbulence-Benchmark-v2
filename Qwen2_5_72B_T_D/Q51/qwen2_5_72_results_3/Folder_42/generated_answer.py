from collections import Counter

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = Counter()
    for string in strings:
        if len(string) >= 3 and string.isalpha():
            anagram_counts[normalize(string)] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs <= 38