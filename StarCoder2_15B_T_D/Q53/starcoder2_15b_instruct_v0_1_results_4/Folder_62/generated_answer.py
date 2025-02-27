def palindrome_of_length_at_least_n(string):
    palindromes = set()
    n = 31
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    return palindromes