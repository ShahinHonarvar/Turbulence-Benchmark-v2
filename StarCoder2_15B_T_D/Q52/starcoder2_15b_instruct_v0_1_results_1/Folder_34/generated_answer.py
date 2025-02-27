def palindrome_of_length_n(string):
    substrings = [string[i:i + 33] for i in range(len(string) - 32)]
    palindromes = set()
    for substring in substrings:
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    return palindromes