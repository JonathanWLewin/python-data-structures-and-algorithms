from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter


def format_code(code: str, overrides=[]) -> str:
    highlighted_code = highlight(code, PythonLexer(), HtmlFormatter(linenos=True))
    highlighted_code = highlighted_code.replace(f'<span class="k">return</span>', f'<span class="r">return</span>')
    for override in overrides:
        if override.override_type == 'class':
            highlighted_code = highlighted_code.replace(f'<span class="n">{override.name}</span>', f'<span class="nc">{override.name}</span>')
        elif override.override_type == 'func':
            highlighted_code = highlighted_code.replace(f'<span class="n">{override.name}</span>', f'<span class="nf">{override.name}</span>')
    return highlighted_code