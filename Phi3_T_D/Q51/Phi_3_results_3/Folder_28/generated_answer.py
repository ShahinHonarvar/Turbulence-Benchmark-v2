from collections import Counter

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        if len(s1) < 3 or len(s2) < 3:
            return False
        return Counter(s1.lower()) == Counter(s2.lower())
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                count += 1
                if count > 78:
                    return False
    return True