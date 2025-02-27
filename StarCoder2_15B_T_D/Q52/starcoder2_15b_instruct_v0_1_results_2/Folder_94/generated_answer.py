def palindrome_of_length_n(string):
    result = set()
    for i in range(len(string) - 92):
        substring = string[i:i + 93]
        if substring == substring[::-1]:
            if substring.isalpha():
                result.add(substring)
    return result