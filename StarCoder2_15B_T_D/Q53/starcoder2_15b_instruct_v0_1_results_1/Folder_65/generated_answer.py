def palindrome_of_length_at_least_n(text):
    palindromes = set()
    window_size = 15
    for i in range(len(text) - window_size + 1):
        window = text[i:i + window_size]
        if window == window[::-1]:
            palindromes.add(window)
    return palindromes