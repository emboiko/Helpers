import sys

class Outfile:
    def __init__(self, file_name):
        self.file_name = file_name
        self._current_stdout = sys.stdout

    
    def __enter__(self):
        self._file = open(self.file_name, "w")
        sys.stdout = self._file


    def __exit__(self, ex_type, ex_value, ex_traceback):
        sys.stdout = self._current_stdout
        self._file.close()
        return False
