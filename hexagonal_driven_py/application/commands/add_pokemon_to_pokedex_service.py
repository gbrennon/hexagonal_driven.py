from hexagonal_driven_py.domain.pokemon.ports.repositories.pokedex_repository import (
    PokedexRepository,
)
from hexagonal_driven_py.domain.pokemon.dtos.add_pokemon_to_pokedex.add_pokemon_to_pokedex_output_dto import (
    AddPokemonToPokedexOutputDTO,
)
from hexagonal_driven_py.domain.pokemon.dtos.add_pokemon_to_pokedex.add_pokemon_to_pokedex_input_dto import (
    AddPokemonToPokedexInputDTO,
)
from hexagonal_driven_py.domain.pokemon.ports.use_cases.add_pokemon_to_pokedex_use_case import (
    AddPokemonToPokedexUseCase,
)


class AddPokemonToPokedexService(AddPokemonToPokedexUseCase):
    __pokedex_repository: PokedexRepository

    def execute(self, dto: AddPokemonToPokedexInputDTO) -> AddPokemonToPokedexOutputDTO:
        pokedex = self.__pokedex_repository.get_by_id(dto.pokedex_id)
        pokedex.register(dto.breed)
        self.__pokedex_repository.save(pokedex)

        return AddPokemonToPokedexOutputDTO.from_entity(pokedex)
