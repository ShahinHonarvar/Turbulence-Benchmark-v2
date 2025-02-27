from collections import defaultdict

def if_contains_anagrams(strings_list):

    def string_to_sorted_tuple(s):
        return tuple(sorted((c for c in s.lower() if c.isalpha() and c.isascii())))
    counts = defaultdict(int)
    for s in strings_list:
        if len(s) >= 3:
            counts[string_to_sorted_tuple(s)] += 1
    anagram_pairs = sum((n * (n - 1) // 2 for n in counts.values() if n > 1))
    return anagram_pairs <= 26