def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    normalized_strings = {}
    for s in strings:
        if len(s) >= 3:
            norm = normalize(s)
            if norm in normalized_strings:
                anagram_count += normalized_strings[norm]
                normalized_strings[norm] += 1
            else:
                normalized_strings[norm] = 1
    return anagram_count <= 73