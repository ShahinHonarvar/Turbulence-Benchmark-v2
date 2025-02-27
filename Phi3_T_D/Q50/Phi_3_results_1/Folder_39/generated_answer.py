def if_contains_anagrams(strings):
    anagram_list = {}
    count = 0
    for s in strings:
        sorted_s = ''.join(sorted(s.lower()))
        if sorted_s in anagram_list:
            count += anagram_list[sorted_s]
            anagram_list[sorted_s] += 1
        elif len(s) >= 3:
            anagram_list[sorted_s] = 1
    return count >= 54