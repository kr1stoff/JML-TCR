# JML-TCR

NGS TCR 分析项目

## 命令行

```bash
poetry run python main.py -i JML-TCR/template/PBMC240805.xlsx -o result/240809_PBMC240805

snakemake -c 32 -s JML-TCR/wf-igblast/Snakefile --configfile JML-TCR/template/snakemake_config.yaml
```

## 依赖

snakemake 8.16.0

- pandas
- plac=1.4.3
- seaborn
- matplotlib

## 更新

- 0.1.0  
  软件初版，内涵 igblast 分析流程  
  <font color=red>推荐单端测序 (400bp以上) 或 `PE300`, TRB 序列中有没有 overlap (有gap) 分析会失败</font>
