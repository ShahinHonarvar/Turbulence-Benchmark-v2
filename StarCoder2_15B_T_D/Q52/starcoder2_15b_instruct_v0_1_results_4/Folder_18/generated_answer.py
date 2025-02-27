def palindrome_of_length_n(string):
    result = set()
    n = 392
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring == substring[::-1]:
            if all((c.isalpha() for c in substring)):
                result.add(substring)
    return result