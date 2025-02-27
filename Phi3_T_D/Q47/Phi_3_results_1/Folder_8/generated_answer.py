def is_alphabetic_palindrome(string, low, high):
    while low < high:
        if not string[low].isalpha():
            low += 1
        elif not string[high].isalpha():
            high -= 1
        elif string[low].lower() != string[high].lower():
            return False
        else:
            low += 1
            high -= 1
    return True

def palindromes_of_specific_lengths(input_string):
    result_set = set()
    substring = input_string[17:73]
    for length in range(50, 52):
        for start in range(len(substring) - length + 1):
            if is_alphabetic_palindrome(substring, start, start + length - 1):
                result_set.add(substring[start:start + length])
    return result_set