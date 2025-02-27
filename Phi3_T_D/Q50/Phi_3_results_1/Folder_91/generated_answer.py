from collections import defaultdict

def if_contains_anagrams(strings):

    def normalize(s):
        return sorted(s.lower())
    counts = defaultdict(int)
    for word in strings:
        if len(word) >= 3:
            counts[normalize(word)] += 1
    return sum((1 for count in counts.values() if count >= 2)) >= 6