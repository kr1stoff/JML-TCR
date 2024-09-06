from pathlib import Path
import yaml
import logging


def get_software_dict() -> dict:
    """获取软件字典"""
    logging.info('获取软件字典')
    yaml_soft = Path(__file__).resolve().parents[1].joinpath('config/software.yaml')

    with open(yaml_soft) as f:
        dict_soft = yaml.safe_load(f)

    return dict_soft


def get_database_dict() -> dict:
    """获取数据库字典"""
    logging.info('获取数据库字典')
    yaml_db = Path(__file__).resolve().parents[1].joinpath('config/database.yaml')

    with open(yaml_db) as f:
        dict_db = yaml.safe_load(f)

    return dict_db


def get_environment_dict() -> dict:
    """获取 Conda 环境字典"""
    logging.info('获取 Conda 环境字典')
    yaml_env = Path(__file__).resolve().parents[1].joinpath('config/environment.yaml')
    with open(yaml_env) as f:
        dict_env = yaml.safe_load(f)

    return dict_env
