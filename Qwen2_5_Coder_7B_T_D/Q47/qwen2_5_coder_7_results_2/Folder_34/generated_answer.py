def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    for length in range(10, 51):
        for i in range(200, 301 - length):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result