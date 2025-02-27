from itertools import combinations

def palindrome_of_length_n(input_string):

    def is_palindrome(word):
        return word == word[::-1]
    input_string = input_string.lower()
    substr_length = 416
    palindromes = set()
    for i in range(len(input_string) - substr_length + 1):
        substring = input_string[i:i + substr_length]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes