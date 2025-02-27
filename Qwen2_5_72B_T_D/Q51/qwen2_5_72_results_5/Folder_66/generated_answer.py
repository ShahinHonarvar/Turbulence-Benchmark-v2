from collections import Counter

def if_contains_anagrams(lst):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_pairs = 0
    count_by_sorted = {}
    for item in lst:
        if len(item) >= 3 and all((c.isalpha() for c in item)):
            normalized = normalize(item)
            if normalized in count_by_sorted:
                anagram_pairs += count_by_sorted[normalized]
                count_by_sorted[normalized] += 1
            else:
                count_by_sorted[normalized] = 1
    return anagram_pairs <= 64