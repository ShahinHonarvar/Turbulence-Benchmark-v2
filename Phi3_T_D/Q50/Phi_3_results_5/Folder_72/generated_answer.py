from collections import defaultdict

def if_contains_anagrams(lst):
    freq = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            freq[key] += 1
    count = sum((v * (v - 1) // 2 for v in freq.values()))
    return count >= 55