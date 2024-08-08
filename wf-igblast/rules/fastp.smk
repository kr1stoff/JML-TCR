ruleorder: fastp_pe > fastp_se

rule fastp_pe:
    input:
        '.rawdata/{sample}.1.fastq',
        '.rawdata/{sample}.2.fastq'
    output:
        j='{sample}/1.qc/fastp.json',
        h='{sample}/1.qc/fastp.html',
        o='{sample}/1.qc/clean.1.fastq',
        O='{sample}/1.qc/clean.2.fastq'
    params:
        fastp=config['software']['fastp'],
        prm='-q 15 -u 40 -t 0 -G -n 5 -l 15 -y'
    threads:
        config['threads']['low']
    log:
        '.log/{sample}.fastp_pe.log'
    benchmark:
        '.log/{sample}.fastp_pe.bm'
    shell:
        '{params.fastp} -w {threads} {params.prm} -j {output.j} -h {output.h} -o {output.o} -O {output.O} -i {input[0]} -I {input[1]} &> {log}'

rule fastp_se:
    input:
        '.rawdata/{sample}.fastq',
    output:
        j='{sample}/1.qc/fastp.json',
        h='{sample}/1.qc/fastp.html',
        o='{sample}/1.qc/clean.fastq'
    params:
        fastp=config['software']['fastp'],
        prm='-q 15 -u 40 -t 0 -G -n 5 -l 15 -y'
    threads:
        config['threads']['low']
    log:
        '.log/{sample}.fastp_se.log'
    benchmark:
        '.log/{sample}.fastp_se.bm'
    shell:
        '{params.fastp} -w {threads} {params.prm} -j {output.j} -h {output.h} -o {output.o} -i {input} &> {log}'

rule parse_fastp_json:
    input:
        '{sample}/1.qc/fastp.json'
    output:
        '{sample}/1.qc/basic.stat.txt'
    benchmark:
        '.log/{sample}.parse_fastp_json.bm'
    script:
        "../scripts/parse_fastp_json.py"
