def palindromes_of_specific_lengths(s):
    s = s[23:83].lower()
    result = set()
    for i in range(len(s) - 31):
        for l in range(32, 35):
            if i + l <= len(s):
                sub = s[i:i + l]
                if sub.isalpha() and sub == sub[::-1]:
                    result.add(sub)
    return result