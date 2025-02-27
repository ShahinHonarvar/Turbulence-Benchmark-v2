def palindrome_of_length_at_least_n(string):
    result_set = set()
    for i in range(len(string)):
        for j in range(i + 10, len(string) + 1):
            substring = string[i:j]
            if substring.lower() == substring[::-1].lower() and substring.isalpha():
                result_set.add(substring.lower())
    return result_set