# #!/usr/bin/env python
#
# import re
# from Bio import SeqIO
#
#
# # pycharm 代码重复项警告，注释掉代码。如果测试再取消注释
#
# def format_header_from_imgt_to_imseq(desc: str):
#     tr_type = seq_record.description.split('|')[1]
#     tr_patt = re.compile('(TR[ABDG])([VDJ])(.*?)\\*(0\\d)')
#     ig_patt = re.compile('(IG[HKL])([VDJ])(.*?)\\*(0\\d)')
#
#     if 'TR' in tr_type:
#         res = tr_patt.findall(tr_type)[0]
#     else:
#         res = ig_patt.findall(tr_type)[0]
#
#     return '|'.join(res) + '|'
#
#
# for seq_record in SeqIO.parse('/data/mengxf/GitHub/JML-TCR/test/data/TRB_VDJ_test.fasta', "fasta"):
#     new_desc = format_header_from_imgt_to_imseq(seq_record.description)
#     print('>' + new_desc)
#     print(seq_record.seq)
