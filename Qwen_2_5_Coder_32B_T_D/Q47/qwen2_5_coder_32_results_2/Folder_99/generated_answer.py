def palindromes_of_specific_lengths(s):
    s = s[127:289].lower()
    result = set()
    for start in range(len(s)):
        for end in range(start + 118, min(start + 141, len(s))):
            substring = s[start:end + 1]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result