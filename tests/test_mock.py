from assert_mock import AnyOfType


class TestAnyOfType:
    def test_with_right_type(self):
        assert AnyOfType(int) == 10

    def test_with_wrong_type(self):
        assert AnyOfType(int) != "10"

    def test_with_multiple_types(self):
        given = AnyOfType(int, str)

        assert given == 10
        assert given == "10"

    def test_with_multiple_wrong_types(self):
        given = AnyOfType(int, str)

        assert given != 10.2
