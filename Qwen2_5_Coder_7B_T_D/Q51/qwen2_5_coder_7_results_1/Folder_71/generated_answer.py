from collections import Counter

def if_contains_anagrams(strings):
    anagrams = []
    for s in strings:
        if len(s) >= 3:
            sorted_s = ''.join(sorted(s.lower()))
            anagrams.append(sorted_s)
    counter = Counter(anagrams)
    return sum((v > 1 for v in counter.values())) <= 9