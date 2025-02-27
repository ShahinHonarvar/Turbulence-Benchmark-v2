def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(24, 85):
        for j in range(i + 21, min(i + 32, len(s))):
            substring = s[i:j]
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes