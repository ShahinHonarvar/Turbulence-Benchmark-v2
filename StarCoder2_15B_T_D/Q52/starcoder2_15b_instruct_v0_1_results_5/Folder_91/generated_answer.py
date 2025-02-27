def palindrome_of_length_n(string):
    palindromes = set()
    length_n_substrings = [string[i:i + 7] for i in range(len(string) - 6)]
    for substring in length_n_substrings:
        if substring.lower() == substring[::-1].lower():
            palindromes.add(substring)
    return palindromes