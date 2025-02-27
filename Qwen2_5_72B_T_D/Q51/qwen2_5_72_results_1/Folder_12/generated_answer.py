def if_contains_anagrams(strings):

    def canonical_form(s):
        return ''.join(sorted(s.lower()))
    anagram_counts = {}
    for string in strings:
        if len(string) >= 3 and string.isalpha():
            canonical = canonical_form(string)
            anagram_counts[canonical] = anagram_counts.get(canonical, 0) + 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_counts.values()))
    return anagram_pairs <= 92