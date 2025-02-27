def palindromes_of_specific_lengths(s):
    s = s[15:73].lower()
    result = set()
    for length in range(19, 56):
        for start in range(len(s) - length + 1):
            substring = s[start:start + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result