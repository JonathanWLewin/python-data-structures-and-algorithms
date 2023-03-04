class StyledCode:
    code = str
    css = str
    def __init__(self, code, css) -> None:
        self.code = code
        self.css = css