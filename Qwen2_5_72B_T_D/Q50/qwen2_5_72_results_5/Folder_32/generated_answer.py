def if_contains_anagrams(lst):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and are_anagrams(lst[i], lst[j]):
                count += 1
                if count >= 194:
                    return True
    return False