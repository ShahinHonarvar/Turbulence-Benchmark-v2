from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(int)
    for word in strings:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            anagrams[key] += 1
    count_pairs = sum((n * (n - 1) // 2 for n in anagrams.values()))
    return count_pairs <= 366