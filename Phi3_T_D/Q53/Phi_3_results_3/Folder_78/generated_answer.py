def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 95):
        substring = s[i:i + 96]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes