def palindromes_of_specific_lengths(s):
    substr = s[36:93].lower()
    result = set()
    for length in range(10, 36):
        for i in range(len(substr) - length + 1):
            substring = substr[i:i + length]
            if substring == substring[::-1] and substring.isalpha():
                result.add(substring)
    return result