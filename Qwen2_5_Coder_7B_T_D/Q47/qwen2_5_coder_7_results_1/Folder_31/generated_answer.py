def palindromes_of_specific_lengths(s):
    s = s[11:84].lower()
    result = set()
    for length in range(37, 61):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result