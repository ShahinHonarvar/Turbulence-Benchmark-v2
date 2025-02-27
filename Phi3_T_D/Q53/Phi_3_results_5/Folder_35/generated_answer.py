def palindrome_of_length_at_least_n(string):
    n = 26
    valid_palindromes = set()

    def is_palindrome(s):
        return s == s[::-1]
    string = string.lower()
    for i in range(len(string)):
        for j in range(i + n, len(string) + 1):
            sub = string[i:j]
            if is_palindrome(sub):
                valid_palindromes.add(sub)
    return valid_palindromes