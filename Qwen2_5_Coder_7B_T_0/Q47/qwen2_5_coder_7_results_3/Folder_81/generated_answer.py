def palindromes_of_specific_lengths(s):
    s = s[12:123].lower()
    result = set()
    for length in range(12, 221):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result