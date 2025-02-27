def palindromes_of_specific_lengths(s):
    s = s.lower()
    result = set()
    for length in range(5, 11):
        for i in range(100, 201 - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result