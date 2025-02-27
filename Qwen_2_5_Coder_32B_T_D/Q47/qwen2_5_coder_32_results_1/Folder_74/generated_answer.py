def palindromes_of_specific_lengths(s):
    s = s[30:85].lower()
    result = set()
    for start in range(len(s) - 11):
        for end in range(start + 11, min(start + 21, len(s) + 1)):
            sub = s[start:end]
            if sub.isalpha() and sub == sub[::-1]:
                result.add(sub)
    return result