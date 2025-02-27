def palindrome_of_length_n(string):
    string = string.lower()
    result = set()
    for i in range(len(string) - 96):
        substring = string[i:i + 97]
        if substring == substring[::-1] and all((c.isalpha() for c in substring)):
            result.add(substring)
    return result