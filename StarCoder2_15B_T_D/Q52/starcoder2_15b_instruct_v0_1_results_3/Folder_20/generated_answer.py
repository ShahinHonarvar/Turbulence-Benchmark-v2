def palindrome_of_length_n(string):
    string = string.lower()
    result = set()
    for i in range(len(string) - 52):
        substring = string[i:i + 53]
        if substring == substring[::-1]:
            result.add(substring)
    return result