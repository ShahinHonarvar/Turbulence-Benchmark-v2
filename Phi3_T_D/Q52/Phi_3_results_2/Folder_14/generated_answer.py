def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_n(input_string):
    result_set = set()
    input_string = input_string.lower()
    for i in range(len(input_string) - 62):
        substring = input_string[i:i + 63]
        if all((char.isalpha() for char in substring)):
            if is_palindrome(substring):
                result_set.add(substring)
    return result_set