def palindrome_of_length_n(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    palindromes = set()
    s_lower = s.lower()
    for i in range(len(s_lower) - 22):
        substring = s_lower[i:i + 23]
        if all((c in alphabet for c in substring)) and substring == substring[::-1]:
            palindromes.add(substring)
    return palindromes