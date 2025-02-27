def palindrome_of_length_at_least_n(s: str) -> set:
    palindromes = set()
    n = 119
    for i in range(len(s) - n + 1):
        window = s[i:i + n]
        for j in range(n // 2):
            if window[j].lower() != window[n - j - 1].lower():
                break
        else:
            palindromes.add(window)
    return palindromes