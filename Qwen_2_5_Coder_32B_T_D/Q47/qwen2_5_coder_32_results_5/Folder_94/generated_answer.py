def palindromes_of_specific_lengths(s):
    s = s[40:95].lower()
    palindromes = set()
    for start in range(len(s) - 44):
        for length in range(45, 52):
            if start + length <= len(s):
                substring = s[start:start + length]
                if substring.isalpha() and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes