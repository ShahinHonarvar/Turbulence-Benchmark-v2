def palindromes_of_specific_lengths(s):
    s = s[100:296].lower()
    result = set()
    for start in range(len(s) - 135):
        for end in range(start + 135, min(start + 161, len(s))):
            substring = s[start:end + 1]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result