 def degistir(self):
        """ Zamanı ayarlayalım"""
        if self.timeSlider.value() == 0:
            self.ZamanLabel.setText("Zaman")
            self.startButton.setEnabled(False)
            return
        self.startButton.setEnabled(True)
        deger = self.timeSlider.value() * 15
        if ((deger - deger % 60) / 60) == 1:
                t = str((deger - deger % 60) / 60) + " saat, "   # saat=1
        elif ((deger - deger % 60) / 60) == 0:
                t = ""
        else:
                t = str((deger - deger % 60) / 60) + " saat, "   # saat=>1

        self.ZamanLabel.setText(t + str(deger % 60) + " dakika")
