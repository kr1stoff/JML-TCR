rule rmdup:
    input:
        rules.fq2fa.output
    output:
        dup_num_file='{sample}/3.rmdup/dup-num.txt',
        outfile='{sample}/3.rmdup/rmdup.fasta'
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
