def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings if len(s) >= 3 and s.isalpha()]
    anagram_count = 0
    anagram_dict = {}
    for s in strings:
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagram_dict:
            anagram_dict[sorted_s] += 1
            anagram_count += 1
        else:
            anagram_dict[sorted_s] = 1
    return anagram_count <= 255