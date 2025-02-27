def if_contains_anagrams(lst):

    def normalize(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for word in lst:
        if len(word) >= 3:
            key = normalize(word)
            if key in anagram_dict:
                anagram_dict[key].append(word)
            else:
                anagram_dict[key] = [word]
    anagram_pairs = 0
    for key in anagram_dict:
        count = len(anagram_dict[key])
        anagram_pairs += count * (count - 1) // 2
        if anagram_pairs > 52:
            return False
    return True