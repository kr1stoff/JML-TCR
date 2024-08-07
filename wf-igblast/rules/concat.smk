rule concat:
    input:
        rules.flash.output.not_comb_1,
        rules.flash.output.not_comb_2
    output:
        '2.merge/{sample}.concat.fastq'
    benchmark:
        '.log/{sample}.concat.bm'
    script:
        '../scripts/concat.py'

rule final_cat:
    input:
        rules.concat.output,
        rules.flash.output.extended
    output:
        '2.merge/{sample}.final.fastq'
    log:
        '.log/{sample}.final_cat.log'
    benchmark:
        '.log/{sample}.final_cat.bm'
    shell:
        'cat {input} > {output} 2> {log}'
