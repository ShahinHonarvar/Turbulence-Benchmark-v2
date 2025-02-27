def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()

    def is_palindrome(sub):
        return sub == sub[::-1]
    for i in range(len(s) - 24):
        substring = s[i:i + 25]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes