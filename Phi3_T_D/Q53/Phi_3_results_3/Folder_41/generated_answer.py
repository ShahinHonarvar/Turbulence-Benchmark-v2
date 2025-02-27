def palindrome_of_length_at_least_n(input_string):
    result = set()
    input_string = input_string.lower()
    for i in range(len(input_string) - 27):
        for j in range(i + 27, len(input_string) + 1):
            substring = input_string[i:j]
            if substring.isalpha() and substring == substring[::-1]:
                result.add(substring)
    return result