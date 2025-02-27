def if_contains_anagrams(lst):

    def sort_lower(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for s in lst:
        if len(s) >= 3:
            sorted_str = sort_lower(s)
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str] += 1
            else:
                anagram_dict[sorted_str] = 1
    anagram_count = sum((1 for count in anagram_dict.values() if count > 1))
    return anagram_count >= 246