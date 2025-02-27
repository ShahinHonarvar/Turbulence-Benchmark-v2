from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    seen = set()
    for s1 in strings:
        s1_sorted = ''.join(sorted(s1.lower()))
        if s1_sorted in seen:
            count += 1
            if count > 48:
                return False
        else:
            seen.add(s1_sorted)
        for s2 in seen:
            if len(s1) >= 3 and len(s2) >= 3 and is_anagram(s1_sorted, s2):
                count += 1
                if count > 48:
                    return False
    return True

def is_anagram(s1_sorted, s2):
    return Counter(s1_sorted) == Counter(s2) and s1_sorted != s2