from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from pyrefine.StyledCode import StyledCode


def format_code(code):
    highlighted_code = highlight(code, PythonLexer(), HtmlFormatter(linenos=True))
    css = HtmlFormatter().get_style_defs()
    return StyledCode(highlighted_code, css)