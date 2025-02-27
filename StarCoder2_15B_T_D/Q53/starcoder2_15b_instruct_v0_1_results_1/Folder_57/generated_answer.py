def palindrome_of_length_at_least_n(string):
    string = string.lower()
    result = set()
    for i in range(len(string) - 92):
        for j in range(i + 92, len(string)):
            substring = string[i:j + 1]
            if substring == substring[::-1]:
                result.add(substring)
    return result