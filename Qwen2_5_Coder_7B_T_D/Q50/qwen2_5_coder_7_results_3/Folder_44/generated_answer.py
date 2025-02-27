def if_contains_anagrams(strs):
    count = 0
    for i in range(len(strs)):
        for j in range(i + 1, len(strs)):
            str1 = sorted(strs[i].lower())
            str2 = sorted(strs[j].lower())
            if len(str1) >= 3 and len(str2) >= 3 and (str1 == str2):
                count += 1
    return count >= 44