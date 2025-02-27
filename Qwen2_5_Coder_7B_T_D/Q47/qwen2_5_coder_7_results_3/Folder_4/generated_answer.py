def palindromes_of_specific_lengths(s):
    s = s[12:93].lower()
    result = set()
    for i in range(len(s) - 16):
        substring = s[i:i + 67]
        if substring == substring[::-1] and substring.isalpha() and (17 <= len(substring) <= 66):
            result.add(substring)
    return result