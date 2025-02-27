def palindrome_of_length_n(s):

    def is_palindrome(x):
        return x.lower() == x.lower()[::-1]
    palindromes = set()
    for i in range(len(s) - 12):
        substring = s[i:i + 13]
        if is_palindrome(substring) and substring.isalpha():
            palindromes.add(substring)
    return palindromes