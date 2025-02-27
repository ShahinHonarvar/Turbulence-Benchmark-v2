def palindromes_of_specific_lengths(s):
    s = s[:31]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 19, min(i + 31, len(s))):
            substring = s[i:j + 1]
            if substring.lower() == substring.lower()[::-1] and substring.isalpha():
                palindromes.add(substring)
    return palindromes