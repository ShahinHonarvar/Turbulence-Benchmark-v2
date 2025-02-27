def palindrome_of_length_at_least_n(input_string):
    palindromes = set()
    input_string = input_string.lower()
    n = len(input_string)

    def expand(left, right):
        while left >= 0 and right < n and (input_string[left] == input_string[right]):
            if right - left + 1 >= 7:
                palindromes.add(input_string[left:right + 1])
            left -= 1
            right += 1
    for i in range(n):
        expand(i, i)
        expand(i, i + 1)
    return palindromes