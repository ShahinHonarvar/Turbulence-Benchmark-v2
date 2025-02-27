from collections import defaultdict

def if_contains_anagrams(lst):

    def generate_signature(s):
        return ''.join(sorted(s.lower()))
    anagram_count = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            anagram_count[generate_signature(word)] += 1
    pairs = sum((count // 2 for count in anagram_count.values()))
    return pairs >= 78