from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLineEdit, QLabel, QPushButton, QGridLayout
from PyQt6.QtCore import pyqtSignal, Qt
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

    def init_ui(self):
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.centralWidget().setStyleSheet("background-color: #1E1E1E; color: #1E1E1E")
        self.setWindowIcon(QIcon('icon.svg'))
        layout = QGridLayout()

        # Readonly textbox
        self.buffer_textbox = QLineEdit("Read-only text")
        self.buffer_textbox.setReadOnly(True)
        self.buffer_textbox.setStyleSheet("background-color: #2F2F2F; color: #DBF2F3; border: none; font-size: 20px")
        layout.addWidget(self.buffer_textbox, 0, 0, 1, 4)

        # ASCII Progress Bar (using QLabel)
        self.progress_bar = QLabel("[--------------------]")
        self.progress_bar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.progress_bar.setStyleSheet("background-color: #1e1e1e; color: #DBF2F3; border: none; font-size: 40px")
        layout.addWidget(self.progress_bar, 1, 0, 1, 4)

        # Label next to the clickable textbox
        self.delay_label = QLabel("Delay in seconds:")
        self.delay_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.delay_label.setStyleSheet("background-color: #2F2F2F; color: #DBF2F3; border: none; font-size: 20px")
        layout.addWidget(self.delay_label, 2, 0, 1, 2)

        # Clickable Textbox (editable)
        self.sleep_textbox = QLineEdit("1")
        self.sleep_textbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sleep_textbox.setStyleSheet("background-color: #2F2F2F; color: #DBF2F3; border: none; font-size: 20px")
        layout.addWidget(self.sleep_textbox, 2, 2, 1, 2)

        # Enter Button
        self.enter_button = QPushButton("Enter")
        self.enter_button.setStyleSheet("background-color: #2E8E91; color: #DBF2F3; border: none; font-size: 20px")
        layout.addWidget(self.enter_button, 3, 0, 1, 4)

        central_widget.setLayout(layout)


def main():
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
