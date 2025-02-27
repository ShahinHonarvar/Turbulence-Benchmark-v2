def palindromes_of_specific_lengths(s):
    s = s[:31].lower()
    results = set()
    for length in range(20, 31):
        for i in range(31 - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                results.add(substring)
    return results