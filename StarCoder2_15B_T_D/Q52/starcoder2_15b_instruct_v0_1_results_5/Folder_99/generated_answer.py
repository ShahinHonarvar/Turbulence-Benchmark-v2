def create__code(text_specification):
    instructions = extract_instructions(text_specification)
    _code = translate_instructions_to__code(instructions)
    _code_formatted = format__code(_code)
    _code_delimited = delimit__code(_code_formatted)
    return _code_delimited