#!/usr/bin/env python
import click


@click.command()
@click.option('-i', '--igblast_out', required=True, type=click.Path(exists=True), help='igblast(outfmt 19) 结果文件.')
@click.option('-d', '--dup_num_file', required=True, type=click.Path(exists=True),
              help='seqkit rmdup 去重数量统计文件.')
@click.option('-o', '--output', default='add_cdr3_num.txt', help='输出 igblast 结果文件, 第一列加上数量信息.')
@click.help_option('-h', '--help')
def main(igblast_out, dup_num_file, output):
    """原始 fastq 数据使用 seqkit rmdup 去重, 经过 igblast 比对后, 再将数量信息添加回去"""

    # seq_id: dup_num 字典
    dup_num_dict = {}
    with open(dup_num_file, 'r') as f:
        for line in f:
            num, seq_id = line.strip().split(',')[0].split('\t')
            dup_num_dict[seq_id] = num

    # 在 igblast 前面把序列数量添加上
    with open(igblast_out) as f, open(output, 'w') as g:
        g.write('num\t' + next(f))

        for line in f:
            lns = line.strip().split('\t')

            # 有一些 read 没有重复
            if lns[0] in dup_num_dict:
                num = dup_num_dict[lns[0]]
            else:
                num = 1

            g.write(f'{num}\t{line}')


if __name__ == '__main__':
    main()
