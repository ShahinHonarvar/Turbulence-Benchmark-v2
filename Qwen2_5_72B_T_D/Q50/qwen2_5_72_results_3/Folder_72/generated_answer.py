from collections import Counter

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    counts = Counter()
    for string in strings:
        if len(string) >= 3:
            counts[normalize(string)] += 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in counts.values()))
    return anagram_pairs >= 55