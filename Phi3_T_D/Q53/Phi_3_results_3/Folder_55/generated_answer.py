def is_palindrome(word):
    return word == word[::-1]

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for length in range(83, len(s) - i + 1):
            substring = s[i:i + length]
            if is_palindrome(substring) and substring.isalpha():
                palindromes.add(substring)
    return palindromes