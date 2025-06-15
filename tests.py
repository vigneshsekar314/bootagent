from os.path import abspath, join
from unittest import main, TestCase
from functions.get_files_info import get_files_info


class TestGetFilesInfo(TestCase):

    def test_empty_dir(self):
        result = get_files_info("calculator")
        self.assertEqual(f"Error: current directory is None", result)

    def test_not_a_dir(self):
        result = get_files_info("calculator", "requirements")
        fullpath = join(abspath("calculator"), "requirements")
        self.assertEqual(f"Error: {fullpath} is not a directory", result)

    def test_cur_dir(self):
        result = get_files_info("calculator",".")
        print(result)
        self.assertTrue(not result.startswith("Error:"))

    def test_pkg_dir(self):
        result = get_files_info("calculator","pkg")
        print(result)
        self.assertTrue(not result.startswith("Error:"))

    def test_bin_dir(self):
        result = get_files_info("calculator","/bin")
        print(result)
        self.assertTrue(result.startswith("Error:"))

    def test_par_dir(self):
        result = get_files_info("calculator","../")
        print(result)
        self.assertTrue(result.startswith("Error:"))



if __name__ == "__main__":
    main()
