def palindrome_of_length_at_least_n(s):
    result_set = set()
    length = len(s)
    for i in range(length):
        for j in range(i + 143, length):
            substring = s[i:j + 1]
            if len(substring) >= 144 and substring.lower() == substring[::-1].lower():
                result_set.add(substring)
    return result_set