from collections import Counter

def if_contains_anagrams(lst):
    lst = [s.lower() for s in lst]
    anagrams = [Counter(s) for s in lst if len(s) >= 3]
    pairs = 0
    for i in range(len(anagrams)):
        for j in range(i + 1, len(anagrams)):
            if anagrams[i] == anagrams[j]:
                pairs += 1
    return pairs >= 22