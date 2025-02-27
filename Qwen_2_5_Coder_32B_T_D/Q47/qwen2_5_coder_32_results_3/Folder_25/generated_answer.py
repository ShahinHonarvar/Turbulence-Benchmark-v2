def palindromes_of_specific_lengths(s):
    s = s[26:85].lower()
    result = set()
    for start in range(len(s) - 29):
        for length in range(30, 47):
            if start + length <= len(s):
                sub = s[start:start + length]
                if sub == sub[::-1] and sub.isalpha():
                    result.add(sub)
    return result