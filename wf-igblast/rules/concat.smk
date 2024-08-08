rule concat:
    input:
        rules.flash.output.not_comb_1,
        rules.flash.output.not_comb_2
    output:
        '{sample}/2.merge/concat.fastq'
    benchmark:
        '.log/{sample}.concat.bm'
    script:
        '../scripts/concat.py'

rule final_cat:
    input:
        rules.concat.output,
        rules.flash.output.extended
    output:
        '{sample}/2.merge/final.fastq'
    log:
        '.log/{sample}.final_cat.log'
    benchmark:
        '.log/{sample}.final_cat.bm'
    shell:
        'cat {input} > {output} 2> {log}'
