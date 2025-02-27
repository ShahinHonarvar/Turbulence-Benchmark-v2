def palindrome_of_length_at_least_n(string):
    palindromes = set()
    for i in range(len(string) - 36):
        window = string[i:i + 37]
        if window == window[::-1]:
            palindromes.add(window)
    return palindromes