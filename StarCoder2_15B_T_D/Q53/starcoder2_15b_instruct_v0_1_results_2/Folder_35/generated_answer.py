def palindrome_of_length_at_least_n(string):
    if not isinstance(string, str):
        raise TypeError('The argument must be a string.')
    string = string.lower()
    result = set()
    for i in range(len(string) - 25):
        for j in range(i + 25, len(string)):
            substring = string[i:j + 1]
            if substring == substring[::-1]:
                result.add(substring)
    return result