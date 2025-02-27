def palindrome_of_length_n(string):
    substring_length = 97
    palindromes = set()
    for i in range(len(string) - substring_length + 1):
        substring = string[i:i + substring_length]
        if substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes