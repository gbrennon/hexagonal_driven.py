from abc import ABC, abstractmethod

from hexagonal_driven_py.domain.pokemon.dtos.add_pokemon_to_pokedex.add_pokemon_to_pokedex_input_dto import (
    AddPokemonToPokedexInputDTO,
)
from hexagonal_driven_py.domain.pokemon.dtos.add_pokemon_to_pokedex.add_pokemon_to_pokedex_output_dto import (
    AddPokemonToPokedexOutputDTO,
)


class AddPokemonToPokedexUseCase(ABC):
    @abstractmethod
    def execute(self, dto: AddPokemonToPokedexInputDTO) -> AddPokemonToPokedexOutputDTO:
        pass
