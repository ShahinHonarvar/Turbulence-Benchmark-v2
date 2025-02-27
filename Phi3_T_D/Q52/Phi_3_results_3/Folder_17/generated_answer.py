def palindrome_of_length_n(input_string):
    input_string = input_string.lower()
    result_set = set()
    for i in range(len(input_string) - 288):
        substring = input_string[i:i + 289]
        if substring.isalpha() and substring == substring[::-1]:
            result_set.add(substring)
    return result_set