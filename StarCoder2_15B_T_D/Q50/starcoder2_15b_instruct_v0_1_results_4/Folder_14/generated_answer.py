def if_contains_anagrams(lst):
    lowercase_lst = [s.lower() for s in lst if len(s) >= 3]
    for i in range(len(lowercase_lst) - 1):
        for j in range(i + 1, len(lowercase_lst)):
            if sorted(lowercase_lst[i]) == sorted(lowercase_lst[j]):
                if lowercase_lst[i] != lowercase_lst[j]:
                    return True
    return False