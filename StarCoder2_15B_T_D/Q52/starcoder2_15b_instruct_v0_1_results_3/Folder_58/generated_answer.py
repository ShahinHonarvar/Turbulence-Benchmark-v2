def palindrome_of_length_n(string):
    n = 223
    result = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring == substring[::-1]:
            result.add(substring)
    return result