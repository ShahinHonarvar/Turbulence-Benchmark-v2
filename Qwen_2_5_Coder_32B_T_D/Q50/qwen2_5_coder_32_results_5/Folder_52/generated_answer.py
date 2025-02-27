from collections import Counter
    from itertools import combinations

def if_contains_anagrams(strings):
    anagram_count = 0
    valid_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    string_counts = Counter(valid_strings)
    for combo in combinations(string_counts.keys(), 2):
        if combo[0] == combo[1]:
            pairs = string_counts[combo[0]] * (string_counts[combo[0]] - 1) // 2
            anagram_count += pairs
        else:
            anagram_count += string_counts[combo[0]] * string_counts[combo[1]]
    return anagram_count >= 58