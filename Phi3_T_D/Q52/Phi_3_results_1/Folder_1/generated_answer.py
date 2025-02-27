def palindrome_of_length_n(string):
    result_set = set()
    string = string.lower()
    for i in range(len(string) - 26):
        substring = string[i:i + 27]
        if substring == substring[::-1]:
            result_set.add(substring)
    return result_set