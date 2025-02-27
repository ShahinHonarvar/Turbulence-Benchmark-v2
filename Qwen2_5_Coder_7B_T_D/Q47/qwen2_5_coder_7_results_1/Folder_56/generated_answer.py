def palindromes_of_specific_lengths(s):
    s = s[1:10].lower()
    result = set()
    for length in range(3, 8):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result