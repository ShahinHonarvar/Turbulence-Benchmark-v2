def palindrome_of_length_at_least_n(string):
    length = 115
    set_of_palindromes = set()
    string = string.lower()

    def is_palindrome(s):
        return s == s[::-1]
    for i in range(len(string)):
        for j in range(i + length, len(string) + 1):
            substring = string[i:j]
            if is_palindrome(substring):
                set_of_palindromes.add(substring)
    return set_of_palindromes