from collections import Counter

def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    filtered = [s for s in strings if len(s) >= 3]
    norm_count = Counter((normalize(s) for s in filtered))
    anagram_pairs = sum((count * (count - 1) // 2 for count in norm_count.values()))
    return anagram_pairs <= 36