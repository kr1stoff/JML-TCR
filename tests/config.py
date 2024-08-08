import unittest
import yaml
from jml_tcr import get_database_dict
from jml_tcr import get_software_dict


class MyTestCase(unittest.TestCase):

    def test_get_software(self):
        soft_dict = get_software_dict()
        self.assertEqual(soft_dict['igblast'], '/home/mengxf/miniforge3/envs/basic/bin/igblastn')  # add assertion here

    def test_get_database(self):
        with open('/data/mengxf/GitHub/JML-TCR/config/database.yaml') as f:
            db_dict_real = yaml.safe_load(f)

        db_dict = get_database_dict()
        self.assertDictEqual(db_dict, db_dict_real)


if __name__ == '__main__':
    unittest.main()
