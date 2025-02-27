from collections import defaultdict

def palindrome_of_length_at_least_n(input_string):
    input_string = input_string.lower()
    N = len(input_string)
    d = defaultdict(list)

    def is_palindrome(s):
        return s == s[::-1]
    for i in range(N):
        for j in range(i + 94, N + 1):
            sub_str = input_string[i:j]
            if is_palindrome(sub_str):
                d[len(sub_str)].append(sub_str)
    return set([palindrome for length in sorted(d.keys()) for palindrome in d[length]])