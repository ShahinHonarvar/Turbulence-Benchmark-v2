from collections import Counter

def if_contains_anagrams(strs):

    def is_anagram(s1, s2):
        return Counter(s1.lower()) == Counter(s2.lower())
    count = 0
    for i in range(len(strs)):
        for j in range(i + 1, len(strs)):
            if len(strs[i]) >= 3 and len(strs[j]) >= 3 and is_anagram(strs[i], strs[j]):
                count += 1
                if count > 407:
                    return False
    return True