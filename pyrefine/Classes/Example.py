class Example:
    title: str
    description: str
    input: str
    output: str
    def __init__(self, title: str, description: str, input = '', output = '', state = None) -> None:
        self.title = title
        self.description = description
        self.input = input
        self.output = output
        self.state = state