import requests
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QAction, QLabel, QTableWidget, QTableWidgetItem, QAbstractItemView, QVBoxLayout, QHBoxLayout, QHeaderView

ip = requests.get('https://ip4.seeip.org/').text

main_api = "https://ipapi.co/"

url = main_api + ip + "/json"

json_data = requests.get(url).json()

    
class IP(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'IP Display' # Window Title
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(30, 30, 500, 400) # Window Size
        
        # IP Information
        
        self.ipText = QLabel(self)
        self.ipText.setText('IP Information')
        self.ipText.move(37, 23)
        self.ipText.setStyleSheet('color : #5f73e3')
        
        self.ipInfo = QLabel(self)
        self.ipInfo.setText('IP : ' + json_data['ip'])
        self.ipInfo.move(37, 50)
        self.ipInfo.setStyleSheet('color : #000000')
        self.ipInfo.setScaledContents(True)
        
        self.networkInfo = QLabel(self)
        self.networkInfo.setText('Network Address : ' + json_data['network'])
        self.networkInfo.move(37, 70)
        self.networkInfo.setStyleSheet('color : #000000')
        self.networkInfo.setScaledContents(True)
        
        self.versionInfo = QLabel(self)
        self.versionInfo.setText('Version : ' + json_data['version'])
        self.versionInfo.move(37, 90)
        self.versionInfo.setStyleSheet('color : #000000')
        self.versionInfo.setScaledContents(True)
        
        self.cityInfo = QLabel(self)
        self.cityInfo.setText('City : ' + json_data['city'])
        self.cityInfo.move(37, 110)
        self.cityInfo.setStyleSheet('color : #000000')
        self.cityInfo.setScaledContents(True)
        
        self.regionInfo = QLabel(self)
        self.regionInfo.setText('Region : ' + json_data['region'])
        self.regionInfo.move(37, 130)
        self.regionInfo.setStyleSheet('color : #000000')
        self.regionInfo.setScaledContents(True)
        
        # Country Information
        
        self.countryText = QLabel(self)
        self.countryText.setText('Country Information')
        self.countryText.move(37, 170)
        self.countryText.setStyleSheet('color : #5f73e3')
        
        self.nameInfo = QLabel(self)
        self.nameInfo.setText('Country : ' + json_data['country_name'])
        self.nameInfo.move(37, 197)
        self.nameInfo.setStyleSheet('color : #000000')
        self.nameInfo.setScaledContents(True)
        
        self.codeInfo = QLabel(self)
        self.codeInfo.setText('Code : ' + json_data['country_code'])
        self.codeInfo.move(37, 217)
        self.codeInfo.setStyleSheet('color : #000000')
        self.codeInfo.setScaledContents(True)
        
        self.capitalInfo = QLabel(self)
        self.capitalInfo.setText('Capital : ' + json_data['country_capital'])
        self.capitalInfo.move(37, 237)
        self.capitalInfo.setStyleSheet('color : #000000')
        self.capitalInfo.setScaledContents(True)
        
         # ISP
        
        self.ispText = QLabel(self)
        self.ispText.setText('ISP')
        self.ispText.move(37, 264)
        self.ispText.setStyleSheet('color : #5f73e3')
        
        self.orgInfo = QLabel(self)
        self.orgInfo.setText('ISP Organization : ' + json_data['org'])
        self.orgInfo.move(37, 291)
        self.orgInfo.setStyleSheet('color : #000000')
        self.orgInfo.setScaledContents(True)
        
        self.show()
     
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Main = IP()
    sys.exit(app.exec_())
