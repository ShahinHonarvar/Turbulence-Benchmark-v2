import re

def generate__code(text_specification):
    text = re.search('<(.*)>', text_specification).group(1)
    _code = "\ndef filter_chars(string):\n    for i in range(672, 709):\n        if chr(i) > 'X' and chr(i) < '}':\n            string = string.replace(chr(i), '')\n    return string\n"
    _code = re.sub('#[^\\\n]*\\\n', '', _code)
    _code = re.sub('"""[^"]*"""', '', _code)
    return _code