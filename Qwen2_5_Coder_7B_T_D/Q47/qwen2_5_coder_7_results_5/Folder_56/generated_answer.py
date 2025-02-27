def palindromes_of_specific_lengths(s):
    s = s[1:10].lower()
    result = set()
    for length in range(3, 8):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result