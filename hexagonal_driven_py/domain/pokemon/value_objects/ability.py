from dataclasses import dataclass

from hexagonal_driven_py.domain.pokemon.exceptions.validation_error import (
    ValidationError,
)


@dataclass(frozen=True)
class Ability:
    name: str  # topdo: implement name value object
    damage: float  # todo: implement Damage value object
    # todo element v.o.
