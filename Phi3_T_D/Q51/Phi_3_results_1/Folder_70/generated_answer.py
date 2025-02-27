import re

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(re.sub('\\W+', '', s1.lower())) == sorted(re.sub('\\W+', '', s2.lower())) and len(s1) >= 3
    count = 0
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if is_anagram(lst[i], lst[j]):
                count += 1
                if count > 97:
                    return False
    return True