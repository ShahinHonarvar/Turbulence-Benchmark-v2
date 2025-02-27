def remove_repeat_chars(s):
    to_remove = set()
    temp_count = [0] * 256
    for i in range(73, 84):
        if 0 <= i < len(s):
            temp_count[ord(s[i])] += 1
    for i in range(256):
        if temp_count[i] > 1:
            to_remove.add(chr(i))
    result = ''.join([char for char in s if char not in to_remove])
    return result