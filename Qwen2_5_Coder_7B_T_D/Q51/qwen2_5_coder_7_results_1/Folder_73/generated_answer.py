from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(list)
    for s in lst:
        if len(s) >= 3:
            count = [0] * 26
            for char in s.lower():
                count[ord(char) - ord('a')] += 1
            sorted_count = tuple(count)
            anagrams[sorted_count].append(s)
    pairs = sum((len(v) * (len(v) - 1) // 2 for v in anagrams.values() if len(v) > 1))
    return pairs <= 279