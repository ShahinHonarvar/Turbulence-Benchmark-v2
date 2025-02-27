def palindromes_of_specific_lengths(s):
    s = s[10:71].lower()
    result = set()
    for i in range(len(s)):
        for j in range(i + 2, min(i + 53, len(s) + 1)):
            substring = s[i:j]
            if substring == substring[::-1] and substring.isalpha() and (24 <= len(substring) <= 52):
                result.add(substring)
    return result