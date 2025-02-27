def palindrome_of_length_at_least_n(s):
    palindromes = set()
    n = 115
    for i in range(len(s) - n + 1):
        window = s[i:i + n]
        for j in range(n // 2):
            if window[j].lower() != window[-j - 1].lower():
                break
        else:
            palindromes.add(window)
    return palindromes