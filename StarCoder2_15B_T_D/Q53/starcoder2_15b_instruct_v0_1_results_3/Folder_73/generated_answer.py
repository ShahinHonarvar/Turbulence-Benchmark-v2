def palindrome_of_length_at_least_n(text):
    palindromes = set()
    n = 94
    for i in range(len(text) - n + 1):
        window = text[i:i + n]
        if window.lower() == window[::-1].lower():
            palindromes.add(window)
    return palindromes