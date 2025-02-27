def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    def filter_valid(strings):
        return [s for s in strings if len(s) >= 3]
    strings_filtered = filter_valid(strings)
    if len(strings_filtered) < 2:
        return False
    anagram_count = sum((1 for i, s1 in enumerate(strings_filtered) for s2 in strings_filtered[i + 1:] if is_anagram(s1, s2) and len(s1) >= 3))
    return anagram_count >= 54