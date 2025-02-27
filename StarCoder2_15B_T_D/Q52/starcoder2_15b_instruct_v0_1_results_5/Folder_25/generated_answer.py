def palindrome_of_length_n(string):
    n = 90
    result = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring == substring[::-1]:
            if all((ch.isalpha() for ch in substring)):
                result.add(substring)
    return result