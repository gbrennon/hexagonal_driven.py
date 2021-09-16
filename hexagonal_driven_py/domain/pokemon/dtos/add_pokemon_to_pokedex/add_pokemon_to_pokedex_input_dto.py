from __future__ import annotations

from dataclasses import dataclass
from typing import Dict
from uuid import UUID


@dataclass
class AddPokemonToPokedexInputDTO:
    pokedex_id: UUID
    breed: Breed

    @classmethod
    def from_data(cls, data: Dict) -> AddPokemonToPokedexInputDTO:
        return cls(**data)
