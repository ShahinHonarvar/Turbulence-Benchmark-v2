def palindrome_of_length_at_least_n(s):
    palindromes = set()
    for i in range(len(s) - 27):
        substring = s[i:i + 28]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes