def palindrome_of_length_n(s):
    palindromes = set()
    s_lower = s.lower()
    for i in range(len(s_lower) - 89):
        substring = s_lower[i:i + 93]
        if substring.isalpha() and substring == substring[::-1]:
            palindromes.add(s_lower[i:i + 93])
    return palindromes