#!/usr/bin/env python

import click
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('agg')


@click.command()
@click.argument('input_file', type=click.Path(exists=True))
@click.option('-o', '--output-file', default='heatmap.png', help='输出 displot 文件路径. (默认: displot.png)')
@click.help_option('-h', '--help')
def main(input_file, output_file):
    """根据 cdr3 stats.tsv 文件, 统计 V/J 基因作热图"""
    df = pd.read_table(input_file, sep='\t', usecols=['vc', 'jc'])
    vj_dict = {}

    for row in df.iterrows():
        vcs = list(set([vc.split('/')[0] for vc in row[1]['vc'].strip().split(',')]))
        jcs = list(set([jc.split('/')[0] for jc in row[1]['jc'].strip().split(',')]))

        for v in vcs:
            for j in jcs:
                vj_dict.setdefault(v, {})
                vj_dict[v].setdefault(j, 1)
                vj_dict[v][j] += 1

    df_plot = pd.DataFrame(vj_dict).fillna(0)
    ax = sns.heatmap(df_plot, cmap=sns.color_palette("vlag", as_cmap=True))
    ax.figure.set_figwidth(15)
    ax.figure.set_figheight(7.4)
    plt.savefig(output_file, dpi=300)


if __name__ == '__main__':
    main()
