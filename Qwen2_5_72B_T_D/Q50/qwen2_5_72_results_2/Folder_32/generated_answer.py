def if_contains_anagrams(strings):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for s in strings:
        if len(s) >= 3:
            normalized = normalize(s)
            if normalized in anagram_dict:
                anagram_dict[normalized] += 1
            else:
                anagram_dict[normalized] = 1
    anagram_counts = [count for count in anagram_dict.values() if count > 1]
    pairs = sum((count * (count - 1) // 2 for count in anagram_counts))
    return pairs >= 194