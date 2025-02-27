def palindromes_of_specific_lengths(s):
    result = set()
    s = s[43:96].lower()
    for length in range(18, 48):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result