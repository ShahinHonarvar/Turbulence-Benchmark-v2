def palindrome_of_length_n(input_string):

    def is_palindrome(s):
        return s.lower() == s[::-1].lower()
    set_of_palindromes = set()
    input_string = input_string.lower()
    for i in range(len(input_string) - 3):
        substring = input_string[i:i + 4]
        if is_palindrome(substring):
            set_of_palindromes.add(substring)
    return set_of_palindromes