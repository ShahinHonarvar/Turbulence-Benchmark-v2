import re

def generate_code_from_text_specification(instruction: str) -> str:
    text_specification_pattern = '<(.*?)>'
    text_specification = re.search(text_specification_pattern, instruction).group(1)
    function_name_pattern = '^(.*?)\\\\('
    argument_name_pattern = '\\\\((.*?)\\\\)'
    function_name = re.search(function_name_pattern, text_specification).group(1)
    argument_name = re.search(argument_name_pattern, text_specification).group(1)
    length_pattern = 'length equal to (\\\\d+)'
    length = int(re.search(length_pattern, text_specification).group(1))
    _code = f'def {function_name}({argument_name}):    substrings = set()    for i in range(len({argument_name}) - {length} + 1):        substring = {argument_name}[i:i + {length}]        if len(set(substring)) == {length}:            substrings.add(substring)    return list(substrings)'
    _code = re.sub('#.*?\\\n', '', _code)
    delimited_code = f