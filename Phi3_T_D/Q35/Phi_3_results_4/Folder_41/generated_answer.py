def remove_repeat_chars(s):
    altered = []
    counter = {}
    for i, char in enumerate(s):
        if 3 <= i <= 8:
            counter[char] = counter.get(char, 0) + 1
        elif char in counter and counter[char] > 1:
            counter[char] -= 1
        else:
            altered.append(char)
    return ''.join(altered)