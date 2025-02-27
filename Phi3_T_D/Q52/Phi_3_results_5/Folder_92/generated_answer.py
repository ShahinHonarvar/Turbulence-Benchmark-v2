def palindrome_of_length_n(in_str):
    n = 10
    result_set = set(filter(lambda x: x == x[::-1], (in_str[i:i + n].lower() for i in range(len(in_str) - n + 1) if in_str[i:i + n].isalpha())))
    return result_set