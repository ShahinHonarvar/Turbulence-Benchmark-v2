def if_contains_anagrams(lst):

    def count_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and count_anagrams(lst[i], lst[j]):
                count += 1
                if count >= 314:
                    return True
    return False