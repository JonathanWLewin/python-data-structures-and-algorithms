class Override:
    name: str
    override_type: str
    def __init__(self, name, override_type) -> None:
        self.name = name
        self.override_type = override_type