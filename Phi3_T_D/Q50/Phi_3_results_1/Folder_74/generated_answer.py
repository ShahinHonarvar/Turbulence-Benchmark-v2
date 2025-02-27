from collections import Counter

def if_contains_anagrams(strings):

    def count_letters(s):
        return Counter(s.lower())
    letter_counts = [count_letters(s) for s in strings if len(s) >= 3]
    seen_counts = {}
    anagram_count = 0
    for c in letter_counts:
        key = frozenset(c.items())
        if key in seen_counts:
            anagram_count += 1
        seen_counts[key] = True
    return anagram_count >= 17