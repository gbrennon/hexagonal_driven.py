from dataclasses import dataclass

from hexagonal_driven_py.domain.pokemon.exceptions.validation_error import \
    ValidationError


@dataclass(frozen=True)
class Name:
    value: str
    __minimum_name_length_threshold: int = 3

    def __post_init__(self):
        if self.value == "":
            raise ValidationError("Name cannot be empty")
        
        if len(self.value) < self.__minimum_name_length_threshold:
            raise ValidationError(f"Name must be at least {self.__minimum_name_length_threshold} characters long.")

        invalid_name = next((name for name in self.value.split() if name[0] != name[0].upper()), None)
        if invalid_name:
            raise ValidationError(f"Name {invalid_name} must start with an upper case character.")
