def palindromes_of_specific_lengths(s):
    palindromes = set()
    start, end = (36, 92)
    for i in range(start, end + 1):
        for j in range(i + 9, min(i + 36, end + 1) + 1):
            substring = s[i:j].lower()
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes