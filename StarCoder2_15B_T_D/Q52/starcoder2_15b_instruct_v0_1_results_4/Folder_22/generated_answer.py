def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 19):
        substring = string[i:i + 20]
        if substring.isalpha():
            if substring.lower() == substring[::-1].lower():
                palindromes.add(substring)
    return palindromes