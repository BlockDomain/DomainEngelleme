from PyQt4.QtCore import Qt, QTimer, SIGNAL

    def __init__(self, parent=None):
        # Bizim proje
        super(MainForm, self).__init__(parent)
        #Bizim pencere başlığı
        self.setWindowTitle(" Sistem Programlama Domain Engelleme ")
        #Bu buton ile domain gireceğiz
        self.editButton = QPushButton("Domain Gir")
        #Bu buton ile zaman başlayacak
        self.startButton = QPushButton("Başla")
        #slider olacak yani zaman aralıkları gösterecek
        self.timeSlider = QSlider(Qt.Horizontal)
        #zamanı label ile ekranda göstereceğiz
        self.timeLabel = QLabel('Zaman')
        # Başlangıçta başla butonumuz pasif olsun
        self.startButton.setEnabled(False)
        #Slideri zamana göre ayarlayacağız ŞUANDA TEMEL PLAN BU
        self.timeSlider.setTickPosition(QSlider.TicksBelow)
        self.timeSlider.setTickInterval(1)
        # Butonlarımızın genişliği ayarlıyoruz
        self.startButton.setFixedWidth(90)
        self.editButton.setFixedWidth(120)
        #Ana Penceremiz boyutları
        self.setFixedSize(600, 150)
        # Contentleri oluşturdum
        bottomRow = QHBoxLayout()
        layout = QVBoxLayout()
        # Oluşturduğum contentlere bileşenleri ekledim ..DAHA GÜZEL BİR GÖRÜNÜM İÇİN
        layout.addWidget(self.startButton, 0, Qt.AlignHCenter)
        layout.addWidget(self.timeSlider)
        bottomRow.addWidget(self.timeLabel)
        bottomRow.addWidget(self.editButton, 0, Qt.AlignRight)
        layout.addLayout(bottomRow)
        self.setLayout(layout)
