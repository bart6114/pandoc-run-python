from dataclasses import dataclass, field
import uuid
import os
import pathlib

from matplotlib.backend_bases import Gcf, FigureManagerBase
from matplotlib.backends.backend_agg import FigureCanvasAgg

FIGURES_DIR = "figures"


@dataclass
class FigureContainer:
    figures: list[str] = field(default_factory=list)


def assert_figure_dir_exists():
    if not os.path.exists(FIGURES_DIR):
        os.makedirs(FIGURES_DIR)


def get_id() -> str:
    return str(uuid.uuid4())[:8]


class FigureManager(FigureManagerBase):
    def show(self):
        pass  # for now


FigureCanvas = FigureCanvasAgg


def show(*args, **kwargs):
    assert_figure_dir_exists()
    fc = FigureContainer()
    id = get_id()
    for num, figmanager in enumerate(Gcf.get_all_fig_managers()):
        fn = (
            pathlib.Path(FIGURES_DIR, f"figure_{id}_{num}.png")
            .resolve()
            .relative_to(pathlib.Path.cwd())
        )
        figmanager.canvas.figure.savefig(fn)
        fc.figures.append(fn)

    return fc
