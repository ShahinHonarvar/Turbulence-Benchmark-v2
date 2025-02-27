def palindromes_of_specific_lengths(s):
    result = set()
    s = s[:51].lower()
    for length in range(50, 101):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result