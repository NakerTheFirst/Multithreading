from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QLabel, QPushButton, QGridLayout
from PyQt6.QtCore import pyqtSignal, Qt, QThread, QObject
from PyQt6.QtGui import QIcon


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.buffer_textbox = None
        self.progress_bar = None
        self.sleep_textbox = None
        self.delay_label = None
        self.enter_button = None
        self.setWindowTitle("Multithreading: GUI Example")
        self.setFixedSize(400, 400)

        self.init_ui()
        self.start_threads()

    def init_ui(self):
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.centralWidget().setStyleSheet("background-color: #1E1E1E; color: #1E1E1E")
        self.setWindowIcon(QIcon('icon.svg'))
        layout = QGridLayout()

        # Read-only textbox
        self.buffer_textbox = QLineEdit("")
        self.buffer_textbox.setReadOnly(True)
        self.buffer_textbox.setStyleSheet("background-color: #2F2F2F; color: #DBF2F3; border: none; font-size: 20px")
        layout.addWidget(self.buffer_textbox, 0, 0, 1, 4)

        # ASCII Progress Bar (using QLabel)
        self.progress_bar = QLabel("[--------------------]")
        self.progress_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progress_bar.setStyleSheet("background-color: #1e1e1e; color: #DBF2F3; border: none; font-size: 40px")
        layout.addWidget(self.progress_bar, 1, 0, 1, 4)

        # Label
        self.delay_label = QLabel("Delay in seconds:")
        self.delay_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.delay_label.setStyleSheet("background-color: #2F2F2F; color: #DBF2F3; border: none; font-size: 20px")
        layout.addWidget(self.delay_label, 2, 0, 1, 2)

        # Time to sleep textbox
        self.sleep_textbox = QLineEdit("1")
        self.sleep_textbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sleep_textbox.setStyleSheet("background-color: #2F2F2F; color: #DBF2F3; border: none; font-size: 20px")
        layout.addWidget(self.sleep_textbox, 2, 2, 1, 2)

        # Enter Button
        self.enter_button = QPushButton("Enter")
        self.enter_button.setStyleSheet("background-color: #2E8E91; color: #DBF2F3; border: none; font-size: 20px")
        layout.addWidget(self.enter_button, 3, 0, 1, 4)

        central_widget.setLayout(layout)

    def start_threads(self):
        # Thread setup
        self.thread1 = QThread()
        self.worker1 = Worker("p", 1)
        self.worker1.moveToThread(self.thread1)
        self.worker1.update_signal.connect(self.update_textbox)
        self.thread1.started.connect(self.worker1.run)
        self.thread1.start()

        self.thread2 = QThread()
        self.worker2 = Worker("s", 1)
        self.worker2.moveToThread(self.thread2)
        self.worker2.update_signal.connect(self.update_textbox)
        self.thread2.started.connect(self.worker2.run)
        self.thread2.start()

        self.thread3 = QThread()
        self.worker3 = Worker("t", 1)
        self.worker3.moveToThread(self.thread3)
        self.worker3.update_signal.connect(self.update_textbox)
        self.thread3.started.connect(self.worker3.run)
        self.thread3.start()

    def update_textbox(self, char):
        current_text = self.buffer_textbox.text()
        new_text = current_text + char
        self.buffer_textbox.setText(new_text)


class Worker(QObject):
    update_signal = pyqtSignal(str)

    def __init__(self, character, delay):
        super().__init__()
        self.character = character
        self.delay = delay

    def run(self):
        while True:
            self.update_signal.emit(self.character)
            QThread.sleep(self.delay)


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
