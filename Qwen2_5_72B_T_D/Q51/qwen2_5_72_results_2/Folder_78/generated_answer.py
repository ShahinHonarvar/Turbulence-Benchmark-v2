def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_pairs = set()
    string_dict = {}
    for s in strings:
        if len(s) >= 3 and s.isalpha():
            normalized = normalize(s)
            if normalized in string_dict:
                for prev in string_dict[normalized]:
                    anagram_pairs.add((min(prev, s), max(prev, s)))
                string_dict[normalized].append(s)
            else:
                string_dict[normalized] = [s]
    return len(anagram_pairs) <= 70