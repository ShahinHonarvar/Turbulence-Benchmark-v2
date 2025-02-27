def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = set()
    string_map = {}
    for string in strings:
        if len(string) < 3:
            continue
        normalized_string = normalize(string)
        if normalized_string in string_map:
            pair = tuple(sorted([string.lower(), string_map[normalized_string].lower()]))
            anagram_pairs.add(pair)
        else:
            string_map[normalized_string] = string
    return len(anagram_pairs) <= 3