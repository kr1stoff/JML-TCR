import unittest
from jml_tcr import get_sample_names_by_samplesheet
from jml_tcr import prepare_fastq_by_samplesheet


class MyTestCase(unittest.TestCase):

    def test_prepare_fastq_samplesheet_tsv(self):
        samplesheet = '/data/mengxf/GitHub/JML-TCR/template/samplesheet.tsv'
        workdir = '/data/mengxf/Project/JML20240806_tcr_pipeline/result/24080801'

        # 软链接 / 解压 fastq
        prepare_fastq_by_samplesheet(workdir, samplesheet)

        self.assertListEqual(
            ['test1', 'test2'],
            get_sample_names_by_samplesheet(samplesheet)
        )


if __name__ == '__main__':
    unittest.main()
