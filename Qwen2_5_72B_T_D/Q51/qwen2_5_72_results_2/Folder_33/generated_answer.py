from collections import Counter

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = Counter()
    for s in strings:
        if len(s) >= 3 and s.isalpha():
            normalized = normalize(s)
            anagram_count[normalized] += 1
    pairs = sum((count * (count - 1) // 2 for count in anagram_count.values()))
    return pairs <= 85