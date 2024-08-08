import unittest
from jml_tcr import get_threads
from jml_tcr import get_database_dict
from jml_tcr import get_software_dict
from jml_tcr import get_sample_names_by_samplesheet
from jml_tcr import create_snakemake_configfile
from jml_tcr import run_snakemake
from jml_tcr import get_environment_dict

class MyTestCase(unittest.TestCase):
    def test_snakemake(self):
        # self.assertEqual(True, False)  # add assertion here
        workdir = '/data/mengxf/Project/JML20240806_tcr_pipeline/result/24080801'
        samplesheet = '/data/mengxf/GitHub/JML-TCR/template/samplesheet.xlsx'
        dict_thr = get_threads()
        dict_db = get_database_dict()
        dict_soft = get_software_dict()
        sample_names = get_sample_names_by_samplesheet(samplesheet)

        # 生成 snakemake 配置文件
        create_snakemake_configfile(dict_soft, dict_db, workdir, sample_names, dict_thr)

        # 跑 snakemake 流程
        dict_env = get_environment_dict()
        run_snakemake(dict_env, dict_thr, workdir)

        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
