def palindromes_of_specific_lengths(s):
    s = s[27:96].lower()
    result = set()
    for i in range(len(s) - 48):
        for length in range(49, 52):
            if i + length <= len(s):
                sub = s[i:i + length]
                if sub.isalpha() and sub == sub[::-1]:
                    result.add(sub)
    return result