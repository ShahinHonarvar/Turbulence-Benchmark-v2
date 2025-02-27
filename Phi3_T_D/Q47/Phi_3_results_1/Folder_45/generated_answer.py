def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(input_string):
    half_length = 60 // 2
    palindromes = set()
    start_index = min(70, len(input_string) - 140)
    end_index = max(140, start_index + 71)
    for center in range(start_index + half_length, end_index):
        left = center - half_length
        right = center + half_length + 1
        substring = input_string[left:right].lower()
        if all((char.isalpha() for char in substring)):
            if left >= start_index and substring.count(substring[half_length]) <= 1:
                current = substring[half_length]
                for i in range(half_length - 1, -1, -1):
                    palindrome = substring[left:left + i + 1] + substring[right - i - 1:right]
                    if is_palindrome(palindrome):
                        palindromes.add(palindrome)
            elif all((substring[i] == substring[i + 1] for i in range(half_length - 1))):
                palindromes.add(substring[left:right])
    return palindromes