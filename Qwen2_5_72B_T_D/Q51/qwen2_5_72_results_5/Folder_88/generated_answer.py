from collections import defaultdict

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3]
    count = defaultdict(int)
    for s in strings:
        count[''.join(sorted(s))] += 1
    anagram_pairs = sum((n * (n - 1) // 2 for n in count.values()))
    return anagram_pairs <= 407