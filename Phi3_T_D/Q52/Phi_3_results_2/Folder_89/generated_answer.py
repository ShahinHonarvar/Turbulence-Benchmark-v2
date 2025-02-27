def palindrome_of_length_n(input_string):
    result_set = set()
    input_string = input_string.lower()
    for i in range(len(input_string) - 36):
        substring = input_string[i:i + 37]
        if substring == substring[::-1] and substring.isalpha():
            result_set.add(substring)
    return result_set