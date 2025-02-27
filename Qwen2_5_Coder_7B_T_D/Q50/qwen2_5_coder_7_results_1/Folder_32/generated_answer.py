from collections import Counter

def if_contains_anagrams(lst):

    def clean(s):
        return ''.join(sorted(s.lower()))
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (clean(lst[i]) == clean(lst[j])):
                count += 1
    return count >= 194