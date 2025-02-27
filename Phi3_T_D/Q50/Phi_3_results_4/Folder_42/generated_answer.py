def if_contains_anagrams(string_list):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower())
    counts = {}
    for s in string_list:
        sorted_str = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            counts[sorted_str] = counts.get(sorted_str, 0) + 1
    anagram_pairs = sum((n * (n - 1) // 2 for n in counts.values()))
    return anagram_pairs >= 233