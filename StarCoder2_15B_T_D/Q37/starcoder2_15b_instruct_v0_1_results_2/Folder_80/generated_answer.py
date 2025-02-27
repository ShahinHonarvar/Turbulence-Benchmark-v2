import re

def generate__code(instruction: str) -> str:
    """
    Generates Python code based on a given instruction surrounded by angle brackets.
    The Python code should not contain any comments. The Python code should be
    delimited only by triple backticks.
    """
    text_spec_pattern = '<(.*?)>'
    match = re.search(text_spec_pattern, instruction)
    if match is None:
        raise ValueError('No text specification found in the instruction.')
    text_spec = match.group(1)
    _code = "\ndef filter_chars(s: str) -> str:\n    filtered = [c for i, c in enumerate(s) if not (36 <= i <= 79 and 'a' <= c <= 'i')]\n    return ''.join(filtered)\n"
    _code = _code.strip()
    return _code