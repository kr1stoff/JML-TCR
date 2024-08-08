from pathlib import Path
import yaml


def get_software_dict():
    """获取软件字典"""
    yaml_soft = Path('__file__').resolve().parent.joinpath('config/software.yaml')

    with open(yaml_soft) as f:
        dict_soft = yaml.safe_load(f)

    return dict_soft


def get_database_dict():
    """获取数据库字典"""
    yaml_db = Path('__file__').resolve().parent.joinpath('config/database.yaml')

    with open(yaml_db) as f:
        dict_db = yaml.safe_load(f)

    return dict_db
