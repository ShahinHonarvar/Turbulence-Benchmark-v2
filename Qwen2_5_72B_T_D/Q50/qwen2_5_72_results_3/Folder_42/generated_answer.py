def if_contains_anagrams(lst):

    def is_anagram(str1, str2):
        return sorted(str1) == sorted(str2)
    count = 0
    lst = [s.lower() for s in lst if len(s) >= 3]
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                count += 1
                if count >= 233:
                    return True
    return False