
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

PROJECT = Path(__file__).resolve().parent

# Project files
files = [
    "original_app.py",
    "optimized_app.py",
    "benchmark.py",
    "profiler.py",
    "test_application.py",
    "generate_report.py",
    "README.md",
    "requirements.txt",
    "benchmark_results.txt",
    "original_profile.txt",
    "optimized_profile.txt"
]

# Detailed project report
report = """
WEEK 4 TASK
PERFORMANCE OPTIMIZATION IN PYTHON APPLICATIONS

==================================================
1. INTRODUCTION
==================================================

The objective of this project is to improve the performance
of a Python application by identifying bottlenecks,
implementing optimization techniques, and comparing
execution efficiency before and after optimization.

The project implements a sales data processing application.

It calculates total sales, category-wise sales, average
prices, and duplicate records.

==================================================
2. ORIGINAL APPLICATION
==================================================

The original application processes records using multiple
loops and repeated dataset scanning.

The main operations include:

- Total sales calculation.
- Category-wise sales calculation.
- Duplicate record detection.
- Average price calculation.

==================================================
3. IDENTIFIED PERFORMANCE BOTTLENECKS
==================================================

The following bottlenecks were identified:

1. Repeated category searches:
   The application scans the entire dataset separately
   for each category.

2. Nested loops:
   Duplicate detection uses nested loops, resulting in
   quadratic time complexity.

3. Repeated computations:
   Multiple operations traverse the same dataset.

4. Inefficient processing:
   The original implementation performs unnecessary
   repeated operations.

==================================================
4. OPTIMIZATION TECHNIQUES
==================================================

The following techniques were implemented:

1. Single-pass processing:
   All major calculations are performed in one traversal.

2. Dictionary-based aggregation:
   Category sales are calculated using dictionaries.

3. Set-based duplicate detection:
   Sets provide efficient average-case membership checks.

4. Reduced redundant computations:
   Intermediate values are calculated once and reused.

==================================================
5. PERFORMANCE BENCHMARK RESULTS
==================================================

The benchmark was conducted using Python's timeit module.

Original execution time:
5.722401 seconds

Optimized execution time:
0.007529 seconds

Execution time improvement:
99.87 percent

Memory measurements using tracemalloc:

Original peak memory:
0.46 KB

Optimized peak memory:
640.58 KB

Memory analysis:

The optimized application uses additional memory because
it maintains a set for efficient duplicate detection.

This represents a trade-off between memory consumption
and execution speed.

==================================================
6. PROFILING ANALYSIS
==================================================

Python's cProfile module was used to inspect function
execution times and identify computational bottlenecks.

Original profiling results are stored in:
original_profile.txt

Optimized profiling results are stored in:
optimized_profile.txt

The profiling data can be used to compare function calls
and cumulative execution times.

==================================================
7. FUNCTIONAL VERIFICATION
==================================================

Automated tests were executed using Python unittest.

The tests verify:

- Total sales calculation.
- Average price calculation.
- Identical results between both applications.
- Empty dataset handling.

All four automated tests passed.

This confirms that the optimized application maintains
the expected functionality for the tested cases.

==================================================
8. CONCLUSION
==================================================

The project successfully demonstrates Python performance
optimization.

The original application required 5.722401 seconds,
whereas the optimized application required only
0.007529 seconds.

The measured execution time improved by approximately
99.87 percent.

The optimized implementation uses additional memory,
but significantly reduces processing time.

The project demonstrates the importance of algorithmic
efficiency, suitable data structures, profiling tools,
and automated testing in Python development.

==================================================
END OF REPORT
==================================================
"""

# Save report
report_path = PROJECT / "Performance_Optimization_Report.txt"

report_path.write_text(report, encoding="utf-8")

# Create ZIP archive
archive = PROJECT / "Week4_Performance_Optimization.zip"

missing_files = []

with ZipFile(archive, "w", ZIP_DEFLATED) as zip_file:

    for filename in files + ["Performance_Optimization_Report.txt"]:

        path = PROJECT / filename

        if path.exists():
            zip_file.write(path, arcname=filename)
        else:
            missing_files.append(filename)

print("\nPROJECT REPORT GENERATED")
print("------------------------")
print("Report:", report_path.name)

print("\nZIP ARCHIVE CREATED")
print("-------------------")
print("Archive:", archive.name)

if missing_files:
    print("\nWARNING - Missing files:")
    for filename in missing_files:
        print("-", filename)
else:
    print("All project files included successfully.")

print("\nPerformance Improvement: 99.87%")
print("Project generation completed.")
