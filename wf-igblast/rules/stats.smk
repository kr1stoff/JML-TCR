rule filter_cdr3:
    input:
        rules.igblast.output
    output:
        '5.stats/{sample}.igblast.out19.cdr3'
    params:
        csvtk=config['software']['csvtk']
    log:
        '.log/{sample}.filter_cdr3.log'
    benchmark:
        '.log/{sample}.filter_cdr3.bm'
    shell:
        """
        {params.csvtk} -t filter2 -f '$cdr3!=""' {input} > {output} 2> {log}
        """

rule add_cdr3_num:
    input:
        rules.filter_cdr3.output,
        rules.rmdup.output.dup_num_file
    output:
        '5.stats/{sample}.add_cdr3_num.txt'
    benchmark:
        '.log/{sample}.add_cdr3_num.bm'
    script:
        '../scripts/add_cdr3_num.py'

rule calc_freq_and_filter:
    input:
        rules.add_cdr3_num.output
    output:
        '5.stats/{sample}.stats.tsv'
    benchmark:
        '.log/{sample}.calc_freq_and_filter.py.bm'
    script:
        '../scripts/calc_freq_and_filter.py'
