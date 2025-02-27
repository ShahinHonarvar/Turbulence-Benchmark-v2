def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return len(s1) == len(s2) and sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if is_anagram(lst[i], lst[j]):
                count += 1
                if count >= 123:
                    return True
    return False