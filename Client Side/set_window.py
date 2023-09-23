from PyQt5.QtWidgets import QMainWindow, QMessageBox, QWidget
from PyQt5.uic import loadUi
from detect_window import DetectionWindow

class SettingsWindow(QMainWindow):
    def __init__(self):
        super(SettingsWindow, self).__init__()
        loadUi('UI/settings_window.ui', self)
        
        self.detect_window = DetectionWindow()
        
        self.pushButton.clicked.connect(self.go_to_detection)
        
    def displayInfo(self):
        self.show()
    
    def go_to_detection(self):
        if self.detect_window.isVisible():
            print('Detection window is already open!')
        else:
            self.detect_window.create_detection_instance()
            self.detect_window.start_detection()
    
    def closeEveent(self, event):
        if self.detect_window.isVisible():
            self.detect_window.detection.running = False
            self.detect_window.close()
            event.accept()