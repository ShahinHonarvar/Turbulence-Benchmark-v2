from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            str1 = sorted(lst[i].lower())
            str2 = sorted(lst[j].lower())
            if str1 == str2 and len(lst[i]) >= 3 and (len(lst[j]) >= 3):
                count += 1
                if count > 70:
                    return False
    return True