from collections import Counter

def if_contains_anagrams(lst):

    def is_anagram(str1, str2):
        return Counter(str1) == Counter(str2)
    count = 0
    lst = [word.lower() for word in lst if len(word) >= 3]
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                count += 1
    return count >= 48