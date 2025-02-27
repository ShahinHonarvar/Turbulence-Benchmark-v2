def palindromes_of_specific_lengths(s):
    s = s[100:201].lower()
    result = set()
    for length in range(5, 11):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                result.add(substring)
    return result