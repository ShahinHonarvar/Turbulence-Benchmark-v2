from collections import Counter

def if_contains_anagrams(list_of_strings):
    anagrams = []
    for i, s1 in enumerate(list_of_strings):
        for j in range(i + 1, len(list_of_strings)):
            s2 = list_of_strings[j]
            if len(s1) >= 3 and len(s2) >= 3 and (Counter(s1.lower()) == Counter(s2.lower())):
                anagrams.append((s1, s2))
    return len(anagrams) >= 89