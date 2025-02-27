def palindromes_of_specific_lengths(s):
    result = set()
    s = s[:7].lower()
    for length in range(3, 7):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result