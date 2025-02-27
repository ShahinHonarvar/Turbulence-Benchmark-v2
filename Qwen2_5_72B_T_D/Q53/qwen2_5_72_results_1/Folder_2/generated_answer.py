def palindrome_of_length_at_least_n(input_string):

    def is_palindrome(s):
        return s == s[::-1]
    input_string = input_string.lower()
    len_input = len(input_string)
    palindromes = set()
    for i in range(len_input):
        for j in range(i + 54, len_input):
            substring = input_string[i:j + 1]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes