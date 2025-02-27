def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 93):
        substring = string[i:i + 94]
        if substring.lower() == substring[::-1].lower():
            if substring.isalpha():
                palindromes.add(substring)
    return palindromes