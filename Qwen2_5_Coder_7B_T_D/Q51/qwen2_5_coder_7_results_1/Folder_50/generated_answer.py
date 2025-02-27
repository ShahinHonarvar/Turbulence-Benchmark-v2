def if_contains_anagrams(lst):
    n = len(lst)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            s1 = sorted(lst[i].lower())
            s2 = sorted(lst[j].lower())
            if len(s1) >= 3 and s1 == s2:
                count += 1
                if count > 47:
                    return False
    return True