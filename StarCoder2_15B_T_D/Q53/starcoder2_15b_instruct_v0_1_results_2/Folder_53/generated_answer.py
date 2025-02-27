def palindrome_of_length_at_least_n(string):
    string = string.lower()
    result = set()
    for i in range(len(string)):
        for j in range(i + 64, len(string) + 1):
            substring = string[i:j]
            if substring == substring[::-1]:
                result.add(substring)
    return result