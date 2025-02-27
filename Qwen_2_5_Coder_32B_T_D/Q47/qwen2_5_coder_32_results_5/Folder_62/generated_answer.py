def palindromes_of_specific_lengths(s):
    result = set()
    s = s[26:88].lower()
    for i in range(len(s) - 51):
        for j in range(52, 57):
            if i + j <= len(s):
                sub = s[i:i + j]
                if sub.isalpha() and sub == sub[::-1]:
                    result.add(sub)
    return result