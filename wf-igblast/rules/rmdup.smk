rule rmdup:
    input:
        rules.fq2fa.output
    output:
        dup_num_file='3.rmdup/{sample}.dup-num.txt',
        outfile='3.rmdup/{sample}.rmdup.fasta'
    params:
        seqkit=config['software']['seqkit'],
        params='-s'  # by-seq
    threads:
        config['threads']['low']
    log:
        '.log/{sample}.rmdup.log'
    benchmark:
        '.log/{sample}.fq2fa.bm'
    shell:
        '{params.seqkit} rmdup -j {threads} {params.params} -D {output.dup_num_file} -o {output.outfile} {input} 2> {log}'
