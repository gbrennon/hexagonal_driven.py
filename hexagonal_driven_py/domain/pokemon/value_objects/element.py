from dataclasses import dataclass

from hexagonal_driven_py.domain.pokemon.value_objects.element_enum import ElementEnum


@dataclass
class Element:
    value: str

    def __post_init__(self):
        if self.value and not hasattr(ElementEnum, self.value):
            raise Exception(f'Invalid Pokemón element: {self.value}.')
