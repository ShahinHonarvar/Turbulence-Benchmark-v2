def palindrome_of_length_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s) - 8):
        substring = s[i:i + 9]
        if substring == substring[::-1] and substring.isalpha():
            palindromes.add(substring)
    return palindromes