def palindromes_of_specific_lengths(s):
    result = set()
    s = s[11:88]
    s = s.lower()
    for length in range(4, 6):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result