from abc import ABC, abstractmethod


class CreatePokemonUseCase(ABC):
    @abstractmethod
    def execute(self, create_pokemon_dto: CreatePokemonDTO) -> pass:
        pass
