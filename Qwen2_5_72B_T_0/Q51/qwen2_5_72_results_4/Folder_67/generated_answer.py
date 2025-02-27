def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = set()
    string_dict = {}
    for s in strings:
        if len(s) >= 3 and s.isalpha():
            norm = normalize(s)
            if norm in string_dict:
                anagram_pairs.add(tuple(sorted((s.lower(), string_dict[norm].lower()))))
            string_dict[norm] = s
    return len(anagram_pairs) <= 5