def palindrome_of_length_n(s):
    length = 186
    result_set = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length].lower()
        if substring == substring[::-1] and substring.isalpha():
            result_set.add(substring)
    return result_set