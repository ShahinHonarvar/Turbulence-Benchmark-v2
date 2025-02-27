def palindrome_of_length_at_least_n(string):
    palindromes = set()
    n = 88
    for i in range(len(string) - n + 1):
        window = string[i:i + n]
        for j in range(n // 2):
            if window[j].lower() != window[-j - 1].lower():
                break
        else:
            palindromes.add(window)
    return palindromes