cd /data/mengxf/Project/JML20240730_trb_VDJtools_compare || exit 1
# 原始 reads 数:  ~3.33M
# flash 合并成功: ~1.237M (FanYin-T.extendedFrags.fastq)
/home/mengxf/miniforge3/envs/basic/bin/flash -t 16 -d . -o FanYin-T -m 1 FanYin-T_1.fq.gz FanYin-T_2.fq.gz
