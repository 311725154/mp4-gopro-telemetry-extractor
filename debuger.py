import time


class Debuger():
    """
    Simple self debuting tool
    """
    def __init__(self):
        self.log_string = ""
        self.file_counter = 0
        self.start_time = time.ctime(time.time())
        self.end_time = ""

    def print_to_console(self, string):
        """
        printing log message according to the string parameter
        :param string: The message that the log reader wants to read
        :return: void
        """
        if "web-driver object created" in string:
            self.file_counter += 1
        self.log_string += string
        print("LOG: " + string)

    def print_summery(self):
        self.end_time = time.ctime(time.time())
        print("Test summery:\n______________\nStart time: {}\nEnd time: {}\nConverted files: {}".format(self.start_time, self.end_time, self.file_counter))