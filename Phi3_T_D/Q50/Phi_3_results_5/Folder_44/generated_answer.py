def if_contains_anagrams(strs):
    count = 0
    for i in range(len(strs)):
        for j in range(i + 1, len(strs)):
            if sorted(strs[i].lower()) == sorted(strs[j].lower()) and len(strs[i]) >= 3:
                count += 1
                if count >= 44:
                    return True
    return False