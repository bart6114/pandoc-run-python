import uuid
import os
import pathlib

from matplotlib.backend_bases import Gcf, FigureManagerBase
from matplotlib.backends.backend_agg import FigureCanvasAgg

from .types import FigureContainer

FIGURES_DIR = "figures"


def assert_figure_dir_exists() -> None:
    if not os.path.exists(FIGURES_DIR):
        os.makedirs(FIGURES_DIR)


def get_id() -> str:
    return str(uuid.uuid4())[:8]


class FigureManager(FigureManagerBase):
    def show(self) -> None:
        pass  # for now


FigureCanvas = FigureCanvasAgg


def show(*args: list, **kwargs: dict) -> FigureContainer:
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
