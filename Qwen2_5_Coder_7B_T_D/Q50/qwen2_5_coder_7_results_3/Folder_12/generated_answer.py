def if_contains_anagrams(str_list):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    str_list = [s.lower() for s in str_list if len(s) >= 3]
    anagram_count = 0
    for i in range(len(str_list)):
        for j in range(i + 1, len(str_list)):
            if is_anagram(str_list[i], str_list[j]):
                anagram_count += 1
    return anagram_count >= 69