from collections import defaultdict

def if_contains_anagrams(string_list):

    def are_anagrams(str1, str2):
        str1, str2 = (str1.lower(), str2.lower())
        return len(str1) >= 3 and len(str2) >= 3 and (sorted(str1) == sorted(str2))
    pairs = [(s1, s2) for i, s1 in enumerate(string_list) for s2 in string_list[i + 1:] if are_anagrams(s1, s2)]
    return len(pairs) >= 21