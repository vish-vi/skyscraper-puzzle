A Python program that solves Skyscraper puzzles using constraint satisfaction and backtracking.

The puzzle consists of an N×N grid where each row and column must contain the numbers 1 through N exactly once. 
Edge clues indicate how many buildings are visible from a given direction.

Supports arbitrary puzzle sizes
Uses permutation generation to create candidate columns
Applies top and bottom clue filtering
Uses recursive backtracking to construct valid solutions
Validates left and right visibility constraints

Generate all possible column permutations.
Filter columns using top and bottom visibility clues.
Build the grid column by column.
Eliminate invalid configurations early using prefix checks.
Verify all visibility constraints once a complete solution is found.
