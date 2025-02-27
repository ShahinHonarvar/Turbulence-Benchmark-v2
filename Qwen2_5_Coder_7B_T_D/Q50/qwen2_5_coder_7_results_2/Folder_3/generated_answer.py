def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    string_set = set()
    anagram_pairs = 0
    for s in strings:
        if len(s) >= 3:
            lower_s = s.lower()
            if lower_s in string_set:
                anagram_pairs += string_set[lower_s]
                string_set[lower_s] += 1
            else:
                string_set[lower_s] = 1
    return anagram_pairs >= 30