#!/usr/bin/env python

import pandas as pd


def main(input_file, output):
    """过滤加过数量的 igblast cdr3 表格, 合并相同 cdr3 的条目"""
    # 使用到的列 num v_call d_call j_call cdr3 cdr3_aa
    df = pd.read_table(input_file, sep='\t', usecols=['num', 'v_call', 'd_call', 'j_call', 'cdr3', 'cdr3_aa'], dtype=str)
    df.fillna('', inplace=True)

    # 过滤 N & 20 <= len <= 80
    df_filter = df[~df['cdr3'].str.contains('N') & (df['cdr3'].str.len() >= 20) & (df['cdr3'].str.len() <= 80)]

    # 合并, 删除等位基因
    def format_vdj_call(gene: str):
        """TRBV3-1*01,TRBV3-2*01,TRBV3-2*02, 去除等位基因信息, 然后去重"""
        gns = [gn.split('*')[0] for gn in gene.strip().split(',')]
        gns = list(set(gns))
        return gns

    # cdr3 总字典, 总数量计数器
    cdr3_dict = {}
    total_num = 0

    for row in df_filter.iterrows():
        cdr3 = row[1]['cdr3']
        num = int(row[1]['num'])
        vc = format_vdj_call(row[1]['v_call'])
        dc = format_vdj_call(row[1]['d_call'])
        jc = format_vdj_call(row[1]['j_call'])
        cdr3aa = row[1]['cdr3_aa']

        if cdr3 not in cdr3_dict:
            cdr3_dict.setdefault(cdr3, {})
            cdr3_dict[cdr3].setdefault('cdr3', cdr3)
            cdr3_dict[cdr3].setdefault('cdr3aa', cdr3aa)
            cdr3_dict[cdr3].setdefault('vc', vc)
            cdr3_dict[cdr3].setdefault('dc', dc)
            cdr3_dict[cdr3].setdefault('jc', jc)
            cdr3_dict[cdr3].setdefault('num', num)
        else:
            cdr3_dict[cdr3]['vc'] = list(set(cdr3_dict[cdr3]['vc'] + vc))
            cdr3_dict[cdr3]['num'] += num
            cdr3_dict[cdr3]['dc'] = list(set(cdr3_dict[cdr3]['dc'] + dc))
            cdr3_dict[cdr3]['jc'] = list(set(cdr3_dict[cdr3]['jc'] + jc))

        total_num += num

    # 添加频率, v_call 列表转回,分割字符
    for cdr3 in cdr3_dict:
        cdr3_dict[cdr3]['freq'] = cdr3_dict[cdr3]['num'] / total_num
        cdr3_dict[cdr3]['vc'] = ','.join(cdr3_dict[cdr3]['vc']) if cdr3_dict[cdr3]['vc'] != [] else ''
        cdr3_dict[cdr3]['dc'] = ','.join(cdr3_dict[cdr3]['dc']) if cdr3_dict[cdr3]['dc'] != [] else ''
        cdr3_dict[cdr3]['jc'] = ','.join(cdr3_dict[cdr3]['jc']) if cdr3_dict[cdr3]['jc'] != [] else ''

    # 按照 num 拍寻, 然后输出
    df_out = pd.DataFrame(cdr3_dict).T.reset_index(drop=True)
    df_out.sort_values(by='num', inplace=True, ascending=False)
    df_out.to_csv(output, sep='\t', index=False)


if __name__ == '__main__':
    main(snakemake.input[0], snakemake.output[0])
