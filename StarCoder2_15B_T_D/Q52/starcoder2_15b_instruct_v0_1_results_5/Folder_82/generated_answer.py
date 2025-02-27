def palindrome_of_length_n(s: str) -> set:
    palindromes = set()
    n = 28
    for i in range(len(s) - n + 1):
        window = s[i:i + n]
        if window == window[::-1] and all((ch.isalpha() for ch in window)):
            palindromes.add(window)
    return palindromes