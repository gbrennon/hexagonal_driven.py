# HexagonalDrivenPy

## What is this?

- This is an architectural model, heaviliy inspired by `ports and adapters` pattern(`hexagonal architecture`) mixed with `layers` concept.
- This architecture focus on defining not only the "macro" details(layers) of your software but also the "micro" details(components).
- The main objective of this architecture is to make developers focus more on "solving problems" and less on "where should I put this component?"

## Core concepts:
- `Inversion of control` rules.
- The `domain layer` is the most important thing AT ALL.
- Software components should be described on the `inner-most layer`(`domain`) as `ports`.
- `Components` living in `outer-layers` should be interpreted as `adapters` for the `ports` that were defined in the `domain` layer.
- Before writing code u should design ur solution with ur team.

## Defining the layers

### Domain

- This is the most important layer for this architecture.
- This is, literally, the heart of our software. 
- This layer should define not only the behaviour and shape of our `entities` but also all `ports` that should be implemented in any `outer-layer`.
- How this layer looks like?

#### Components of this layer:

##### DTOs: Data Transfer Objects.

- The DTOs are going to be the description or our boundaries. What our `use cases` are going to use as `input/output`.
```python
class CreateProductDTO:
    name: str
    price: float
```

##### Entities: The living beings

- The entities should be the most tangible abstraction of our domain.
- This should be the lowest level implementation of our code. The business rule at its finest.
- Entities should contain an `id`. Example: 

```python
class Product:
    id: UUID
    name: str
    price: Price

```

##### Value Objects: The worst enemy of the primitives.

- This should represent a significant `value` for ur domain.
- It should contain `self validation` logic!
- Example: Price(16.30)
```python
@dataclass
class Price:
    value: float

    def __post_init__(self):
        self.__validate()

    def __validate(self):
        if self.value < 0:
            raise Exception

```

##### Ports

- This is where we define the interfaces that should be implemented in outer-layers.
- On this approach we should describe everything that will be implemented outside in here.
    - Repositories: This describes the interfaces for the repository pattern implementation
```python
class ProductRepository(ABC):
    @abstractmethod
    def persist(self, product: Product) -> None:
        pass

```
    - Use Cases: This describes the interface for an application service
```python
class CreateProductUseCase(ABC):
    @abstractmethod
    def execute(self, dto: CreateProductDTO) -> None:
        pass

```
    - Services: This describes the interface for a domain service


### Application

#### Components of this layer:


#### Commands

- A `command` is the is the concrete implementation of an `usecase` that should cause `side effects` in the system.

#### Queries

- A `query` is the concrente implementation of an `usecase` that should retrieve data from our system.
