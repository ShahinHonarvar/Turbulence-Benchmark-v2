from collections import Counter

def if_contains_anagrams(strings):
    sorted_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    count = Counter(sorted_strings)
    return sum((n * (n - 1) // 2 for n in count.values())) <= 131