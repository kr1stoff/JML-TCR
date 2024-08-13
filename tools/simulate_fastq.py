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

outdir = Path('/data/mengxf/Project/JML20240731_trb_synthesized_sequence/fastq')

# # trb 序列模拟
# 200k * 12 = 2.4M
num_per_seq = 200000

for i in range(1, 5):
    fasta_trb_seq = f'/data/mengxf/Project/JML20240731_trb_synthesized_sequence/fasta/trb_amplicon.{i}.fasta'

    fastq1_trb = outdir.joinpath(f'trb_amplicon.{i}.1.fastq')
    fastq2_trb = outdir.joinpath(f'trb_amplicon.{i}.2.fastq')

    with open(fastq1_trb, 'w') as f1, open(fastq2_trb, 'w') as f2:
        for seq_record in SeqIO.parse(fasta_trb_seq, "fasta"):

            for i in range(num_per_seq):
                timestamp = str(time.time()).replace('.', '')

                f1.write(f'@{seq_record.id}_{timestamp} 1\n')
                f2.write(f'@{seq_record.id}_{timestamp} 2\n')

                f1.write(f'{seq_record.seq[:150]}\n')
                f2.write(f'{seq_record.seq[-150:]}\n')

                f1.write('+\n')
                f2.write('+\n')

                f1.write('F' * 150 + '\n')
                f2.write('F' * 150 + '\n')


# 抽 1M 阴性样本并合并
# seqtk sample /data/mengxf/Software/neoimmune/AutoMRD-1.0.1.2024-07-15_release/Rawdata/PBMC240805/NI240729N01-9-46_L2_1.fq.gz 1000000 > NI240729N01_1M.1.fastq &
# seqtk sample /data/mengxf/Software/neoimmune/AutoMRD-1.0.1.2024-07-15_release/Rawdata/PBMC240805/NI240729N01-9-46_L2_2.fq.gz 1000000 > NI240729N01_1M.2.fastq &

# 合并 trb + negative 脚本
# with open(outdir.joinpath('1.sh'), 'w') as f:
#     for i in range(1, 5):
#         cml = f"""
#         cat NI240729N01_1M.1.fastq trb_amplicon.{i}_trb.1.fastq > trb_amplicon.{i}.merged_1.fastq
#         cat NI240729N01_1M.2.fastq trb_amplicon.{i}_trb.2.fastq > trb_amplicon.{i}.merged_2.fastq
#         """
#         f.write(cml)
