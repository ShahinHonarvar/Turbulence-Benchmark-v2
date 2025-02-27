def palindrome_of_length_at_least_n(string):
    string = string.lower()
    window_size = 137
    if len(string) < window_size:
        return set()
    palindromes = set()
    for i in range(len(string) - window_size + 1):
        window = string[i:i + window_size]
        if window == window[::-1]:
            palindromes.add(window)
    return palindromes