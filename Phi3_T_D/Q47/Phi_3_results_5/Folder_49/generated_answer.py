def palindromes_of_specific_lengths(s):
    s = s[9:101]
    s = ''.join([char.lower() for char in s if char.isalpha()])
    palindromes = set()
    for length in range(10, 51):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes