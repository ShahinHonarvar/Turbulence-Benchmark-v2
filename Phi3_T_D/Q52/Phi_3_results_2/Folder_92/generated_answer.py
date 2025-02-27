def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def palindrome_of_length_n(string):
    palindromes = set()
    for i in range(len(string) - 9):
        sub = string[i:i + 10].lower()
        if sub.isalpha() and is_palindrome(sub):
            palindromes.add(sub)
    return palindromes