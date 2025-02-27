def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 44):
        window = s[i:i + 44]
        if window == window[::-1]:
            palindromes.add(window)
    return palindromes