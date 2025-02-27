from collections import Counter

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return len(s1) >= 3 and len(s2) >= 3 and (Counter(s1.lower()) == Counter(s2.lower()))
    count = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if is_anagram(strings[i], strings[j]):
                count += 1
                if count > 65:
                    return False
    return True