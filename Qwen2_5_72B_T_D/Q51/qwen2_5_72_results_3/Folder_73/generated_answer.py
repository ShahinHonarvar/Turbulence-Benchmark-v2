from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = defaultdict(int)
    for s in strings:
        if len(s) >= 3 and s.isalpha():
            norm = normalize(s)
            anagram_counts[norm] += 1
    pairs_count = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return pairs_count <= 279