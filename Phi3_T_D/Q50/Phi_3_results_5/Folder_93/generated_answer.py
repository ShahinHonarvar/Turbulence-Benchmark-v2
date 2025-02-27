from collections import defaultdict

def if_contains_anagrams(lst):
    sorted_by_length = [''.join(sorted(s)) for s in lst if len(s) >= 3]
    freq = defaultdict(int)
    for s in sorted_by_length:
        freq[s] += 1
    count = sum((v * (v - 1) // 2 for v in freq.values()))
    return count >= 18