def palindromes_of_specific_lengths(s):
    s = s[11:97].lower()
    result = set()
    for length in range(45, 53):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result