def are_anagrams(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    return sorted(s1) == sorted(s2)

def if_contains_anagrams(strings):
    pairs = 0
    for i, s1 in enumerate(strings):
        for s2 in strings[i + 1:]:
            if are_anagrams(s1, s2):
                pairs += 1
                if pairs > 34:
                    return False
    return True