def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for item in lst:
        if len(item) >= 3 and item.isalpha():
            norm = normalize(item)
            anagram_dict[norm] = anagram_dict.get(norm, 0) + 1
    anagram_pairs = sum((count * (count - 1) // 2 for count in anagram_dict.values()))
    return anagram_pairs <= 40