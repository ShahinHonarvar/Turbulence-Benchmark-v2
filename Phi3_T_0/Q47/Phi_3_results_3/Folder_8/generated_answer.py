def palindromes_of_specific_lengths(s):
    start, end = (17, 72)
    s = s[start - 1:end]
    palindromes = set()
    for i in range(start, end + 1):
        for j in range(i + 49, min(i + 52, end - start + 2)):
            substring = s[i:j + 1]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes