from collections import Counter

def if_contains_anagrams(lst):
    anagrams_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (Counter(lst[i].lower()) == Counter(lst[j].lower())):
                anagrams_count += 1
                if anagrams_count > 14:
                    return False
    return True