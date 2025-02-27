def palindromes_of_specific_lengths(s):
    s = s[36:93].lower()
    result = set()
    for start in range(len(s) - 9):
        for end in range(start + 10, min(start + 36, len(s)) + 1):
            substring = s[start:end]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result