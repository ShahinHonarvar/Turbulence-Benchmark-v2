def palindrome_of_length_n(input_string):

    def is_palindrome(s):
        return s == s[::-1]
    length = 96
    palindromes = set()
    string_lower = input_string.lower()
    for i in range(len(string_lower) - length + 1):
        substring = string_lower[i:i + length]
        if is_palindrome(substring):
            palindromes.add(substring.lower())
    return palindromes