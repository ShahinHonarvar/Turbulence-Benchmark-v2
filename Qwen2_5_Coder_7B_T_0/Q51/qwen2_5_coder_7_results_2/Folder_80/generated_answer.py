from collections import Counter

def if_contains_anagrams(lst):
    anagram_count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (Counter(lst[i].lower()) == Counter(lst[j].lower())):
                anagram_count += 1
                if anagram_count > 255:
                    return False
    return True