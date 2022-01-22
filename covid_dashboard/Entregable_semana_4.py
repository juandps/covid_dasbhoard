#Karen masache astudillo
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

#Importar aquí las librerías a utilizar
import pandas as pd
import matplotlib.pyplot as plt

from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import (QListWidget, QMessageBox, 
     QVBoxLayout)

qtCreatorFile = "appandas.ui" #Aquí va el nombre de tu archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.boton2.clicked.connect(self.plot)
        self.df = pd.read_csv(str( 'covid_data_official.csv'))

   #Este es el primer método para el WIDGET 1
    def plot(self):
        
        fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()
        self.df.plot(x="dateRep", y="cases", ax=ax1, ylabel= "Casos Positivos")
        self.df.plot(x="dateRep" ,y="deaths", ax=ax2, ylabel= "Muertes")
        plt.show()
    #Este es el primer método para el WIDGET 1
    def cuadro_lista_1 (self):

        vbox = QVBoxLayout(self)

        listWidget = QListWidget()
    
       # PROFE: Aquí van a ir los estados del dataframe de pandas que aun no logro conectarlo. Pero ya mismo     
        listWidget.addItem("New York") 
        listWidget.addItem("New Jersey")
        listWidget.addItem("Washington")
        listWidget.addItem("Delaware")
        listWidget.addItem("California")
        listWidget.addItem("Kentucky")
        listWidget.addItem("Boston")
        listWidget.addItem("Connecicut")
        listWidget.addItem("Meriland")
        listWidget.addItem("Virginia")
    
            
        listWidget.itemDoubleClicked.connect(self.onClicked)
        
        vbox.addWidget(listWidget)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('QListWidget')
        self.show()
    #Este es el primer método para el WIDGET 3
    def cuadro_lista_2 (self):
            vbox = QVBoxLayout(self)
            listWidget = QListWidget()
        
            # PROFE: Aquí van a ir los paises del dataframe de pandas que aun no logro conectarlo. Pero ya mismo     
            listWidget.addItem("Australia") 
            listWidget.addItem("Ecuador")
            listWidget.addItem("España")
            listWidget.addItem("Suiza")
            listWidget.addItem("Colombia")
            listWidget.addItem("Francia")
            listWidget.addItem("Alemania")
            listWidget.addItem("Israel")
            listWidget.addItem("China")
            listWidget.addItem("Portugal")
            listWidget.addItem("Argentina")
                
            listWidget.itemDoubleClicked.connect(self.onClicked)
            
            vbox.addWidget(listWidget)
            self.setLayout(vbox)

            self.setGeometry(300, 300, 350, 250)
            self.setWindowTitle('QListWidget')
            self.show()


  
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())