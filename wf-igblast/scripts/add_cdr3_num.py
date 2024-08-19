#!/usr/bin/env python

def main(igblast_out, dup_num_file, output):
    """
    原始 fastq 数据使用 seqkit rmdup.smk 去重, 经过 igblast 比对后, 再将数量信息添加回去
    :param igblast_out:
    :param dup_num_file:
    :param output:

    ```bash
    igblastn \
        -germline_db_V Database/IMGT/2024.07/Homo_sapiens/TR/igblast/human_TRBV.fa \
        -germline_db_D Database/IMGT/2024.07/Homo_sapiens/TR/igblast/human_TRBD.fa \
        -germline_db_J Database/IMGT/2024.07/Homo_sapiens/TR/igblast/human_TRBJ.fa \
        -domain_system imgt \
        -organism human \
        -ig_seqtype TCR \
        -auxiliary_data miniforge3/envs/basic/share/igblast/optional_file/human_gl.aux \
        -show_translation \
        -outfmt 19 \
        -num_threads 16 \
        -query rmdup.smk.fasta \
        -out igblast.output.19

    # 保留注释到CDR3的信息
    csvtk -t filter2 -f '$cdr3!=""' igblast.output.19 > igblast.output.19.cdr3

    # 给 output.19 添加num信息
    python add_cdr3_num.py -i igblast.output.19.cdr3 -d rmdup.smk/dup-num.txt
    ```
    """

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
    main(snakemake.input[0], snakemake.input[1], snakemake.output[0])
