def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    for length in range(3, 8):
        for i in range(1, 11 - length):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result