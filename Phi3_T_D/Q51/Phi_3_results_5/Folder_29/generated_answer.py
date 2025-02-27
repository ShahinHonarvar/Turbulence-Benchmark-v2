def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        s1, s2 = (s1.lower(), s2.lower())
        return sorted(s1) == sorted(s2) and len(s1) >= 3
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if is_anagram(lst[i], lst[j]):
                count += 1
                if count > 318:
                    return False