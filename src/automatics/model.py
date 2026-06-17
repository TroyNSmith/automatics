"""Calculation metadata."""

import hashlib
import json

from pydantic import BaseModel, model_validator


class Model(BaseModel):
    r"""Calculation model specification.

    Attributes
    ----------
    program : str
        Quantum chemistry program used (psi4, ORCA, ...)
    program_version : str, optional
        Quantum chemistry program version.
    calc_type : str
        Calculation type (energy, optimization, ...)
    method : str
        Computational method (B3LYP, MP2, ...)
    basis : str, optional
        Orbital basis set.

    Example
    -------
    ```
    opt_model = Model(
        program = "orca",
        program_version = "6.1.1",
        calc_type = "optimization",
        method = "b3lyp",
        basis = "def2-SVP",
    )
    ```
    """

    program: str
    program_version: str | None = None
    calc_type: str
    method: str
    basis: str | None = None
    hash: str | None = None

    @model_validator(mode="after")
    def populate_hash(self) -> "Model":
        """Populate hash after model is validated."""
        if self.hash is None:
            self.hash = model_hash(self)
            self.model_fields_set.add("hash")
        return self


def model_hash(model: Model) -> str:
    """Generate a determinate model hash string.

    Parameters
    ----------
    model
        Instance of a Model.

    Returns
    -------
    model hash
    """
    data = {
        k: v.strip().lower() if isinstance(v, str) else v
        for k, v in model.model_dump(exclude={"hash"}).items()
    }

    serialized = json.dumps(data, sort_keys=True)

    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()
