class DistributedCounter:
    def __init__(self) -> None:
        self.__value: int = 0

    def _increment_internal(self, amount: int) -> None:
        self.__value += amount

    def _decrement_internal(self, amount: int) -> None:
        self.__value -= amount

    def _reset_internal(self) -> None:
        self.__value = 0
    
    def increment(self, amount: int = 1) -> None:
        if amount < 1:
            raise ValueError(f"amount must be >=1, got {amount}")
        self._increment_internal(amount)
    
    def decrement(self, amount: int = 1) -> None:
        if amount < 1:
            raise ValueError(f"amount must be >=1, got {amount}")
        self._decrement_internal(amount)

    def reset(self) -> None:
        self._reset_internal()

    def get(self) -> int:
        return self.__value
