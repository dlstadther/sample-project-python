# CHANGELOG

<!-- version list -->

## v1.3.1 (2026-09-12)

### Bug Fixes

- **lint**: Exclude nox/venv/cache dirs from interrogate scan
  ([#24](https://github.com/dlstadther/sample-project-python/pull/24),
  [`ff18b38`](https://github.com/dlstadther/sample-project-python/commit/ff18b38a3bcd2bf7501bf5674179ee5ef9e8f931))


## v1.3.0 (2026-09-11)

### Features

- **pyscn**: Add .pyscn.toml config with reasonable defaults
  ([#23](https://github.com/dlstadther/sample-project-python/pull/23),
  [`31b0e3d`](https://github.com/dlstadther/sample-project-python/commit/31b0e3d7f4e4a750a57ba7810376ed2a9da92e01))

- **pyscn**: Integrate pyscn code quality gate into CI
  ([#23](https://github.com/dlstadther/sample-project-python/pull/23),
  [`31b0e3d`](https://github.com/dlstadther/sample-project-python/commit/31b0e3d7f4e4a750a57ba7810376ed2a9da92e01))

### Refactoring

- **pyscn**: Move config into pyproject.toml, trim to essentials
  ([#23](https://github.com/dlstadther/sample-project-python/pull/23),
  [`31b0e3d`](https://github.com/dlstadther/sample-project-python/commit/31b0e3d7f4e4a750a57ba7810376ed2a9da92e01))


## v1.2.1 (2026-09-11)

### Bug Fixes

- **ci**: Trigger docs workflow on push to main
  ([#22](https://github.com/dlstadther/sample-project-python/pull/22),
  [`b71f95f`](https://github.com/dlstadther/sample-project-python/commit/b71f95f54d8d2f0d469da5f707b7e78879af2e22))

### Chores

- **docs**: Replace mkdocs with zensical
  ([#21](https://github.com/dlstadther/sample-project-python/pull/21),
  [`909dd6b`](https://github.com/dlstadther/sample-project-python/commit/909dd6b326a23656f56f8695aeeaa7f2c77d3288))


## v1.2.0 (2026-09-11)

### Features

- **interrogate**: Add docstring coverage checks to prek and lint
  ([#20](https://github.com/dlstadther/sample-project-python/pull/20),
  [`1f3b9c1`](https://github.com/dlstadther/sample-project-python/commit/1f3b9c1942e18b76e6f8177362a3b3de44f1329e))


## v1.1.0 (2026-09-11)

### Chores

- **deps**: Upgrade python dependencies
  ([#19](https://github.com/dlstadther/sample-project-python/pull/19),
  [`992abd9`](https://github.com/dlstadther/sample-project-python/commit/992abd9f16b842e95cfc372aae0a643b78ae5835))

### Documentation

- Add tooling TODOs
  ([`f948d56`](https://github.com/dlstadther/sample-project-python/commit/f948d56ca26a4eb47927838cc04b75324e6e8335))

### Features

- **nox**: Support multi-version testing and pytest posargs
  ([`1e9ab2f`](https://github.com/dlstadther/sample-project-python/commit/1e9ab2f91fa8147d39c49e83229073c86f9c11d8))


## v1.0.2 (2026-09-11)

### Bug Fixes

- **type-check**: Pin pyrefly-pre-commit to a stable release
  ([#18](https://github.com/dlstadther/sample-project-python/pull/18),
  [`c4b1678`](https://github.com/dlstadther/sample-project-python/commit/c4b1678f1ef61875328a4ec0e6cf31082329bc32))

- **type-check**: Use the official pyrefly pre-commit hook
  ([#18](https://github.com/dlstadther/sample-project-python/pull/18),
  [`c4b1678`](https://github.com/dlstadther/sample-project-python/commit/c4b1678f1ef61875328a4ec0e6cf31082329bc32))

### Chores

- **type-check**: Switch static type checking from ty to pyrefly
  ([#18](https://github.com/dlstadther/sample-project-python/pull/18),
  [`c4b1678`](https://github.com/dlstadther/sample-project-python/commit/c4b1678f1ef61875328a4ec0e6cf31082329bc32))

### Refactoring

- **type-check**: Drop stale type: ignore now unneeded by pyrefly
  ([#18](https://github.com/dlstadther/sample-project-python/pull/18),
  [`c4b1678`](https://github.com/dlstadther/sample-project-python/commit/c4b1678f1ef61875328a4ec0e6cf31082329bc32))


## v1.0.1 (2026-01-18)

### Bug Fixes

- Typo in semantic-release config
  ([#17](https://github.com/dlstadther/sample-project-python/pull/17),
  [`0ece801`](https://github.com/dlstadther/sample-project-python/commit/0ece801b969b6256d88aa5b9949580e9c30abe7d))


## v1.0.0 (2026-01-18)

- Initial Release

## v1.0.0-rc.5 (2026-01-18)

### Bug Fixes

- Attempt to use action for release
  ([`dc8fe56`](https://github.com/dlstadther/sample-project-python/commit/dc8fe561c1b7bc621c45db8ed5b83a6b90d9df4d))

- Ensure uv is still available to support build_command
  ([`c743f9e`](https://github.com/dlstadther/sample-project-python/commit/c743f9ea35ffaf3c2aa775d64137a0cf7a1db03c))

- Include checkout
  ([`53b6f72`](https://github.com/dlstadther/sample-project-python/commit/53b6f726114d9edce3156aa814b897a3c34dce95))

- Revert semantic-release to make version; updates token to GH_TOKEN
  ([`26633eb`](https://github.com/dlstadther/sample-project-python/commit/26633eb756bda5b9c20d0ddf51ed1906ba331ce5))


## v1.0.0-rc.4 (2026-01-14)

### Bug Fixes

- Attempt workflow permission
  ([`bdc2a63`](https://github.com/dlstadther/sample-project-python/commit/bdc2a631b0bc8e5580a061f463c60216d1090901))

- Attempting pr write permission given github discussion comment
  ([`c755c4b`](https://github.com/dlstadther/sample-project-python/commit/c755c4b2745bc4e0d6db79f64d77d9c0b0fc3fb9))


## v1.0.0-rc.3 (2026-01-14)

### Bug Fixes

- Github token permissions
  ([`198dfc1`](https://github.com/dlstadther/sample-project-python/commit/198dfc122492d27210f9d428745e7388017cf6e6))


## v1.0.0-rc.2 (2026-01-13)

### Bug Fixes

- Allow github action token to create release
  ([`b735f71`](https://github.com/dlstadther/sample-project-python/commit/b735f714412aa0028ce793892af2c434d01d5202))


## v1.0.0-rc.1 (2026-01-13)

- Initial Release
