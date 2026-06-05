# cacheflow

`cacheflow` 是计算机组成原理课程设计中的轻量级 Agent Skill，用于减少缓存测试与参数探索中的重复操作。

它实现三项自动化功能：

1. 批量编译 MMA/MMB/MMC 和数组顺序/随机访问测试程序，生成机器码和反汇编列表。
2. 根据一级缓存容量、块大小和相联度组合，生成 Vivado 参数探索 Tcl 流程。
3. 读取性能实验 CSV，自动生成包含最优配置和平均指标的 Markdown 汇总报告。

将本仓库中的 `skills/cacheflow/` 放入 `Pipeline_Cache` 工程根目录后运行：

```bash
python3 skills/cacheflow/scripts/assemble_workloads.py
python3 skills/cacheflow/scripts/cacheflow.py generate --mode all
python3 skills/cacheflow/scripts/cacheflow.py summarize
```

生成的主要文件为：

- `sim/tools/cacheflow_sweep.tcl`
- `sim/results/cacheflow_summary.md`
- `sim/mem/program_*.mem` 与 `sim/listings/listing_*.lst`

在 Vivado Tcl Console 中执行参数探索：

```tcl
source sim/tools/cacheflow_sweep.tcl
cacheflow_run_all
```

`generate` 支持 `single`、`grid` 和 `all` 三种模式；`summarize` 可通过 `--input` 和 `--output` 指定其他 CSV 与输出路径。