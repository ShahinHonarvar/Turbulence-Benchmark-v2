from collections import Counter

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        normalized_s1 = ''.join(sorted(s1.lower()))
        normalized_s2 = ''.join(sorted(s2.lower()))
        return normalized_s1 == normalized_s2
    count = 0
    for i in range(len(lst)):
        if len(lst[i]) >= 3:
            for j in range(i + 1, len(lst)):
                if is_anagram(lst[i], lst[j]):
                    count += 1
                    if count > 35:
                        return False
    return True