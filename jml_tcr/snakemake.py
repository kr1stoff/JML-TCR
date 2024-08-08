import yaml
from pathlib import Path
from subprocess import run


def create_snakemake_configfile(
        dict_soft: dict,
        dict_db: dict,
        workdir: str,
        sample_names: list,
        dict_thr: dict
) -> None:
    """创建 snakemake 配置文件"""

    dict_out = {
        'workdir': workdir,
        'samples': sample_names,
        'threads': dict_thr,
        'software': dict_soft,
        'database': dict_db
    }

    with open(f'{workdir}/snakemake_config.yaml', 'w') as f:
        yaml.dump(dict_out, f)


def run_snakemake(dict_env: dict, dict_thr: dict, workdir: str) -> None:
    activate = dict_env['activate']
    snakemake = dict_env['snakemake']
    cores = dict_thr['high']
    snakefile = Path('__file__').resolve().parent.joinpath('wf-igblast/Snakefile')
    configfile = f'{workdir}/snakemake_config.yaml'

    cml = f"""
    source {activate} {snakemake}
    snakemake -c {cores} -s {snakefile} --configfile {configfile}
    """

    run(cml, shell=True, executable='/bin/bash', capture_output=True)
