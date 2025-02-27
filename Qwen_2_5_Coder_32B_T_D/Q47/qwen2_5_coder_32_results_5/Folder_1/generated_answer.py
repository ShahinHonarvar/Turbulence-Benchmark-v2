def palindromes_of_specific_lengths(s):
    s = s[15:90].lower()
    result = set()
    for start in range(len(s) - 39):
        for end in range(start + 40, min(start + 73, len(s)) + 1):
            substring = s[start:end]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result