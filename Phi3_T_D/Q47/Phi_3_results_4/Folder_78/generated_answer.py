def palindromes_of_specific_lengths(s):
    selected_substr = s[15:73]
    palindromes = set()
    for i in range(len(selected_substr) - 18):
        for length in range(19, 56):
            char = selected_substr[i]
            if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
                current_palindrome = char
                for j in range(1, length // 2 + 1):
                    if i + length <= len(selected_substr):
                        left_char = selected_substr[i + j - 1]
                        right_char = selected_substr[i + length - j]
                        if 'a' <= left_char <= 'z' and 'A' <= right_char <= 'Z':
                            if left_char.lower() == right_char.lower():
                                current_palindrome = left_char + current_palindrome + right_char
                            else:
                                break
                        else:
                            break
                else:
                    palindromes.add(current_palindrome)
    return palindromes