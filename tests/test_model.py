"""Model tests."""

from automatics import Model


def test__deterministic_hash() -> None:
    """Test whether Model hash is deterministic."""
    model1 = Model(
        program="foo",
        program_version="bar",
        calc_type="baz",
        method="qux",
        basis="quux",
    )

    model2 = Model(
        program="FOO",
        program_version="BAR",
        calc_type="BAZ",
        method="QUX",
        basis="QUUX",
    )

    assert model2.hash == model1.hash

    model3 = Model(program="foo", calc_type="baz", method="qux", basis="quux")

    assert model3.hash != model1.hash

    model4 = Model(program="foo", program_version="bar", calc_type="baz", method="baz")

    assert model4.hash != model1.hash

    model5 = Model(program="foo", calc_type="baz", method="qux")

    assert model5.hash != model1.hash
