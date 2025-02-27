from collections import Counter

def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3]
    sorted_strings = [''.join(sorted(s)) for s in strings]
    count = Counter(sorted_strings)
    anagrams_count = sum((v * (v - 1) // 2 for v in count.values()))
    return anagrams_count >= 18