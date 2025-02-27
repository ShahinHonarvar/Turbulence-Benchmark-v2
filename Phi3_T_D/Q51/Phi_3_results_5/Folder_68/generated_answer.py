def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = sum((is_anagram(s1, s2) for i, s1 in enumerate(string_list) for s2 in string_list[i + 1:] if len(s1) >= 3 and len(s2) >= 3))
    return count <= 94