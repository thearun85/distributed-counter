from pysyncobj import SyncObj, replicated


class DistributedCounter(SyncObj):  # type: ignore[misc]
    def __init__(self, self_address: str, partner_addresses: list[str]) -> None:
        super().__init__(self_address, partner_addresses)
        self.__value: int = 0

    @replicated
    def _increment_internal(self, amount: int) -> None:
        self.__value += amount

    @replicated
    def _decrement_internal(self, amount: int) -> None:
        self.__value -= amount

    @replicated
    def _reset_internal(self) -> None:
        self.__value = 0

    def increment(self, amount: int = 1) -> None:
        if amount < 1:
            raise ValueError(f"amount must be >=1, got {amount}")
        self._increment_internal(amount, sync=True)

    def decrement(self, amount: int = 1) -> None:
        if amount < 1:
            raise ValueError(f"amount must be >=1, got {amount}")
        self._decrement_internal(amount, sync=True)

    def reset(self) -> None:
        self._reset_internal(sync=True)

    def get(self) -> int:
        return self.__value

    def wait_until_ready(self, timeout: float = 5.0) -> bool:
        import time

        deadline = time.monotonic() + timeout
        while time.monotonic() < deadline:
            if self.isReady():
                return True
            time.sleep(0.1)
        return False
