<!---
SPDX-FileCopyrightText: Copyright (c) 2024-2026 Almaz Ilaletdinov <a.ilaletdinov@yandex.ru>
SPDX-License-Identifier: MIT
--->

# flake8-no-json

[![Build Status](https://github.com/blablatdinov/flake8-no-json/workflows/test/badge.svg?branch=master&event=push)](https://github.com/blablatdinov/flake8-no-json/actions?query=workflow%3Atest)
[![codecov](https://codecov.io/gh/blablatdinov/flake8-no-json/branch/master/graph/badge.svg)](https://codecov.io/gh/blablatdinov/flake8-no-json)
[![Python Version](https://img.shields.io/pypi/pyversions/flake8-no-json.svg)](https://pypi.org/project/flake8-no-json/)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

## Background

This is a Flake8 plugin that prevents the use of the standard json package in Python code.
The intent is to enforce the use of an alternative JSON handling library, such as ujson,
orjson, or any other specified by your project guidelines.

## Installation

To install `flake8-no-json`, you can use `pip`:

```bash
pip install flake8-no-json
```

## Usage

Once installed, the plugin will automatically be used when running Flake8. There is no additional configuration required.

Run Flake8 as you normally would:

```bash
flake8 your_project/
```

The plugin will raise an error whenever it detects an import of the json package:

```python
import json  # FJ001: Usage of the 'json' package is not allowed.
```

## License

[MIT](https://github.com/blablatdinov/flake8-no-json/blob/master/LICENSE)


## Credits

This project was generated with [`wemake-python-package`](https://github.com/wemake-services/wemake-python-package). Current template version is: [9899cb192f754a566da703614227e6d63227b933](https://github.com/wemake-services/wemake-python-package/tree/9899cb192f754a566da703614227e6d63227b933). See what is [updated](https://github.com/wemake-services/wemake-python-package/compare/9899cb192f754a566da703614227e6d63227b933...master) since then.
