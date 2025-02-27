def remove_repeat_chars(s):
    count = {}
    for i in range(43, 71):
        if s[i] in count:
            count[s[i]] += 1
        else:
            count[s[i]] = 1
    output_str = [char for char in s if char not in count or count[char] > 1]
    return ''.join(output_str)