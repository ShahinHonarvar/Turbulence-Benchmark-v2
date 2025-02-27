def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1) == sorted(s2)
    count = 0
    lst = [s.lower() for s in lst if len(s) >= 3]
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if is_anagram(lst[i], lst[j]):
                count += 1
                if count >= 91:
                    return True
    return False