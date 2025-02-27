def palindromes_of_specific_lengths(s):
    start, end = (27, 77)
    s = s[start:end + 1].lower()
    palindromes = set()
    for i in range(start, end - 18):
        for j in range(i + 18, min(i + 19, end + 1)):
            substring = s[i:j + 1]
            if substring.isalpha() and substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes