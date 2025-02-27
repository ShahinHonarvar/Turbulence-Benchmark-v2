def palindromes_of_specific_lengths(s):
    s = s[12:93].lower()
    result = set()
    for start in range(len(s)):
        for end in range(start + 17, min(start + 67, len(s)) + 1):
            substring = s[start:end]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result