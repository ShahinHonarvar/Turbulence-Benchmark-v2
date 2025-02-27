def palindromes_of_specific_lengths(s):
    s = s[13:96].lower()
    result = set()
    for i in range(len(s) - 56):
        for l in range(57, 61):
            if i + l <= len(s):
                sub = s[i:i + l]
                if sub.isalpha() and sub == sub[::-1]:
                    result.add(sub)
    return result