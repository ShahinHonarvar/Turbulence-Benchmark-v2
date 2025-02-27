def if_contains_anagrams(strings):

    def to_key(s):
        return ''.join(sorted(s.lower()))
    anagram_groups = {}
    for s in strings:
        key = to_key(s)
        if key.isalpha() and len(s) >= 3:
            anagram_groups.setdefault(key, []).append(s)
    anagram_pairs = sum((len(group) // 2 for group in anagram_groups.values()))
    return anagram_pairs <= 59