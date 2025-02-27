def palindrome_of_length_n(s):
    length = 84
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring == substring[::-1]:
            palindromes.add(substring.upper())
    return palindromes