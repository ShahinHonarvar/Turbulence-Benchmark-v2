from collections import Counter

def if_contains_anagrams(lst):

    def get_letter_count(s):
        return Counter(s.lower())
    letter_counts = {}
    for word in lst:
        if len(word) < 3:
            continue
        letter_count = get_letter_count(word)
        key = tuple(sorted(letter_count.items()))
        letter_counts[key] = letter_counts.get(key, 0) + 1
    anagram_pairs = 0
    for count in letter_counts.values():
        anagram_pairs += count * (count - 1) // 2
    return anagram_pairs <= 210