rule displot:
    input:
        rules.calc_freq_and_filter.output
    output:
        '{sample}/6.figure/displot.png'
    benchmark:
        '.log/{sample}.displot.bm'
    script:
        '../scripts/cdr3_displot.py'

rule heatmap:
    input:
        rules.calc_freq_and_filter.output
    output:
        '{sample}/6.figure/heatmap.png'
    benchmark:
        '.log/{sample}.heatmap.bm'
    script:
        '../scripts/cdr3_heatmap.py'
