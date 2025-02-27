def palindrome_of_length_at_least_n(string):
    palindromes = set()
    n = 85
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring.isalpha() and substring.lower() == substring.lower()[::-1]:
            palindromes.add(substring)
    return palindromes