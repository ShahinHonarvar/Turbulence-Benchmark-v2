def palindromes_of_specific_lengths(s):
    s = s[10:71].lower()
    result = set()
    for i in range(len(s) - 23):
        for j in range(24, 53):
            if i + j <= len(s):
                sub = s[i:i + j]
                if sub.isalpha() and sub == sub[::-1]:
                    result.add(sub)
    return result