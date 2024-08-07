rule igblast:
    input:
        rules.rmdup.output.outfile
    output:
        '4.igblast/{sample}.igblast.out19'
    threads:
        config['threads']['high']
    params:
        igblastn=config['software']['igblast'],
        params='-organism human -domain_system imgt -ig_seqtype TCR -show_translation -outfmt 19',
        db_v=config['database']['germline_db_V'],
        db_d=config['database']['germline_db_D'],
        db_j=config['database']['germline_db_J'],
        aux=config['database']['auxiliary_data']
    log:
        '.log/{sample}.igblast.log'
    benchmark:
        '.log/{sample}.igblast.bm'
    shell:
        """
        {params.igblastn} -num_threads {threads} {params.params} \
            -germline_db_V {params.db_v} \
            -germline_db_D {params.db_d} \
            -germline_db_J {params.db_j} \
            -auxiliary_data {params.aux} \
            -query {input} -out {output} &> {log}
         """
