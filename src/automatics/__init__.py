"""automatics."""

__version__ = "0.0.6"

from . import element, geom, rd, utils
from .geom import Geometry
from .identity import Identity
from .model import Model
from .view import View

__all__ = [
    "Geometry",
    "Identity",
    "Model",
    "View",
    "element",
    "geom",
    "rd",
    "utils",
]
