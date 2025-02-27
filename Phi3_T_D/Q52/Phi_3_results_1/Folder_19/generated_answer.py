def is_valid_character(char):
    return char.isalpha()

def is_palindrome(substring):
    return substring == substring[::-1]

def palindrome_of_length_n(input_string):
    palindromes = set()
    input_string = input_string.lower()
    for i in range(len(input_string) - 66):
        if all((is_valid_character(char) for char in input_string[i:i + 67])):
            if is_palindrome(input_string[i:i + 67]):
                palindromes.add(input_string[i:i + 67])
    return palindromes