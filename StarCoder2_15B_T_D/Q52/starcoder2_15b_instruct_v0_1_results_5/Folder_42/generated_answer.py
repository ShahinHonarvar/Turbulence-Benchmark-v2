def palindrome_of_length_n(string):
    n = 279
    palindromes = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    return palindromes