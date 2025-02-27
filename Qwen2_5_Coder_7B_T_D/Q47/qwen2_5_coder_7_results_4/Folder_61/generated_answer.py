def palindromes_of_specific_lengths(s):
    s = s[:31].lower()
    result = set()
    for length in range(20, 31):
        for start in range(0, 31 - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result