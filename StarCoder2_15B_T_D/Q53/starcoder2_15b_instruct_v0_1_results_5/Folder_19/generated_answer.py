def palindrome_of_length_at_least_n(string):
    string = string.lower()
    palindromes = set()
    for i in range(len(string) - 22):
        window = string[i:i + 23]
        for j in range(len(window) // 2):
            if window[j] != window[-j - 1]:
                break
        else:
            palindromes.add(window)
    return palindromes