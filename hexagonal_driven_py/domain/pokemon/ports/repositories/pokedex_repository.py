from abc import ABC, abstractmethod
from uuid import UUID

from hexagonal_driven_py.domain.pokemon.entities.pokedex import Pokedex


class PokedexRepository(ABC):
    @abstractmethod
    def get_by_id(self, pokedex_id: UUID):
        pass

    @abstractmethod
    def save(self, pokedex: Pokedex):
        pass
