def palindromes_of_specific_lengths(s):
    result = set()
    s = s.lower()
    for length in range(3, 8):
        for i in range(10, 56):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result