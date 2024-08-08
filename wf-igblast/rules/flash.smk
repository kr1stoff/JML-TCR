rule flash:
    input:
        '{sample}/1.qc/clean.1.fastq',
        '{sample}/1.qc/clean.2.fastq'
    output:
        not_comb_1='{sample}/2.merge/notCombined_1.fastq',
        not_comb_2='{sample}/2.merge/notCombined_2.fastq',
        extended='{sample}/2.merge/extendedFrags.fastq'
    params:
        flash=config['software']['flash'],
        params='-m 10'
    threads:
        config['threads']['high']
    log:
        '.log/{sample}.flash.log'
    benchmark:
        '.log/{sample}.flash.bm'
    run:
        outdir = output.not_comb_1.split('/')[0]
        prefix = output.not_comb_1.split('/')[1].split('.')[0]
        shell('{params.flash} -t {threads} -d {outdir} -o {prefix} {params.params} {input} &> {log}')
