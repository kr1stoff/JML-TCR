cd /data/mengxf/Project/JML20240730_trb_VDJtools_compare || exit 1
# 原始 reads 数:  ~3.33M
# flash 合并成功: ~1.237M (FanYin-T.extendedFrags.fastq)
/home/mengxf/miniforge3/envs/basic/bin/flash -t 16 -d . -o FanYin-T -m 1 FanYin-T_1.fq.gz FanYin-T_2.fq.gz
/home/mengxf/miniforge3/envs/python3.8/bin/python /data/mengxf/GitHub/kPyScripts/concat_non_overlap_pe_reads/concat.py merge/FanYin-T.notCombined_1.fastq merge/FanYin-T.notCombined_2.fastq -o FanYin-T.mergedPyNNN.fastq
# 合并有无 overlap fasta
cat FanYin-T.mergedPyNNN.fastq FanYin-T.extendedFrags.fastq > FanYin-T.final.fastq
# 转 fasta
seqkit fq2fa FanYin-T.final.fastq > FanYin-T.final.fasta
# 去重
seqkit rmdup -j 16 -s -D dup-num-file -o rmdup.fasta merge/FanYin-T.final.fasta

# igblast
igblastn \
  -germline_db_V /data/mengxf/Database/IMGT/2024.07/Homo_sapiens/TR/igblast/human_TRBV.fa \
  -germline_db_D /data/mengxf/Database/IMGT/2024.07/Homo_sapiens/TR/igblast/human_TRBD.fa \
  -germline_db_J /data/mengxf/Database/IMGT/2024.07/Homo_sapiens/TR/igblast/human_TRBJ.fa \
  -domain_system imgt \
  -organism human \
  -ig_seqtype TCR \
  -auxiliary_data /home/mengxf/miniforge3/envs/basic/share/igblast/optional_file/human_gl.aux \
  -show_translation \
  -outfmt 19 \
  -num_threads 16 \
  -query ../rmdup/rmdup.fasta \
  -out igblast.output.19
