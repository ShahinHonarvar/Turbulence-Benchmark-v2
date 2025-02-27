def if_contains_anagrams(lst):

    def canonical_form(word):
        return ''.join(sorted(word.lower()))
    anagram_counts = {}
    for word in lst:
        if len(word) < 3:
            continue
        canonical = canonical_form(word)
        anagram_counts[canonical] = anagram_counts.get(canonical, 0) + 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs <= 59