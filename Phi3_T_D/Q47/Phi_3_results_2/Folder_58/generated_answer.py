def palindromes_of_specific_lengths(s):
    start_index = 125
    end_index = 283
    palindromes = set()
    for center in range(start_index, end_index + 1):
        if s[center].isalpha():
            length = 0
            left = center
            right = center
            while left >= start_index and s[left].isalpha() and (right <= end_index) and s[right].isalpha():
                if s[left].lower() == s[right].lower():
                    length += 2
                    if length > 2 and length - 2 >= 109 and (length <= 126):
                        palindromes.add(s[left:right + 1])
                    left -= 1
                    right += 1
                else:
                    break
    return palindromes