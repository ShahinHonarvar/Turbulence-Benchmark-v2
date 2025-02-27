def palindromes_of_specific_lengths(s):
    s = s[26:85].lower()
    result = set()
    for length in range(30, 47):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result