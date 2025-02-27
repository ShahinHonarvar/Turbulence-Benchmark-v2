def if_contains_anagrams(lst):

    def count_chars(s):
        return sorted([c.lower() for c in s if c.isalpha()])
    count_anagrams = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3:
                if count_chars(lst[i]) == count_chars(lst[j]):
                    count_anagrams += 1
                    if count_anagrams > 25:
                        return False
    return True