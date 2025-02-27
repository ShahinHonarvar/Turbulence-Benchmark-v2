def palindrome_of_length_n(string):
    substrings = [string[i:i + 401] for i in range(len(string) - 400)]
    palindromes = []
    for substring in substrings:
        if substring == substring[::-1] and substring.isalpha():
            palindromes.append(substring)
    return set(palindromes)