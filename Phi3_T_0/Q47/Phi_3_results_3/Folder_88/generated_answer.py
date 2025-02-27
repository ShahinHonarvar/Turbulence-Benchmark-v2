def palindromes_of_specific_lengths(s):
    s = s[11:88]
    palindromes = set()
    for i in range(len(s)):
        for length in range(4, 6):
            if i + length > len(s):
                break
            substring = s[i:i + length]
            if substring.isalpha() and substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes