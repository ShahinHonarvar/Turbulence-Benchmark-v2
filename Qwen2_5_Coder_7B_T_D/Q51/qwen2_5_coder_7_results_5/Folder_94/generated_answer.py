from collections import Counter

def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return Counter(s1) == Counter(s2)
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i].lower(), lst[j].lower()) and len(lst[i]) >= 3:
                count += 1
                if count > 181:
                    return False
    return True