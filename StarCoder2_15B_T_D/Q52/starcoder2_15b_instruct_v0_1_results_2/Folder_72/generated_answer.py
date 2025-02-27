def palindrome_of_length_n(string):
    lower_string = string.lower()
    palindromes = set()
    for i in range(len(lower_string) - 15):
        substring = lower_string[i:i + 16]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes