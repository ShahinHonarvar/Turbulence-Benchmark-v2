def palindrome_of_length_n(s):
    s = s.lower()
    min_len = max(len(s) - 84, 0)
    palindromes = set()
    for i in range(min_len):
        potential_palindrome = s[i:i + 85].lower()
        if potential_palindrome.isalpha() and potential_palindrome == potential_palindrome[::-1]:
            palindromes.add(s[i:i + 85])
    return palindromes