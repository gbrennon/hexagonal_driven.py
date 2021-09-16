from dataclasses import dataclass

from hexagonal_driven_py.domain.pokemon.exceptions.validation_error import \
    ValidationError


@dataclass(frozen=True)
class Damage:
    __minimum_value_threshold = 0
    value: int

    def __post_init__(self):
        if self.value < self.__minimum_value_threshold:
            raise ValidationError(f'Damage below {self.__minimum_value_threshold}')
