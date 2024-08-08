#!/usr/bin/env python

import click


@click.command()
@click.option('-i', '--sample_sheet', type=click.Path(exists=True), help='样本表, 支持 .tsv 和 .xlsx . 格式: "name fq1 fq2"')
@click.option('-I', '--fastq_dir', type=click.Path(exists=True),
              help='Illumina bcl2fastq 拆分后的 fastq 目录, 按照文件名分配样本名称.')
def main(samplesheet, fastq_dir):
    pass


# TODO 组间分析 和 CDR3 追踪分析

if __name__ == '__main__':
    main()
