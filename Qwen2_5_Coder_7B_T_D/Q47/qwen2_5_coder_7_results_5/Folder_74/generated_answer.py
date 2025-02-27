def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    s = ''.join(filter(str.isalpha, s[30:85]))
    for length in range(12, 21):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result