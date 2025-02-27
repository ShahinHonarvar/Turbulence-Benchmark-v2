def palindromes_of_specific_lengths(s):
    s = s[24:85].lower()
    result = set()
    for i in range(21, 32):
        for j in range(24, len(s) - i + 1):
            substr = s[j:j + i]
            if substr.isalpha() and substr == substr[::-1]:
                result.add(substr)
    return result