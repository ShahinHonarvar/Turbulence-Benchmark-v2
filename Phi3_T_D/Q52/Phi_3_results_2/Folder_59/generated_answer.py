def palindrome_of_length_n(s):
    s = s.lower()
    s_len = len(s)
    palindromes = set()
    for i in range(s_len - 38):
        potential_palindrome = s[i:i + 39]
        if potential_palindrome == potential_palindrome[::-1]:
            palindromes.add(potential_palindrome)
    return palindromes