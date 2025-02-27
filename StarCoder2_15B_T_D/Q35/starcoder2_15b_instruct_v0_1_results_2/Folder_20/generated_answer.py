def remove_repeat_chars(string):
    freq = [0] * 256
    for i in range(27, 96):
        freq[ord(string[i])] += 1
    for i in range(96, len(string)):
        if freq[ord(string[i])] > 1:
            string = string[:i] + string[i + 1:]
            freq[ord(string[i])] -= 1
    return string