# SPDX-FileCopyrightText: Copyright (c) 2024-2026 Almaz Ilaletdinov <a.ilaletdinov@yandex.ru>
# SPDX-License-Identifier: MIT

# flake8: noqa: WPS232, WPS226

import ast
from collections.abc import Generator
from typing import final


@final
class ImportVisitor(ast.NodeVisitor):
    """Class visitor for checking importing json package."""

    def __init__(self) -> None:
        """Ctor."""
        self.problems: list[int] = []

    def visit_Import(self, node) -> None:
        """Visit by classes."""
        if node.names[0].name == 'json':
            self.problems.append(node.lineno)
        self.generic_visit(node)


@final
class Plugin:
    """Flake8 plugin."""

    def __init__(self, tree) -> None:
        """Ctor."""
        self._tree = tree

    def run(self) -> Generator[tuple[int, int, str, type], None, None]:
        """Entry."""
        visitor = ImportVisitor()
        visitor.visit(self._tree)
        for line in visitor.problems:  # noqa: WPS526
            yield (line, 0, "NJN100 Usage of the 'json' package is not allowed", type(self))
