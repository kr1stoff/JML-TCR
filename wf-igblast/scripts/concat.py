#!/usr/bin/env python

def main(fastqs, output):
    """
    TCR PE150 没有 overlap 的双端 FASTQ 合并脚本.

    :param fastqs:  read1/2 FASTQ 文件
    :param output:  输出合并后 FASTQ 文件

    ```bash
    flash -t 16 -d . -o FanYin-T -m 10 FanYin-T_1.fq.gz FanYin-T_2.fq.gz

    python concat_non_overlap_pe_reads.py -o FanYin-T.mergedPyNNN.fastq \
        FanYin-T.notCombined_1.fastq FanYin-T.notCombined_2.fastq
    ```
    """
    input1, input2 = fastqs
    line_count = 0
    g = open(output, 'wt')

    with open(input1) as f1, open(input2) as f2:

        for line1, line2 in zip(f1, f2):
            line_count += 1

            # header 信息行
            if line_count % 4 == 1:
                head_info1 = line1.split(' ')[0]
                head_info2 = line2.split(' ')[0]
                # 检查双端 fastq 是否配对
                assert head_info1 == head_info2, f'FASTQ当前序列不是一对. {head_info1} - {head_info2}'
                g.write(head_info1 + '\n')
            # 序列行
            elif line_count % 4 == 2:
                g.write(f'{line1.strip()}{"N" * 100}{line2.strip()}\n')
            # +
            elif line_count % 4 == 3:
                g.write('+\n')
            # 质量行
            else:
                g.write(f'{line1.strip()}{"?" * 100}{line2.strip()}\n')

    g.close()


if __name__ == '__main__':
    main((snakemake.input[0], snakemake.input[1]), snakemake.output[0])
