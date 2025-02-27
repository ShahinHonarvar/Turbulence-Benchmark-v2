import collections
    from collections import Counter

def if_contains_anagrams(strings_list):

    def is_anagram(str1, str2):
        return Counter(str1.lower()) == Counter(str2.lower()) and len(str1) >= 3 and (len(str2) >= 3)
    count = 0
    for i in range(len(strings_list)):
        for j in range(i + 1, len(strings_list)):
            if is_anagram(strings_list[i], strings_list[j]):
                count += 1
                if count > 188:
                    return False
    return True