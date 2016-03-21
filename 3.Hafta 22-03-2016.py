class ListemEditor(QDialog):

    def __init__(self, parent=None):
        super(ListemEditor, self).__init__(parent)
        self.setWindowTitle("Engellenecek Domain Adı")
        # Create widgets
        self.tableView = QPlainTextEdit()
        layout = QVBoxLayout()
        layout.addWidget(self.tableView)
        self.kaydetButton = QPushButton("Tamam")
        self.kaydetButton.clicked.connect(self.closeList)
        layout.addWidget(self.kaydetButton, 0, Qt.AlignRight)

        self.setLayout(layout)

    def updateBlocks(self):
        """1. siteyi engelledik ve programı kapattık Daha sonra  programı tekrar çalıştır bu seferde  2.siteyi engellemeki için update yapman lazım"""
        file = open(homedir + "blocklist", 'w+')
        file.write(list.tableView.toPlainText())

    def closeList(self):
        """ Engellenecek domain adı adlı pencereyi kapatmaya yarar  """
        self.updateBlocks()
        list.hide()
