from dataclasses import dataclass, field


@dataclass
class FigureContainer:
    figures: list[str] = field(default_factory=list)


@dataclass
class PythonOutput:
    fc: FigureContainer = field(default_factory=FigureContainer)
    stdout: str = ""

    @property
    def has_stdout(self) -> bool:
        return len(self.stdout) > 0

    @property
    def has_figures(self) -> bool:
        return len(self.fc.figures) > 0
