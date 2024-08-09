from pathlib import Path
import pandas as pd
from subprocess import run
import re
import logging


def prepare_fastq_by_samplesheet(workdir, samplesheet: str) -> None:
    """
    在项目目录下面准备 fastq 文件
    - 如果未压缩 link, 如果压缩 zcat
    - 支持 .tsv 和 .xlsx 格式
    :param workdir:         工作目录
    :param samplesheet:     样本信息表 SampleSheet
    :return:
    """
    logging.info('在项目目录下面准备 fastq 文件')
    # 创建 {workdir}/.rawdata
    Path(workdir).joinpath('.rawdata').mkdir(exist_ok=True, parents=True)

    df = samplesheet2dataframe(samplesheet)

    # 软链接或解压
    for row in df.iterrows():
        name, fastq1, fastq2 = row[1]
        link_or_zcat_fastq(workdir, name, fastq1, fastq2)


def get_sample_names_by_samplesheet(samplesheet: str) -> list:
    """
    获取样本名列表
    :param samplesheet:
    :return sample_names:   样本名列表
    """
    logging.info('获取样本名列表')
    df = samplesheet2dataframe(samplesheet)
    return df.iloc[:, 0].to_list()


def samplesheet2dataframe(samplesheet: str) -> pd.DataFrame:
    """
    输入 SampleSheet 转成 DataFrame 格式

    :param samplesheet:
    :return df: SampleSheet 转的 DataFrame
    """
    if samplesheet.endswith('.xlsx'):
        df = pd.read_excel(samplesheet, header=None)
    elif samplesheet.endswith('.tsv'):
        df = pd.read_table(samplesheet, sep='\t', header=None)
    else:
        raise ValueError(f'samplesheet 扩展名必须是 .xlsx or .tsv : {samplesheet}')

    # 检查 SampleSheet
    check_samplesheet(df)

    return df


def link_or_zcat_fastq(workdir, name, fastq1, fastq2) -> None:
    """
    软链接或解压fastq文件
    :param workdir:
    :param name:
    :param fastq1:
    :param fastq2:
    :return:
    """
    if fastq1.endswith('.gz'):
        cml = f"""
        zcat {fastq1} > {workdir}/.rawdata/{name}.1.fastq
        zcat {fastq2} > {workdir}/.rawdata/{name}.2.fastq
        """
    else:
        cml = f"""
        ln -sf {fastq1} {workdir}/.rawdata/{name}.1.fastq
        ln -sf {fastq2} {workdir}/.rawdata/{name}.2.fastq
        """

    run(cml, shell=True, executable='/bin/bash', capture_output=True)  # 接收输出防止阻塞(NewBing)


def check_samplesheet(df) -> None:
    """
    检查 SampleSheet 文件, 输入 SampleSheet 转的 DataFrame
    :param df:
    :return:
    """
    for row in df.iterrows():
        name, fastq1, fastq2 = row[1]

        # 检查名称
        pattern = r'[\\/:*?"<>| ]'
        assert not re.search(pattern, name), f'样本名称含有非法字符 (\\/:*?"<>| ) : {name}'

        # 检查 fastq 是否存在
        assert Path(fastq1).exists(), f'fastq1 不存在 : {fastq1}'
        assert Path(fastq2).exists(), f'fastq2 不存在 : {fastq2}'

        # 检查 fastq1 和 fastq2 是否相同
        assert fastq1 != fastq2, f'fastq1 和 fastq2 相同 : {fastq1} - {fastq2}'
