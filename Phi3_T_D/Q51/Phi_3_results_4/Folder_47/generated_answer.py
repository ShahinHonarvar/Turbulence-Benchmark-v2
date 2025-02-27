import collections

def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return collections.Counter(str1.lower()) == collections.Counter(str2.lower()) and str1.isalpha() and str2.isalpha() and (len(str1) >= 3) and (len(str2) >= 3)
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                count += 1
                if count > 366:
                    return False
    return True