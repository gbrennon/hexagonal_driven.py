from __future__ import annotations

from dataclasses import dataclass


@dataclass
class AddPokemonToPokedexOutputDTO:
    @classmethod
    def from_entity(cls, entity) -> AddPokemonToPokedexOutputDTO:
        return cls(entity.name)
