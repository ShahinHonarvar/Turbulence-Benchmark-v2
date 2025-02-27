def palindromes_of_specific_lengths(s):
    s = s[103:277].lower()
    result = set()
    for length in range(100, 170):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result