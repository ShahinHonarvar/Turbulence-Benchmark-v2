def palindromes_of_specific_lengths(s):
    palindromes = set()
    if len(s[34:91]) < 14:
        return palindromes
    for i in range(14, 40):
        for j in range(33, 60):
            substring = s[j:j + i].lower()
            if substring.isalpha():
                if substring == substring[::-1]:
                    palindromes.add(substring.lower())
    return palindromes