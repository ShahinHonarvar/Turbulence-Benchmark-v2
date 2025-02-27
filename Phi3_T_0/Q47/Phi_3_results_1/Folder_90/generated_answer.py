def palindromes_of_specific_lengths(s):
    start, end = (106, 280)
    palindromes = set()
    for length in range(136, 152):
        for i in range(start, end - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes