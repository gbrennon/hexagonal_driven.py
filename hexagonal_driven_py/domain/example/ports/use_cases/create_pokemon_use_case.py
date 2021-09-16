from abc import ABC, abstractmethod

from hexagonal_driven_py.domain.example.dtos.create_foo_dto import CreatePokemonDTO


class CreatePokemonUseCase(ABC):
    @abstractmethod
    def execute(self, create_pokemon_dto: CreatePokemonDTO) -> None:
        pass
