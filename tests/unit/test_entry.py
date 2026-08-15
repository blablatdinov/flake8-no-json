# SPDX-FileCopyrightText: Copyright (c) 2024-2026 Almaz Ilaletdinov <a.ilaletdinov@yandex.ru>
# SPDX-License-Identifier: MIT

import ast

import pytest

from flake8_no_json.entry import Plugin


@pytest.fixture
def plugin_run():
    """Fixture for easy run plugin."""
    def _plugin_run(code: str) -> list[tuple[int, int, str]]:  # noqa: WPS430
        """Plugin run result."""
        plugin = Plugin(ast.parse(code))
        res = []
        for viol in plugin.run():
            res.append((
                viol[0],
                viol[1],
                viol[2],
            ))
        return res
    return _plugin_run


@pytest.mark.parametrize('import_string', [
    'import json',
    'import json; import os',
    'import json as jsn',
])
def test_wrong(plugin_run, import_string):
    """Test wrong case."""
    got = plugin_run(import_string)

    assert got == [
        (
            1,
            0,
            "NJN100 Usage of the 'json' package is not allowed",
        ),
    ]


@pytest.mark.parametrize('import_string', [
    'import ujson',
    'import orjson',
    'import ujson as json',
    'import ujson as jsn',
])
def test_valid(plugin_run, import_string):
    """Test valid case."""
    got = plugin_run(import_string)

    assert not got
