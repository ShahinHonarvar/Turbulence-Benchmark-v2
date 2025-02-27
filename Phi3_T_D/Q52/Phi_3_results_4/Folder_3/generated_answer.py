def palindrome_of_length_n(input_string):
    input_string = input_string.lower()
    length = 100
    return_set = set()
    for i in range(len(input_string) - length + 1):
        substring = input_string[i:i + length]
        if substring.isalpha() and substring == substring[::-1]:
            return_set.add(substring)
    return return_set