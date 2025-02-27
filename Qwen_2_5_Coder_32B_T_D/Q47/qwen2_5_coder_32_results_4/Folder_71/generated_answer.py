def palindromes_of_specific_lengths(s):
    s = s[18:66]
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for i in range(len(s) - 22):
        for j in range(23, 37):
            if i + j <= len(s):
                substring = s[i:i + j]
                if substring == substring[::-1]:
                    palindromes.add(substring)
    return palindromes