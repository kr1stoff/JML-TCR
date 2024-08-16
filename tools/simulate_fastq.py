#!/usr/bin/env python
"""
@Time ： 2024/8/12 下午2:17
@Auth ： kristoff
@File ：simulate_fastq.py
@IDE ：PyCharm
@Motto ：Continuous learning
@LastModified : 2024/8/12 下午2:17
"""
from pathlib import Path
import time
from multiprocessing import Pool

from Bio import SeqIO
from Bio.Seq import Seq

# # trb 序列模拟
# 100% 200k         (total 2.4M)
num_per_seq = 200000
gradient = '1_150'
num_negative_read = 0
fastq1_negative = ''
fastq2_negative = ''

# 10^(-3)   200     (total 2.4M)
# num_per_seq = 200
# num_negative_read = 2397600
# gradient = '103'
# fastq1_negative = '/data/mengxf/Software/neoimmune/AutoMRD-1.0.1.2024-07-15_release/Rawdata/PBMC240805/NI240729N01-9-46_L2_1.fq.gz'
# fastq2_negative = '/data/mengxf/Software/neoimmune/AutoMRD-1.0.1.2024-07-15_release/Rawdata/PBMC240805/NI240729N01-9-46_L2_2.fq.gz'

# 10^(-4)   20      (total 2.4M)
# num_per_seq = 20
# num_negative_read = 2399760
# gradient = '104'
# fastq1_negative = '/data/mengxf/Software/neoimmune/AutoMRD-1.0.1.2024-07-15_release/Rawdata/PBMC240805/NI240729N01-9-46_L2_1.fq.gz'
# fastq2_negative = '/data/mengxf/Software/neoimmune/AutoMRD-1.0.1.2024-07-15_release/Rawdata/PBMC240805/NI240729N01-9-46_L2_2.fq.gz'

# 10^(-5)   5     (total 6M)
# num_per_seq = 5
# num_negative_read = 5999940
# gradient = '105'
# fastq1_negative = '/data/mengxf/Project/JML20240731_trb_synthesized_sequence/fastq/NI240729N01_12M_rename.1.fastq.gz'
# fastq2_negative = '/data/mengxf/Project/JML20240731_trb_synthesized_sequence/fastq/NI240729N01_12M_rename.2.fastq.gz'

# 10^(-6)   1     (total 12M)
# num_per_seq = 1
# num_negative_read = 11999988
# gradient = '106'
# fastq1_negative = '/data/mengxf/Project/JML20240731_trb_synthesized_sequence/fastq/NI240729N01_12M_rename.1.fastq.gz'
# fastq2_negative = '/data/mengxf/Project/JML20240731_trb_synthesized_sequence/fastq/NI240729N01_12M_rename.2.fastq.gz'

# main
outdir = Path(f'/data/mengxf/Project/JML20240731_trb_synthesized_sequence/fastq/{gradient}')
outdir.mkdir(exist_ok=True, parents=True)
cml_cats = []

for i in range(1, 5):
    fasta_trb_seq = f'/data/mengxf/Project/JML20240731_trb_synthesized_sequence/fasta/trb_amplicon.{i}.fasta'

    fastq1_trb = outdir.joinpath(f'trb_amplicon.{i}.1.fastq')
    fastq2_trb = outdir.joinpath(f'trb_amplicon.{i}.2.fastq')

    with open(fastq1_trb, 'w') as f1, open(fastq2_trb, 'w') as f2:
        for seq_record in SeqIO.parse(fasta_trb_seq, "fasta"):

            for _ in range(num_per_seq):
                timestamp = str(time.time()).replace('.', '')

                f1.write(f'@{seq_record.id}_{timestamp} 1\n')
                f2.write(f'@{seq_record.id}_{timestamp} 2\n')

                f1.write(f'{seq_record.seq[:150]}\n')
                # read2 反向互补
                f2.write(f'{Seq(seq_record.seq[-150:]).reverse_complement()}\n')

                f1.write('+\n')
                f2.write('+\n')

                f1.write('F' * 150 + '\n')
                f2.write('F' * 150 + '\n')

    cml = f"""
    cat {outdir}/NI240729N01_seqtk_sample.1.fastq {fastq1_trb} > {outdir}/trb_amplicon.{i}_merged.1.fastq
    cat {outdir}/NI240729N01_seqtk_sample.2.fastq {fastq2_trb} > {outdir}/trb_amplicon.{i}_merged.2.fastq
    """
    cml_cats.append(cml)

# 阴性数据
cml = f"""
/home/mengxf/miniforge3/envs/basic/bin/seqtk sample {fastq1_negative} {num_negative_read} > {outdir}/NI240729N01_seqtk_sample.1.fastq
/home/mengxf/miniforge3/envs/basic/bin/seqtk sample {fastq2_negative} {num_negative_read} > {outdir}/NI240729N01_seqtk_sample.2.fastq
"""

with open(outdir.joinpath('seqtk_sample.sh'), 'w') as f:
    f.write(cml)

# 合并 trb + negative 脚本
with open(outdir.joinpath('cat.sh'), 'w') as f:
    for cml in cml_cats:
        f.write(cml)
