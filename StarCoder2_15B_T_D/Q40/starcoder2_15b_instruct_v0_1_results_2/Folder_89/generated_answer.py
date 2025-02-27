import textwrap

def create__code(text):
    code = textwrap.dedent(textwrap.unwrap(text, width=1000))
    return code