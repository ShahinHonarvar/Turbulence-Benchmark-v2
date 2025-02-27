def palindrome_of_length_n(s):
    s_lower = s.lower()
    palindromes = set()
    for i in range(len(s_lower) - 391):
        substring = s_lower[i:i + 392]
        if substring == substring[::-1]:
            palindromes.add(substring.capitalize())
    return palindromes