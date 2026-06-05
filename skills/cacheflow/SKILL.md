---
name: cacheflow
description: Automate cache workload assembly, parameter-exploration preparation, and result summarization for the Pipeline_Cache course project. Use when batch-compiling matrix/array locality tests, generating Vivado Tcl runs for L1 cache parameter combinations, or converting cache experiment CSV files into concise comparison reports.
---

# Cacheflow

Use `scripts/cacheflow.py` from the project root.

## Assemble workloads

Run:

```bash
python3 skills/cacheflow/scripts/assemble_workloads.py
```

This batch-compiles the MMA/MMB/MMC and sequential/random array assembly
sources into `program_*.mem` machine-code images and `.lst` listings.

## Generate parameter-exploration Tcl

Run:

```bash
python3 skills/cacheflow/scripts/cacheflow.py generate --mode all
```

This writes `sim/tools/cacheflow_sweep.tcl`. Open the Vivado project, source the
file in the Tcl Console, then call `cacheflow_run_all`.

Use `--mode single` for the three single-factor groups or `--mode grid` for the
3x3 block-size by associativity experiment.

## Summarize experiment CSV

Run:

```bash
python3 skills/cacheflow/scripts/cacheflow.py summarize
```

This reads `sim/results/cache_results_sweep_combined_current.csv` and writes
`sim/results/cacheflow_summary.md`. Use `--input` and `--output` to select other
paths.

## Checks

- Keep `tb_cache_perf` as the Vivado simulation top.
- Verify every summarized row has `pass=1`.
- Compare cycles, speedup, D-Cache hit rate, and L2 hit rate before selecting a
  preferred configuration.
