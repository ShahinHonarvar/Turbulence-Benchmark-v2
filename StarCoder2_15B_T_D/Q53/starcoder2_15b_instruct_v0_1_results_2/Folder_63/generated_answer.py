def palindrome_of_length_at_least_n(string):
    palindromes = set()
    string = string.lower()
    for i in range(len(string) - 37 + 1):
        substring = string[i:i + 37]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes