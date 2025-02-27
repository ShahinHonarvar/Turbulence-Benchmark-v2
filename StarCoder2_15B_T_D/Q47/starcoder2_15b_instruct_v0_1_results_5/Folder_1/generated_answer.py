def palindromes_of_specific_lengths(s):
    palindromes = set()
    for length in range(40, 73):
        for i in range(15, 90 - length + 1):
            substring = s[i:i + length]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes