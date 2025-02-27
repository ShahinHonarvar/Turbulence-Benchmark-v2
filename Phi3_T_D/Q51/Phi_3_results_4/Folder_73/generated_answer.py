from collections import Counter

def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        s1, s2 = (s1.lower(), s2.lower())
        return Counter(s1) == Counter(s2)
    count, length = (0, len(strings))
    for i in range(length):
        for j in range(i + 1, length):
            if is_anagram(strings[i], strings[j]) and len(strings[i]) >= 3 and (len(strings[j]) >= 3):
                count += 1
                if count > 279:
                    return False
    return True