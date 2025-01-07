from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QProgressBar, QApplication
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPixmap

class IconProgressDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Processing...")
        self.setFixedSize(300, 150)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setStyleSheet("background-color: #ffffff; border-radius: 15px;")

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)

        # Add icon
        icon_label = QLabel(self)
        pixmap = QPixmap("icon-2.png")  # Load the icon as a QPixmap
        if not pixmap.isNull():  # Check if the file is valid
            icon_label.setPixmap(pixmap.scaled(100, 150, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        else:
            icon_label.setText("Icon not found")
        icon_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(icon_label)

        # Add text
        text_label = QLabel("Processing your request...", self)
        text_label.setStyleSheet("font-size: 14px; color: #2c3e50;")
        text_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(text_label)

        # Add progress bar
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 0)  # Indeterminate mode
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: 1px solid #ddd;
                background: #eee;
                border-radius: 5px;
            }
            QProgressBar::chunk {
                background-color: #3498db;
            }
        """)
        layout.addWidget(self.progress_bar)

        self.setLayout(layout)

app = QApplication([])

# Show the dialog
dialog = IconProgressDialog()
dialog.show()

# Close the dialog after 20 seconds using a QTimer
timer = QTimer()
timer.singleShot(20000, dialog.close)  # 20000 ms = 20 seconds

app.exec_()
