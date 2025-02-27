def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 52):
        potential_palindrome = s[i:i + 53]
        if potential_palindrome == potential_palindrome[::-1]:
            palindromes.add(potential_palindrome.upper())
    return palindromes