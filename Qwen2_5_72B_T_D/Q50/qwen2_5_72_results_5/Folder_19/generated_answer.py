def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    count = 0
    anagram_dict = {}
    for s in strings:
        if len(s) >= 3:
            normalized = normalize(s)
            if normalized in anagram_dict:
                anagram_dict[normalized] += 1
            else:
                anagram_dict[normalized] = 1
    for key, value in anagram_dict.items():
        count += value * (value - 1) // 2
    return count >= 84