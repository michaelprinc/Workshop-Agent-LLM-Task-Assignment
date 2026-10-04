# Grade calculator — specification

Workshop starter project: a Python CLI computes weighted student scores from a semicolon-separated CSV and assigns letter grades. Determine its actual behavior yourself and compare it with this specification.

## Required behavior

- Subject weights: `a1` = 0.3, `a2` = 0.3, `praktikum` = 0.4.
- An empty grade is absent, not a numeric score. Use only available grades and renormalize their weights to sum to one.
- A student with no available grades is listed as insufficient data with letter `-`. Reading the provided file must preserve student records without aborting the whole report. Missing trailing grade fields are treated as absent grades.
- Letter grades use inclusive lower bounds: A ≥ 90, B ≥ 80, C ≥ 70, D ≥ 60; otherwise F.
- Averages are rounded to two decimal places. Letter grades use that computed average.
- Non-numeric non-empty grade values are outside the supplied fixture's specification. Report an unsupported input instead of guessing its meaning.
- Input data stays unchanged. Expected values in tests and reports are derived from these requirements, not copied from current program output.

## Running

Use the prepared Python interpreter from this directory:

```bash
python -m src.cli data/znamky.csv
python -m pytest tests/ -v
```

`src/` contains starter code. `tests/` contains a basic import check; it does not establish behavioral correctness. `data/` contains immutable sample input. `docs/` holds working notes and reports.
