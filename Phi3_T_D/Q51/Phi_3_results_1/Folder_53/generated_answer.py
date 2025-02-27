import itertools
from collections import defaultdict

def if_contains_anagrams(strings):
    seen = defaultdict(int)
    for i, word in enumerate(strings):
        word = word.lower()
        for j in range(i + 1, len(strings)):
            other = strings[j].lower()
            if sorted(word) == sorted(other) and len(word) >= 3:
                seen[min(word, other), max(word, other)] += 1
                if seen[min(word, other), max(word, other)] > 8:
                    return False
    return True