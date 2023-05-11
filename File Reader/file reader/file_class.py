import logging
import os.path

logging.basicConfig(filename="File_Reader.log", level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")


class FileParser:
    """This is a file reader"""

    def __init__(self, f):
        """Bind a data to the parent class"""
        self.file = f

    def file_checker(self):
        """The file checker"""
        try:
            if os.path.exists(self.file):
                return True
            else:
                return f"You don't have the file"
        except Exception as e:
            logging.info(f"{e}")

    def file_writer(self):

        """The file writer"""
        try:
            if self.file_checker():
                if self.file[-4:] != ".txt":
                    with open(f"{self.file}.txt", "w") as file:
                        while True:
                            writing = input("Write a sentence, it breaks when you enter '-1'. \n")
                            if writing == "-1":
                                return f"You are logged out already"
                                break
                            else:
                                file.writelines(writing + "\n")
                        logging.info("Your file has been written successfully")
            else:
                logging.info("There is no file like that, but a new file will be created")
                with open(f"{self.file}", "r+") as file:
                    while True:
                        writing = input("Write a sentence, it breaks when you enter '-1'. \n")

                        if writing == "-1":
                            break
                        else:
                            file.writelines(writing + "\n")
                    logging.info("Your file has been written successfully even though the path wasn't correct initally")
        except Exception as e:
            logging.info(f"{e}")

    def file_reader(self):

        """The file reader"""

        try:
            if self.file_checker():
                if self.file[-4:] != ".txt":
                    with open(f"{self.file}.txt", "r") as f:
                        for line in f.readlines():
                            logging.info(f"{line}")
                elif self.file[-4:] == ".txt":
                    with open(self.file, "r") as f:
                        for line in f.readlines():
                            logging.info(f"{line}")
                else:
                    return -1
        except Exception as e:
            logging.info(f"{e}")


class file_child(FileParser):
    def __init__(self, *args):
        FileParser.__init__(self, *args)
