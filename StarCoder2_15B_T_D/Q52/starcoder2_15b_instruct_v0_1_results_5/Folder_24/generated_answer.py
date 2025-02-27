def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 28):
        substring = s[i:i + 29]
        if substring == substring[::-1]:
            if substring.isalpha():
                palindromes.add(substring)
    return palindromes