def palindromes_of_specific_lengths(s):
    sub = s[101:293]
    palindromes = set()
    for i in range(154, 183):
        for j in range(101, 293 - i + 1):
            substring = sub[j:j + i]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes