def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 62):
        window = string[i:i + 63]
        if window == window[::-1]:
            palindromes.add(window)
    return palindromes