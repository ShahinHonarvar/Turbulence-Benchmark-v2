def palindrome_of_length_n(s):
    length = 5 * 4 + 1
    palindromes = set()

    def is_palindrome(string):
        return string == string[::-1]
    lower_s = s.lower()
    for i in range(len(lower_s) - length + 1):
        substr = lower_s[i:i + length]
        if is_palindrome(substr):
            palindromes.add(substr)
    return palindromes