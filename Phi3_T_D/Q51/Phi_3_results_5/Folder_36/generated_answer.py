import collections

def if_contains_anagrams(strings):
    count = 0
    sorted_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    counter = collections.Counter(sorted_strings)
    for key, value in counter.items():
        count += value * (value - 1) // 2
    return count <= 25