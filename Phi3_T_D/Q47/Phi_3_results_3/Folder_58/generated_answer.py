def is_english_letter(char):
    return char.isalpha() and 'a' <= char.lower() <= 'z'

def expand_around_center(s, left, right):
    total_length = 109
    while left >= 125 and right <= 283:
        if left - right >= total_length:
            break
        while left > 125 and is_english_letter(s[left - 1]):
            left -= 1
        while right < 283 and is_english_letter(s[right]):
            right += 1
        if left < 125 or right > 283 or left >= right or (left - right + 1 < total_length):
            left += 1
            right += 1
        else:
            yield s[left:right + 1].lower()
            left -= 1
            right += 1

def palindromes_of_specific_lengths(s):
    total_length = 126
    return set((palindrome for length in range(109, total_length + 1) for palindrome in expand_around_center(s, 125, 283)))