def palindrome_of_length_n(input_string):
    s = input_string.lower()
    result = set()
    for i in range(len(s) - 55):
        substring = s[i:i + 56]
        if substring == substring[::-1]:
            result.add(substring)
    return result