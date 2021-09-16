from dataclasses import dataclass

from hexagonal_driven_py.domain.pokemon.exceptions.validation_error import \
    ValidationError


@dataclass(frozen=True)
class Level:
    __minimum_value_threshold = 1
    value: int

    def __post_init__(self):
        if self.value < self.__minimum_value_threshold:
            raise ValidationError(f'Level below {self.__minimum_value_threshold}')
