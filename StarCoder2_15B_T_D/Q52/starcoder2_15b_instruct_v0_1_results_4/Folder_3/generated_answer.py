def palindrome_of_length_n(string):
    result = set()
    n = 100
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if all((c.isalpha() for c in substring)):
            if substring == substring[::-1]:
                result.add(substring)
    return result