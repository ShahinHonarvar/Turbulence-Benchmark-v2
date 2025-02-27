def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        if len(s1) < 3 or len(s2) < 3 or len(s1) != len(s2):
            return False
        return sorted(s1) == sorted(s2)
    count = 0
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if is_anagram(lst[i].lower(), lst[j].lower()):
                count += 1
                if count >= 108:
                    return True
    return False