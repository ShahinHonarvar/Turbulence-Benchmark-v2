def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    count = 0
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and is_anagram(lst[i].lower(), lst[j].lower()):
                count += 1
                if count >= 95:
                    return True
    return False