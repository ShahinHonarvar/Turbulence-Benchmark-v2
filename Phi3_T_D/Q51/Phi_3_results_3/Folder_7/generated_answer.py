from collections import defaultdict

def if_contains_anagrams(strings):
    filtered_strings = [s.lower() for s in strings if len(s) >= 3]
    anagrams_count = defaultdict(int)
    for s in filtered_strings:
        sorted_string = ''.join(sorted(s))
        anagrams_count[sorted_string] += 1
    pairs = sum((v * (v - 1) // 2 for v in anagrams_count.values()))
    return pairs <= 445