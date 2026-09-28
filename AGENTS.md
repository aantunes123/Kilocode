# AGENTS.md

## Project Overview
Simple Python plotting script using NumPy and Matplotlib. Configuration is separated into `config.py`.

## Commands
- **Run**: `python test.py`
- **Dependencies**: `numpy`, `matplotlib` (install via `pip install numpy matplotlib`)

## Structure
- `test.py` — Entry point, contains `plot_quadratic()` function
- `config.py` — All plot parameters (range, appearance, labels, power)

## Conventions
- Configuration values in `config.py` are imported as module attributes
- Function parameters default to config values for easy override
- No test suite, linting, or type checking configured