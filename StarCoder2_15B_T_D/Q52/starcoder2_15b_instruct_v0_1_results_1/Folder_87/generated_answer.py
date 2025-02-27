def palindrome_of_length_n(string):
    n = 57
    modified_string = ''.join((c for c in string.lower() if c.isalpha()))
    result = set()
    for i in range(len(modified_string) - n + 1):
        substring = modified_string[i:i + n]
        if substring == substring[::-1]:
            result.add(substring)
    return result