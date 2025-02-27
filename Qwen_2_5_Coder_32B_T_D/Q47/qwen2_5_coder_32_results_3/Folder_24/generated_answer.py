def palindromes_of_specific_lengths(s):
    s = s[12:93].lower()
    result = set()
    for start in range(len(s) - 41):
        for end in range(start + 41, min(start + 78, len(s) + 1)):
            substring = s[start:end]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result