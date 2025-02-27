def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 3):
        substring = string[i:i + 4]
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    return palindromes