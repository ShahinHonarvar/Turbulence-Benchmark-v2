def palindromes_of_specific_lengths(s):

    def is_palindrome(p):
        return p.lower() == p[::-1].lower()
    palindromes = set()
    substring = s[13:100]
    for i in range(26, 30):
        for j in range(0, len(substring) - i + 1):
            potential_palindrome = substring[j:j + i]
            if potential_palindrome.isalpha() and is_palindrome(potential_palindrome):
                palindromes.add(potential_palindrome.lower())
    return palindromes