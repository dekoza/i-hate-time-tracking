# I Hate Time Tracking

[comment]: <> ([![ci]&#40;https://github.com/dekoza/i-hate-time-tracking/workflows/ci/badge.svg&#41;]&#40;https://github.com/dekoza/i-hate-time-tracking/actions?query=workflow%3Aci&#41;)

[comment]: <> ([![documentation]&#40;https://img.shields.io/badge/docs-mkdocs%20material-blue.svg?style=flat&#41;]&#40;https://dekoza.github.io/i-hate-time-tracking/&#41;)

[comment]: <> ([![pypi version]&#40;https://img.shields.io/pypi/v/i-hate-time-tracking.svg&#41;]&#40;https://pypi.org/project/i-hate-time-tracking/&#41;)

[comment]: <> ([![gitter]&#40;https://badges.gitter.im/join%20chat.svg&#41;]&#40;https://gitter.im/i-hate-time-tracking/community&#41;)

Get time tracking out of your way.

## Requirements

I Hate Time Tracking requires Python 3.8 or above.

<details>
<summary>To install Python 3.8, I recommend using <a href="https://github.com/pyenv/pyenv"><code>pyenv</code></a>.</summary>

```bash
# install pyenv
git clone https://github.com/pyenv/pyenv ~/.pyenv

# setup pyenv (you should also put these three lines in .bashrc or similar)
export PATH="${HOME}/.pyenv/bin:${PATH}"
export PYENV_ROOT="${HOME}/.pyenv"
eval "$(pyenv init -)"

# install Python 3.8
pyenv install 3.8.12

# make it available globally
pyenv global system 3.8.12
```
</details>

## Installation

With `pip`:
```bash
python3.8 -m pip install i-hate-time-tracking
```

With [`pipx`](https://github.com/pipxproject/pipx):
```bash
python3.8 -m pip install --user pipx

pipx install --python python3.8 i-hate-time-tracking
```
