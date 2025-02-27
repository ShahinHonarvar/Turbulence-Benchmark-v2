def if_contains_anagrams(string_list):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    length_count = {}
    for s in string_list:
        key = normalize(s)
        if len(s) >= 3:
            length_count[key] = length_count.get(key, 0) + 1
    anagram_pairs = sum((v * (v - 1) // 2 for v in length_count.values()))
    return anagram_pairs >= 67