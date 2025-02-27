from collections import defaultdict

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return sorted(str1.lower()) == sorted(str2.lower()) and len(str1) >= 3 and (len(str2) >= 3)
    count = 0
    for i, string1 in enumerate(strings):
        for string2 in strings[i + 1:]:
            if is_anagram(string1, string2):
                count += 1
    return count >= 153