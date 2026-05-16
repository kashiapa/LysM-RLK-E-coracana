# LysM-RLK Gene Filtering in Eleusine coracana (Finger Millet)

## Project Goal
Identify LysM motif receptor-like kinases (LysM-RLKs) in the *E. coracana* genome using tBLASTn results from potato, wheat and Brachypodium queries.

## Filtering Criteria
- E-value ≤ 1e-5
- % Identity ≥ 70%
- Query coverage ≥ 70%
- etc. (we will expand this)

## Project Structure

LysM_Ecoracana/Scripts
├── Data/
├── Code/
├── Output/
└── README.md


## How to Run
```bash
conda activate your_env
python Code/filter_lysm.py

Author
Kash - May 2026

