import pytest

from sample.placeholder import Sample


def test_Sample_init():
    sample = Sample()

    assert isinstance(sample, Sample)


# intentionally don't test this method to avoid 100% test coverage
# def test_Sample_sample_0():
#     pass


def test_Sample_sample_1():
    sample = Sample()
    assert sample.sample_1() == "Sample"


@pytest.mark.parametrize(
    "input_x",
    [
        pytest.param(5, id="positive"),
        pytest.param(-5, id="negative"),
        pytest.param(0, id="zero"),
    ],
)
def test_Sample_sample_2(input_x):
    # Arrange
    sample = Sample()

    # Act
    result = sample.sample_2(x=input_x)

    # Assert
    assert min(0, input_x) <= result <= max(0, input_x)
