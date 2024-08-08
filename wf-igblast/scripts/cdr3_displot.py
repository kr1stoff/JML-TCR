#!/usr/bin/env python

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('agg')


def main(input_file, output_file):
    """根据 cdr3 stats.tsv 文件, 统计 cdr3 长度作分布图"""
    df = pd.read_table(input_file, sep='\t', usecols=['cdr3'])
    df['CDR3 length'] = df['cdr3'].str.len()
    sns.displot(data=df, x="CDR3 length", kde=True)
    # plt.show()
    plt.savefig(output_file, dpi=300)


if __name__ == '__main__':
    main(snakemake.input[0], snakemake.output[0])
