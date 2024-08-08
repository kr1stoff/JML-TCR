from pathlib import Path
import yaml


def get_software_dict():
    """获取软件字典"""
    soft_yaml = Path('__file__').resolve().parent.joinpath('config/software.yaml')

    with open(soft_yaml) as f:
        soft_dict = yaml.safe_load(f)

    return soft_dict


def get_database_dict():
    """获取数据库字典"""
    db_yaml = Path('__file__').resolve().parent.joinpath('config/database.yaml')

    with open(db_yaml) as f:
        db_dict = yaml.safe_load(f)

    return db_dict
