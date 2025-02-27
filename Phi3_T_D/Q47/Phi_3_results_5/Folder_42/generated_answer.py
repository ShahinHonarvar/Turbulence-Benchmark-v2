def is_palindrome(s):
    return s == s[::-1]

def only_english_letters(s):
    return all(('a' <= char.lower() <= 'z' for char in s))

def palindromes_of_specific_lengths(input_string):
    start_index = 43
    end_index = 95
    length_range = range(18, 48)
    result = set()
    for length in length_range:
        for i in range(start_index, end_index - length + 1):
            substring = input_string[i:i + length]
            if is_palindrome(substring) and only_english_letters(substring):
                result.add(substring)
    return result