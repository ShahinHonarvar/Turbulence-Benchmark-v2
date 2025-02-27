def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 6):
        substring = s[i:i + 7]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes