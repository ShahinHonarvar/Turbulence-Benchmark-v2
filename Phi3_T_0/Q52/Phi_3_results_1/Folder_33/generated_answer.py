def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 474):
        substring = s[i:i + 475]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes