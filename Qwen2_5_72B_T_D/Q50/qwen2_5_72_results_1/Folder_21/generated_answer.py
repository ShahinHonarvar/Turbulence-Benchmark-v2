def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for string in strings:
        if len(string) >= 3:
            key = normalize(string)
            if key in anagram_dict:
                anagram_dict[key] += 1
            else:
                anagram_dict[key] = 1
    anagram_pairs = 0
    for count in anagram_dict.values():
        anagram_pairs += count * (count - 1) // 2
    return anagram_pairs >= 136