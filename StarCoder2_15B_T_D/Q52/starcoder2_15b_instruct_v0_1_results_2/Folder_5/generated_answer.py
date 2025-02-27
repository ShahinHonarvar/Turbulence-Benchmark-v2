def palindrome_of_length_n(string):
    n = 17
    result = set()
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring == substring[::-1] and substring.isalpha():
            result.add(substring)
    return result