import pytest

from counter.service import DistributedCounter


@pytest.fixture
def distcounter() -> DistributedCounter:
    return DistributedCounter()


def test_initialise_counter(distcounter: DistributedCounter) -> None:
    assert distcounter is not None
    assert distcounter.get() == 0


def test_default_increment(distcounter: DistributedCounter) -> None:
    distcounter.increment()
    assert distcounter.get() == 1


def test_custom_increment(distcounter: DistributedCounter) -> None:
    distcounter.increment(10)
    assert distcounter.get() == 10


def test_default_decrement(distcounter: DistributedCounter) -> None:
    distcounter.decrement()
    assert distcounter.get() == -1


def test_custom_decrement(distcounter: DistributedCounter) -> None:
    distcounter.decrement(10)
    assert distcounter.get() == -10


def test_reset(distcounter: DistributedCounter) -> None:
    distcounter.decrement(10)
    assert distcounter.get() == -10
    distcounter.reset()
    assert distcounter.get() == 0


def test_multiple_increments(distcounter: DistributedCounter) -> None:
    distcounter.increment(4)
    assert distcounter.get() == 4
    distcounter.increment(10)
    assert distcounter.get() == 14
    distcounter.increment(100)
    assert distcounter.get() == 114


def test_multiple_decrements(distcounter: DistributedCounter) -> None:
    distcounter.increment(100)
    distcounter.decrement(4)
    assert distcounter.get() == 96
    distcounter.decrement(10)
    assert distcounter.get() == 86
    distcounter.decrement(100)
    assert distcounter.get() == -14


def test_multiple_operations(distcounter: DistributedCounter) -> None:
    distcounter.increment(100)
    distcounter.decrement(4)
    assert distcounter.get() == 96
    distcounter.reset()
    assert distcounter.get() == 0
    distcounter.increment(1000)
    assert distcounter.get() == 1000


def test_increment_amount_must_be_positive(distcounter: DistributedCounter) -> None:
    with pytest.raises(ValueError, match="amount must be >=1, got "):
        distcounter.increment(-10)


def test_increment_amount_cannot_be_zero(distcounter: DistributedCounter) -> None:
    with pytest.raises(ValueError, match="amount must be >=1, got "):
        distcounter.increment(0)


def test_decrement_amount_must_be_positive(distcounter: DistributedCounter) -> None:
    with pytest.raises(ValueError, match="amount must be >=1, got "):
        distcounter.decrement(-10)


def test_decrement_amount_cannot_be_zero(distcounter: DistributedCounter) -> None:
    with pytest.raises(ValueError, match="amount must be >=1, got "):
        distcounter.decrement(0)
