# The MIT License (MIT)
#
# Copyright (c) 2024 blablatdinov
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
# OR OTHER DEALINGS IN THE SOFTWARE.

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
