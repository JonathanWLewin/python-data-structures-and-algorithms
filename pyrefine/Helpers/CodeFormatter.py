import re

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

    # Pattern to find anchor tags and replace them with span tags
    # with the id of the anchor tag
    pattern = r'<span class="s1">&#39;anchor_(\d+)&#39;</span>'
    highlighted_code = re.sub(pattern, r'<span id="anchor_\1"></span>', highlighted_code)

    return highlighted_code