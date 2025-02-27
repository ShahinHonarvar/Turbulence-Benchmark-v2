def palindromes_of_specific_lengths(s):
    palindromes = set()
    for i in range(124, 284):
        for j in range(150, 133, -1):
            if i + j <= 283:
                substring = s[i:i + j].lower()
                if substring.isalpha() and substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes