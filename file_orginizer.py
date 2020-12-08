import os
import sys
import shutil
from os import listdir
from os.path import isfile, join
from pathlib import Path
from  PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import QtGui

dir_path = os.path.dirname(os.path.realpath(__file__))
dir_path = dir_path.replace("\\", "/")
destination_folder = []
search_directories = []
search_directories.append(dir_path)
file_format = ""
file = ""
i = 0

#Application
class Application(QMainWindow):
    def __init__(self):
        super().__init__()
        self.left=10
        self.top=10
        self.width=800
        self.height=600
        self.initUI()
    
    def initUI(self):
        self.setGeometry(self.left, self.top, self.width, self.height)


        self.button=QPushButton("Search directory", self)
        self.button.move(25, 75)
        self.button.clicked.connect(self.directory_search)
    

        self.button1=QPushButton("Destination Folder", self)
        self.button1.move(25, 125)
        self.button1.clicked.connect(self.set_desination)

        self.button2=QPushButton("Move files", self)
        self.button2.move(25, 225)
        self.button2.clicked.connect(self.move_file)

        self.button3=QPushButton("Delete Files", self)
        self.button3.move(25, 275)
        self.button3.clicked.connect(self.delete_file)

        self.clearDirectories=QPushButton("Clear directories", self)
        self.clearDirectories.move(25, 175)
        self.clearDirectories.clicked.connect(self.clear_dir)


        self.dirSearch = QLabel("Selected Directories: ", self)
        self.dirSearch.move(300, 100)
        self.listDirectories = QTextEdit(self)
        self.listDirectories.setReadOnly(True)
        self.listDirectories.move(300, 125)
        self.listDirectories.resize(200,200)


        self.fileTypeLabel = QLabel("File extension: ", self)
        self.fileTypeLabel.move(300, 25)
        self.setFileType = QLineEdit(self)
        self.setFileType.move(300, 55)
        
        self.show()
    
    @pyqtSlot()
    def directory_search(self):
        directory = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if directory:
            directory = directory.replace("\\", "/")
            print(directory)
            search_directories.append(directory)
            self.listDirectories.append(directory)
            print(search_directories)
            

    def set_desination(self):
        destination = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if destination:
            destination = destination.replace("\\", "/")
            destination_folder.append(destination)
            print(destination_folder)
            

    def move_file(self):
        #iterate through the list of directories and if the file has a matching extension, move it to the destination folder
        for i in range(len(search_directories)):
            sourcepath = search_directories[i]
            sourcefiles = os.listdir(sourcepath)
            for file in sourcefiles:
                if file.endswith(self.setFileType.text()):
                    shutil.move(os.path.join(sourcepath, file), destination_folder[0])
                    print(f'moved {i} files')

    def delete_file(self):
        for i in range(len(search_directories)):
            sourcepath = search_directories[i]
            sourcefiles = os.listdir(sourcepath)
            for file in sourcefiles:
                if file.endswith(self.setFileType.text()):
                    os.remove(os.path.join(sourcepath, file))    

    def rename_file(self):
        pass

    def clear_dir(self):
        search_directories.clear()
        self.listDirectories.clear()

                    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Application()
    sys.exit(app.exec_())
    