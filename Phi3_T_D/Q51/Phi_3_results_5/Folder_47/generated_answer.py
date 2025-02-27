def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_count = 0
    len_lst = len(lst)
    for i in range(len_lst):
        for j in range(i + 1, len_lst):
            if_anagram_flag = is_anagram(lst[i], lst[j]) and len(lst[i]) >= 3
            if if_anagram_flag:
                anagram_count += 1
                if anagram_count > 366:
                    return False
    return True