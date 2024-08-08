import unittest
from jml_tcr import prepare_fastq_samplesheet


class MyTestCase(unittest.TestCase):

    def test_prepare_fastq_samplesheet_tsv(self):
        self.assertListEqual(
            ['test1', 'test2'],
            prepare_fastq_samplesheet(
                '/data/mengxf/Project/JML20240806_tcr_pipeline/result/24080801',
                '/data/mengxf/GitHub/JML-TCR/template/samplesheet.tsv')
        )

    def test_prepare_fastq_samplesheet_xlsx(self):
        self.assertListEqual(
            ['test1', 'test2'],
            prepare_fastq_samplesheet(
                '/data/mengxf/Project/JML20240806_tcr_pipeline/result/24080801',
                '/data/mengxf/GitHub/JML-TCR/template/samplesheet.xlsx')
        )


if __name__ == '__main__':
    unittest.main()
