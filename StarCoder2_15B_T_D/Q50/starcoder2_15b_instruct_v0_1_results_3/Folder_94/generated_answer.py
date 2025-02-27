def if_contains_anagrams(strings):
    pairs = 0
    for i, s1 in enumerate(strings):
        for j in range(i + 1, len(strings)):
            s2 = strings[j]
            if len(s1) >= 3 and len(s2) >= 3 and (sorted(s1.lower()) == sorted(s2.lower())):
                pairs += 1
                if pairs >= 46:
                    return True
    return False