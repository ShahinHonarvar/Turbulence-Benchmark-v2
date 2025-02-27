def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for item in lst:
        if len(item) >= 3:
            normalized = normalize(item)
            if normalized in anagram_dict:
                anagram_dict[normalized] += 1
            else:
                anagram_dict[normalized] = 1
    anagram_count = sum((1 for count in anagram_dict.values() if count >= 2))
    return anagram_count >= 2