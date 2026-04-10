class DistributedCounter:
    def __init__(self) -> None:
        self.__value: int = 0

    def increment(self, amount: int = 1) -> None:
        if amount < 1:
            raise ValueError(f"amount must be >=1, got {amount}")
        self.__value += amount

    def decrement(self, amount: int = 1) -> None:
        if amount < 1:
            raise ValueError(f"amount must be >=1, got {amount}")
        self.__value -= amount

    def reset(self) -> None:
        self.__value = 0

    def get(self) -> int:
        return self.__value
