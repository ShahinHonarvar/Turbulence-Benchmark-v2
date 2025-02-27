import re

def create__code(text_specification):
    function_name_match = re.search("'(.*?)'", text_specification)
    if function_name_match:
        function_name = function_name_match.group(1)
    argument_name_match = re.search('a (.*?) in the given string', text_specification)
    if argument_name_match:
        argument_name = argument_name_match.group(1)
    character_range_match = re.search('between the indices (.*?) and (.*?) in the given string', text_specification)
    if character_range_match:
        start_index, end_index = map(int, character_range_match.groups())

    def filter_chars(string):
        return ''.join((character for i, character in enumerate(string) if i < start_index or i >= end_index or character <= 'E' or (character >= '~')))
    _code = f"\ndef {function_name}({argument_name}):\n    return ''.join(character for i, character in enumerate({argument_name}) if i < {start_index} or i >= {end_index} or character <= 'E' or character >= '~')\n"
    return _code