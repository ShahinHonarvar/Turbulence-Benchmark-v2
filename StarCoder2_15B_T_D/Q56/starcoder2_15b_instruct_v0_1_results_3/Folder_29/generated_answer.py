def generate__code(text_specification):
    function_name, arguments = parse_text_specification(text_specification)
    _code = generate_function_definition(function_name, arguments)
    _code = remove_comments(_code)
    _code = delimit__code(_code)
    return _code

def parse_text_specification(text_specification):
    function_name = 'all_substring_of_size_n'
    arguments = ['string']
    return (function_name, arguments)

def generate_function_definition(function_name, arguments):
    _code = f'def {function_name}({', '.join(arguments)}):'
    _code += '    pass'
    return _code

def remove_comments(_code):
    _code = _code.replace('#', '')
    return _code

def delimit__code(_code):
    _code = f