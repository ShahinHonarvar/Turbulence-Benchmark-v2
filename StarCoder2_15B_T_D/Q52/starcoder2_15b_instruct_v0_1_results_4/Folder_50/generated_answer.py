def palindrome_of_length_n(string):
    if len(string) < 40:
        return set()
    palindromes = set()
    for i in range(len(string) - 39):
        substring = string[i:i + 40]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes