#!/usr/bin/env python

import click
from Bio import SeqIO


@click.command()
@click.argument('i', 'input_file', type=click.Path(exists=True), required=True,
                help='输入IMGT数据库, 合并 VDJ fasta 文件.')
@click.argument('o', 'output_file', default='imseq.fasta', help='输出 imseq 数据库文件. (默认: imseq.fasta)')
def main(input_file, output_file):
    for seq_record in SeqIO.parse(input_file, "fasta"):
        print(seq_record)
