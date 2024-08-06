# JML-TCR

NGS TCR 分析项目

## 依赖

Python 3.8.19

- click
- pandas
- seaborn
- matplotlib

## tools

### concat_non_overlap_pe_reads.py

TCR PE150 没有 overlap 的双端 fastq 合并脚本

  ```bash
  flash -t 16 -d . -o FanYin-T -m 10 FanYin-T_1.fq.gz FanYin-T_2.fq.gz
  
  python concat_non_overlap_pe_reads.py -o FanYin-T.mergedPyNNN.fastq FanYin-T.notCombined_1.fastq FanYin-T.notCombined_2.fastq
  ```

### add_cdr3_num.py

原始 fastq 数据使用 seqkit rmdup 去重, 经过 igblast 比对后, 再将数量信息添加回去

  ```bash
  igblastn \
    -germline_db_V Database/IMGT/2024.07/Homo_sapiens/TR/igblast/human_TRBV.fa \
    -germline_db_D Database/IMGT/2024.07/Homo_sapiens/TR/igblast/human_TRBD.fa \
    -germline_db_J Database/IMGT/2024.07/Homo_sapiens/TR/igblast/human_TRBJ.fa \
    -domain_system imgt \
    -organism human \
    -ig_seqtype TCR \
    -auxiliary_data miniforge3/envs/basic/share/igblast/optional_file/human_gl.aux \
    -show_translation \
    -outfmt 19 \
    -num_threads 16 \
    -query rmdup.fasta \
    -out igblast.output.19

  # 保留注释到CDR3的信息
  csvtk -t filter2 -f '$cdr3!=""' igblast.output.19 > igblast.output.19.cdr3
  
  # 给 output.19 添加num信息
  python add_cdr3_num.py -i igblast.output.19.cdr3 -d rmdup/dup-num.txt
  ```

### calc_freq_and_filter.py

过滤加过数量的 igblast cdr3 表格, 合并相同 cdr3 的条目  
使用到的列 num v_call d_call j_call cdr3 cdr3_aa

1. 过滤
    - len(cdr3) < 20, 20 bp 以下的 cdr3 条目
    - 'N' in cdr3, 含 N 碱基的条目

   凯杰 PPT 从 cdr3 长度 20bp - 80bp 作图
   (claude) 对于TCR, TCR β链: 通常在9-15个氨基酸之间
2. 合并
    - vdj 删除等位基因信息 (\*01, \*02)
    - 根据 cdr3 序列合并条目

```bash
python calc_freq_and_filter.py add_cdr3_num.txt
```

### cdr3_heatmap.py

根据 cdr3 stats.tsv 文件, 统计 V/J 基因作热图

```bash
python /data/mengxf/GitHub/JML-TCR/tools/cdr3_heatmap.py stats.tsv
```

### cdr3_displot.py

根据 cdr3 stats.tsv 文件, 统计 cdr3 长度作分布图

```bash
python /data/mengxf/GitHub/JML-TCR/tools/cdr3_displot.py stats.tsv
```
