from PyQt4.QtCore import Qt, QTimer, SIGNAL

    def __init__(self, parent=None):
        # Create our main layout for picking duration and such
        super(MainForm, self).__init__(parent)
        self.setWindowTitle(" Sistem Programlama Domain Engelleme ")
        # Create widgets such as buttons and slider
        self.editButton = QPushButton("Domain Gir")
        self.startButton = QPushButton("Başla")
        self.timeSlider = QSlider(Qt.Horizontal)
        self.timeLabel = QLabel('Zaman')
        # Disable start button
        self.startButton.setEnabled(False)
        # Mess with the slider
        self.timeSlider.setTickPosition(QSlider.TicksBelow)
        self.timeSlider.setTickInterval(1)
        # Edit button widths
        self.startButton.setFixedWidth(90)
        self.editButton.setFixedWidth(120)
        self.setFixedSize(600, 150)
        # Create another layout to hold bottom contents
        bottomRow = QHBoxLayout()
        layout = QVBoxLayout()
        # Add to the layout
        layout.addWidget(self.startButton, 0, Qt.AlignHCenter)
        layout.addWidget(self.timeSlider)
        bottomRow.addWidget(self.timeLabel)
        bottomRow.addWidget(self.editButton, 0, Qt.AlignRight)
        layout.addLayout(bottomRow)
        # Set layout
        self.setLayout(layout)
        # Link functions to button and slider
        self.startButton.clicked.connect(backend.startBlock)
        self.timeSlider.valueChanged.connect(self.change)
        self.editButton.clicked.connect(self.openList)
