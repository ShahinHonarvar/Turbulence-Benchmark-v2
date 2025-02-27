def palindrome_of_length_at_least_n(string):
    palindromes = set()
    for i in range(len(string) - 132):
        substring = string[i:i + 133]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes