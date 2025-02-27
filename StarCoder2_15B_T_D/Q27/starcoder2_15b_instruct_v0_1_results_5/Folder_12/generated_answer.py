def create__code(text_specification: str) -> str:
    function_name, argument_name, index = text_specification[1:-1].split(' ')
    index = int(index)
    _code = f'\ndef {function_name}({argument_name}):\n    {argument_name}.insert({index + 1}, 96)\n    return {argument_name}\n'
    _code = _code.strip()
    return _code