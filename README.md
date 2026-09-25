# Python Risk & Position Size Calculator

A beginner Python command-line project that calculates a risk budget, stop-loss distance, and whole-share position size from user inputs. Built to practise Python fundamentals through a practical maths problem.

## Features

- Accepts account size, risk percentage, entry price, and stop-loss price.
- Calculates the stop-loss distance as a percentage of entry price.
- Limits the calculated position to the available account balance.
- Rounds the share count down to whole shares.
- Displays the position value and planned risk after rounding.
- Checks numeric values for a positive account balance, risk above 0% and at most 100%, and a positive stop-loss below entry.

## How to Run

Requires Python 3.6 or newer. No external packages are needed.

1. Save the calculator code as `risk_calculator.py`.
2. Open a terminal in the folder containing the file.
3. Run:

```bash
python3 risk_calculator.py
```

If your Python installation uses `python` instead, run `python risk_calculator.py`.

4. Enter numbers when prompted. Enter `1` for 1%, without a percent sign. Do not include currency symbols or commas.

## Example

Fictional inputs used to demonstrate the calculation:

| Input | Value |
| --- | ---: |
| Account size | 10000 |
| Risk per trade (%) | 1 |
| Entry price | 50 |
| Stop-loss price | 48 |

Output:

```text
Stop-loss distance: 4.00%
Risk budget: $100.00
Number of shares: 50
Position value: $2500.00
Planned risk at stop-loss: $100.00
```

## Calculations

```text
Stop-loss percentage = ((Entry price - Stop-loss price) / Entry price) × 100
Risk budget = Account size × (Risk percentage / 100)
Position size before balance limit = Risk budget / (Stop-loss percentage / 100)
Limited position size = minimum(Position size before balance limit, Account size)
Whole shares = round down(Limited position size / Entry price)
Position value = Whole shares × Entry price
Planned risk = Whole shares × (Entry price - Stop-loss price)
```

The account risk percentage and stop-loss percentage are different: one measures the risk budget relative to the account; the other measures the price drop from entry. Rounding and the balance limit can make planned risk smaller than the risk budget.

## Python Concepts Practised

- User input with `input()`
- Numeric conversion with `float()` and `int()`
- Variables and arithmetic operators
- Input validation with `if`, `elif`, and `else`
- Limiting values with `min()`
- Formatted output using f-strings and `:.2f`

## Limitations

- Supports buying whole shares only; no short positions, fractional shares, or borrowing.
- Treats the entered account size as available cash and does not account for existing positions.
- Assumes all monetary inputs use the same currency; the dollar sign is only an output label.
- Excludes fees, price gaps, and differences between the stop price and actual execution price. Planned risk is not a guaranteed maximum loss.
- Blank or non-numeric input currently raises an error.
- Uses floating-point arithmetic, which can produce small precision differences.

This is an educational programming project, not a trading recommendation or brokerage tool.

## Possible Improvements

- Handle non-numeric input with `try` and `except`.
- Allow another calculation without restarting the program.
- Organise calculations into functions.
- Add tests for invalid inputs, rounding, and balance limits.

## Development

Developed as a beginner Python learning project.
