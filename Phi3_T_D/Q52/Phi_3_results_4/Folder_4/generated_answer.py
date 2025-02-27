def palindrome_of_length_n(string):
    result = set()
    string = string.lower()
    for i in range(len(string) - 14):
        substring = string[i:i + 15]
        if substring == substring[::-1]:
            result.add(substring)
    return result