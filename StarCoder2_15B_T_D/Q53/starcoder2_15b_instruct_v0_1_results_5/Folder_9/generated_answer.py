def palindrome_of_length_at_least_n(text):
    n = 95
    palindromes = set()
    for i in range(len(text) - n + 1):
        window = text[i:i + n]
        reversed_window = window[::-1]
        if window.lower() == reversed_window.lower():
            palindromes.add(window)
    return palindromes