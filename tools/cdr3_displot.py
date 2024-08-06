#!/usr/bin/env python

import click
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('agg')


@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('-o', '--output-file', default='displot.png', help='输出 displot 文件路径. (默认: displot.png)')
@click.help_option('-h', '--help')
def main(input_file, output_file):
    """根据 cdr3 stats.tsv 文件, 统计 cdr3 长度作分布图"""
    df = pd.read_table(input_file, sep='\t', usecols=['cdr3'])
    df['CDR3 length'] = df['cdr3'].str.len()
    sns.displot(data=df, x="CDR3 length", kde=True)
    # plt.show()
    plt.savefig(output_file, dpi=300)


if __name__ == '__main__':
    main()
