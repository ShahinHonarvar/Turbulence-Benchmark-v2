from itertools import combinations

def are_anagrams(str1, str2):
    return sorted(str1.lower().replace(' ', '')) == sorted(str2.lower().replace(' ', ''))

def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if are_anagrams(lst[i], lst[j]) and len(lst[i]) >= 3 and (len(lst[j]) >= 3):
                count += 1
                if count > 44:
                    return False
    return True