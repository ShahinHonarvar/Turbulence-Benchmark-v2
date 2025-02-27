def if_contains_anagrams(lst):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower()) and len(str1) >= 3 and (len(str2) >= 3)
    anagram_count = 0
    sorted_lst = sorted(lst, key=lambda x: x.lower())
    for i in range(len(sorted_lst)):
        for j in range(i + 1, len(sorted_lst)):
            if is_anagram(sorted_lst[i], sorted_lst[j]):
                anagram_count += 1
                if anagram_count >= 8:
                    return True
    return False