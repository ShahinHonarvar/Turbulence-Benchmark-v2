def palindrome_of_length_at_least_n(s):
    s_lower = s.lower()
    n = 20
    palindromes = set()
    for i in range(len(s_lower) - n + 1):
        window = s_lower[i:i + n]
        if window == window[::-1]:
            palindromes.add(window)
    return palindromes