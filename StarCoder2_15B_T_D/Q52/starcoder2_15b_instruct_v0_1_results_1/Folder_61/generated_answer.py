def palindrome_of_length_n(string):
    result = set()
    n = 74
    for i in range(len(string) - n + 1):
        substring = string[i:i + n]
        if substring == substring[::-1]:
            if substring.isalpha():
                result.add(substring)
    return result