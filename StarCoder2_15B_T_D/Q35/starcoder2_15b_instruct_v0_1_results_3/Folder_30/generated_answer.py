import re

def remove_repeat_chars(text):
    match = re.search('<(.*?)>', text)
    if match:
        function_name, argument_name = match.group(1).split(' ', 1)
        argument_name = argument_name.split(' ', 1)[0]
        _code = f'\ndef {function_name}({argument_name}):\n    char_counts = {{}}\n    for char in {argument_name}:\n        char_counts[char] = char_counts.get(char, 0) + 1\n\n    repeated_chars = [char for char, count in char_counts.items() if count > 1]\n\n    result = ""\n    for char in {argument_name}:\n        if char in repeated_chars:\n            continue\n        result += char\n\n    return result\n'
        return _code
    else:
        return ''