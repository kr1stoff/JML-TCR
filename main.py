#!/usr/bin/env python
"""
@Time ： 2024/8/9 9:35
@Auth ： kristoff
@File ：temp.py
@IDE ：PyCharm
@Motto：Continuous learning
@LastModified : 2024/8/9 9:35
"""

import click
import logging
from jml_tcr import get_threads_dict
from jml_tcr import get_software_dict
from jml_tcr import get_database_dict
from jml_tcr import get_environment_dict
from jml_tcr import get_sample_names_by_samplesheet
from jml_tcr import prepare_fastq_by_samplesheet
from jml_tcr import create_snakemake_configfile
from jml_tcr import run_snakemake

logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")


@click.command()
@click.option('-i', '--samplesheet', type=click.Path(exists=True),
              help='样本表, 支持 .tsv 和 .xlsx . 格式: "name fq1 fq2"')
# TODO 支持直接输入 bcl2fastq 拆分后的 fastq 文件夹
# @click.option('-I', '--fastq_dir', type=click.Path(exists=True),
#               help='Illumina bcl2fastq 拆分后的 fastq 目录, 按照文件名分配样本名称.')
@click.option('-o', '--workdir', default='tcr_analysis', help='结果输出目录.')
@click.help_option('-h', '--help')
def main(samplesheet, workdir):
    """TCR-Seq 分析工具"""
    logging.info('开始分析')
    dict_thr = get_threads_dict()
    dict_soft = get_software_dict()
    dict_db = get_database_dict()
    dict_env = get_environment_dict()
    sample_names = get_sample_names_by_samplesheet(samplesheet)
    prepare_fastq_by_samplesheet(workdir, samplesheet)
    create_snakemake_configfile(dict_soft, dict_db, workdir, sample_names, dict_thr)
    run_snakemake(dict_env, dict_thr, workdir)
    logging.info('分析结束')


# TODO 组间分析 和 CDR3 追踪分析

if __name__ == '__main__':
    main()
