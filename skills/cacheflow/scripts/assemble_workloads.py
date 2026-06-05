#!/usr/bin/env python3
"""Batch-assemble cache workload sources into machine-code and listing files."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SIM = ROOT / "sim"
DEFAULT_NAMES = ("mma", "mmb", "mmc", "array_seq", "array_rand")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--names",
        default=",".join(DEFAULT_NAMES),
        help="Comma-separated workload names without the test_ prefix.",
    )
    parser.add_argument(
        "--output-root",
        default=str(SIM),
        help="Directory receiving mem/ and listings/ outputs.",
    )
    args = parser.parse_args()

    names = [name.strip() for name in args.names.split(",") if name.strip()]
    output_root = Path(args.output_root)
    mem_dir = output_root / "mem"
    listing_dir = output_root / "listings"
    assembler = SIM / "tools" / "rv32i_asm.py"
    mem_dir.mkdir(parents=True, exist_ok=True)
    listing_dir.mkdir(parents=True, exist_ok=True)

    for name in names:
        source = SIM / "asm" / f"test_{name}.S"
        if not source.exists():
            raise SystemExit(f"Missing workload source: {source}")
        subprocess.run(
            [
                "python3",
                str(assembler),
                str(source),
                str(mem_dir / f"program_{name}.mem"),
                str(listing_dir / f"listing_{name}.lst"),
            ],
            check=True,
        )
        print(f"Assembled {name}")

    print(f"Generated {len(names)} program images in {output_root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
