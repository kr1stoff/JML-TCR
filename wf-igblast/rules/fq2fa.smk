rule fq2fa:
    input:
        rules.final_cat.output
    output:
        '2.merge/{sample}.final.fasta'
    params:
        seqkit=config['software']['seqkit']
    threads:
        config['threads']['low']
    log:
        '.log/{sample}.fq2fa.log'
    benchmark:
        '.log/{sample}.fq2fa.bm'
    shell:
        '{params.seqkit} fq2fa -j {threads} {input} > {output} 2> {log}'
