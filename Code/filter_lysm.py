# ================================================
# LysM-RLK Filtering Script
# ================================================

# To get into pyhton
# library(reticulate)
# setwd("C:/Users/kashi/OneDrive/Documents/LysM-RLK/Scripts")
# Import libraries
# import pandas as pd   # This is the main library for data frames in Python

import pandas as pd
import os
import sys

print("Python version:", sys.version.split()[0])
print("Pandas version:", pd.__version__)


# ================================================
# Load the tBLASTn results - Robust method
# ================================================

file_path = "Data/tblastn_results.tsv"

# Method 1: Skip lines that start with '#' (comments and headers)
df = pd.read_csv(file_path, 
                 sep="\t", 
                 comment="#",           # Skip all lines starting with #
                 low_memory=False)

print("\n✅ File loaded successfully (skipping comment lines)!")
print(f"Total number of data rows: {len(df):,}")
print(f"Number of columns: {df.shape[1]}")

print("\nColumn names:")
for i, col in enumerate(df.columns):
    print(f"   {i+1:2d}. {col}")

print("\nFirst 5 rows:")
print(df.head())

print(f"Original rows: {len(df):,}")

# ================================================
# Clean column names (very important)
# ================================================

# Replace spaces and dots with underscores, remove special characters

df.columns = [col.strip().replace(" ", "_").replace(".", "_").replace("%", "percent").lower() 
              for col in df.columns]

print("\nCleaned column names:")
for col in df.columns:
    print(f"   - {col}")
    
    
# ================================================
# Apply initial filters (based on literature cutoffs)
# ================================================

# Convert key columns to numeric

df['evalue'] = pd.to_numeric(df['evalue'], errors='coerce')
df['percent_identity'] = pd.to_numeric(df['percent_identity'], errors='coerce')
df['percent_query_coverage_per_subject'] = pd.to_numeric(df['percent_query_coverage_per_subject'], errors='coerce')

# Apply filters
filtered = df[
    (df['evalue'] <= 1e-5) &
    (df['percent_identity'] >= 70) &
    (df['percent_query_coverage_per_subject'] >= 70)
].copy()

print(f"\n✅ After filtering: {len(filtered):,} hits remain")
print(f"Filtered out {len(df) - len(filtered):,} low-quality hits")

# Show summary of top hits
print("\nTop 10 hits by bit score:")
print(filtered.nlargest(10, 'bit_score')[['query_id', 'subject_id', 'percent_identity', 'evalue', 'bit_score']])

# Save the filtered results
filtered.to_csv("Output/filtered_lysm_hits.tsv", sep="\t", index=False)
print("\n✅ Filtered results saved to Output/filtered_lysm_hits.tsv")
