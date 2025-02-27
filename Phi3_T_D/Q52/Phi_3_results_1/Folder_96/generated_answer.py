def palindrome_of_length_n(s):
    length = 83
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring.isalpha():
            if substring == substring[::-1]:
                palindromes.add(substring)
    return palindromes