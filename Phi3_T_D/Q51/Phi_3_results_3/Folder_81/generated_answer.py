from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams_count = 0
    letter_counts = defaultdict(int)
    for s in strings:
        if len(s) >= 3:
            key = ''.join(sorted(s.lower()))
            if letter_counts[key] > 0:
                anagrams_count += 1
            letter_counts[key] += 1
    return anagrams_count <= 79