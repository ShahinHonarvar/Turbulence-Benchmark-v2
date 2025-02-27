def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 337):
        substring = s[i:i + 338]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes