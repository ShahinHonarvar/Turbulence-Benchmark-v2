def palindrome_of_length_n(string):
    palindromes = set()
    lowercase_string = string.lower()
    for i in range(len(lowercase_string) - 5):
        substring = lowercase_string[i:i + 6]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes