# SPDX-FileCopyrightText: 2024-present Christian Hartung <hartungstenio@outlook.com>
#
# SPDX-License-Identifier: MIT

from typing import Final
from unittest import mock

__all__ = [
    "Any",
    "AnyOfType",
]

Any: Final = mock.ANY


class AnyOfType:
    """Helper that compares based on type."""

    __slots__ = ("types",)

    def __init__(self, *types: type):
        self.types = tuple(types)

    def __eq__(self, value: object) -> bool:
        return isinstance(value, self.types)

    def __repr__(self) -> str:
        types = [typ.__name__ for typ in self.types]
        return f"<AnyOfType({', '.join(types)})>"
