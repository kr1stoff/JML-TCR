#!/usr/bin/env python

import click
from Bio import SeqIO
import re


def format_header_from_imgt_to_imseq(desc: str):
    tr_type = desc.split('|')[1]
    tr_patt = re.compile('(TR[ABDG])([VDJ])(.*?)\\*(0\\d)')
    ig_patt = re.compile('(IG[HKL])([VDJ])(.*?)\\*(0\\d)')

    if 'TR' in tr_type:
        res = tr_patt.findall(tr_type)[0]
    else:
        res = ig_patt.findall(tr_type)[0]

    return '|'.join(res) + '|'


@click.command()
@click.option('-i', '--input_file', type=click.Path(exists=True), required=True,
              help='输入IMGT数据库, 合并 VDJ fasta 文件.')
@click.option('-o', '--output_file', default='imseq.fasta', help='输出 imseq 数据库文件. (默认: imseq.fasta)')
def main(input_file, output_file):
    g = open(output_file, 'w')

    for seq_record in SeqIO.parse(input_file, "fasta"):
        new_desc = format_header_from_imgt_to_imseq(seq_record.description)
        g.write('>' + new_desc + '\n')
        g.write(str(seq_record.seq).replace('.', '') + '\n')

    g.close()


if __name__ == '__main__':
    main()
