def palindrome_of_length_n(string):
    window_size = 15
    palindromes = set()
    for i in range(len(string) - window_size + 1):
        substring = string[i:i + window_size]
        if substring == substring[::-1] and all((c.isalpha() for c in substring)):
            palindromes.add(substring.lower())
    return palindromes