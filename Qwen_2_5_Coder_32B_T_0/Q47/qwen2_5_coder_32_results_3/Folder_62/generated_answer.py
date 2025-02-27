def palindromes_of_specific_lengths(s):
    s = s[26:88].lower()
    result = set()
    for i in range(len(s) - 51):
        for l in range(52, 57):
            if i + l <= len(s):
                sub = s[i:i + l]
                if sub.isalpha() and sub == sub[::-1]:
                    result.add(sub)
    return result