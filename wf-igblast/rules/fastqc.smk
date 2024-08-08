ruleorder: pre_fastqc_pe > pre_fastqc_se
ruleorder: post_fastqc_pe > post_fastqc_se

rule pre_fastqc_pe:
    input:
        '.rawdata/{sample}.1.fastq',
        '.rawdata/{sample}.2.fastq'
    output:
        directory('{sample}/1.qc/before')
    params:
        fastqc=config['software']['fastqc'],
        prm='--extract'
    threads:
        config['threads']['low']
    log:
        '.log/{sample}.pre_fastqc_pe.log'
    benchmark:
        '.log/{sample}.pre_fastqc_pe.bm'
    shell:
        """
        mkdir -p {output}
        {params.fastqc} -t {threads} {params.prm} -o {output} {input[0]} {input[1]} &> {log}
        """

rule pre_fastqc_se:
    input:
        '.rawdata/{sample}.fastq'
    output:
        directory('{sample}/1.qc/before')
    params:
        fastqc=config['software']['fastqc'],
        prm='--extract'
    threads:
        config['threads']['low']
    log:
        '.log/{sample}.pre_fastqc_se.log'
    benchmark:
        '.log/{sample}.pre_fastqc_se.bm'
    shell:
        """
        mkdir -p {output}
        {params.fastqc} -t {threads} {params.prm} -o {output} {input} &> {log}
        """

rule post_fastqc_pe:
    input:
        '{sample}/1.qc/clean.1.fastq',
        '{sample}/1.qc/clean.2.fastq'
    output:
        directory('{sample}/1.qc/after')
    params:
        fastqc=config['software']['fastqc'],
        prm='--extract'
    threads:
        config['threads']['low']
    log:
        '.log/{sample}.post_fastqc_pe.log'
    benchmark:
        '.log/{sample}.post_fastqc_pe.bm'
    shell:
        """
        mkdir -p {output}
        {params.fastqc} -t {threads} {params.prm} -o {output} {input[0]} {input[1]} &> {log}
        """

rule post_fastqc_se:
    input:
        '{sample}/1.qc/clean.fastq'
    output:
        directory('{sample}/1.qc/after')
    params:
        fastqc=config['software']['fastqc'],
        prm='--extract'
    threads:
        config['threads']['low']
    log:
        '.log/{sample}.post_fastqc_se.log'
    benchmark:
        '.log/{sample}.post_fastqc_se.bm'
    shell:
        """
        mkdir -p {output}
        {params.fastqc} -t {threads} {params.prm} -o {output} {input} &> {log}
        """
