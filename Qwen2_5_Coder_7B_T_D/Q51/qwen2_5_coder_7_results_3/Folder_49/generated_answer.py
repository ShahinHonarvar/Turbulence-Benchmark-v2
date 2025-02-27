def if_contains_anagrams(lst):
    lst = [word.lower() for word in lst if len(word) >= 3]
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if sorted(lst[i]) == sorted(lst[j]):
                count += 1
                if count > 10:
                    return False
    return True