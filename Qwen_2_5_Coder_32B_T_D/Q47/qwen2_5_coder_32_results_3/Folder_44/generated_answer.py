def palindromes_of_specific_lengths(s):
    result = set()
    s = s[18:99]
    s = s.lower()
    for i in range(len(s) - 31 + 1):
        for j in range(31, 52):
            if i + j > len(s):
                break
            sub = s[i:i + j]
            if sub.isalpha() and sub == sub[::-1]:
                result.add(sub)
    return result