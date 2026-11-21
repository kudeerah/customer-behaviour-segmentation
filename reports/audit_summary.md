
# Data Audit Summary

## Dataset Overview
- Original records: 541,909
- Original columns: 8
- Missing CustomerIDs: 135,080
- Missing Descriptions: 1,454
- Duplicate records: 5,268
- Non-positive quantities: 10,624
- Non-positive unit prices: 2,517

## Cleaning Process

| Cleaning Stage | Remaining Records |
|---|---:|
| Original dataset | 541,909 |
| After removing duplicates | 536,641 |
| After removing missing CustomerIDs | 401,604 |
| After removing non-positive sales | 392,692 |

Total records removed: 149,217.

## Cleaning Decisions
1. Removed duplicate records.
2. Removed records without CustomerIDs.
3. Excluded records with non-positive quantities.
4. Excluded records with non-positive unit prices.
5. Calculated TotalAmount as Quantity multiplied by UnitPrice.

Missing Descriptions were retained because they were not required for the RFM calculations.

## Limitation
Negative quantities were excluded. Therefore, Monetary represents
positive sales only and does not deduct returns.

## Final Dataset
- Remaining records: 392,692
- Unique customers: 4,338
- Total positive sales: £8,887,208.89
