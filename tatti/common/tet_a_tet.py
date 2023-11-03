import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt, QTimer

class MyWindow(QMainWindow):
   def __init__(self, parent = None):
      super().__init__(parent)

      self.setupUi()
   
   def setupUi(self):
      self.setWindowTitle("NAVBANK")
      self.resize(1280, 720)

      central_widget = QWidget()

      self.setCentralWidget(central_widget)

      layout = QVBoxLayout(central_widget)

      # CSS
      self.setStyleSheet("background-color: #806087")

      self.lbl = QLabel("день добрый", self)
      self.lbl.SetStyleSheet()

      self.lbl_font = QFont()
      # self.lbl_font.setFamily("")
      self.lbl_font.setPointSize(15)
      self.lbl.setStyleSheet("color: white")

      self.lbl.setFont(self.lbl_font)
      # self.lbl.move(100, 50)

      self.lbl.adjustSize()
      self.lbl.setAlignment(Qt.AlignCenter | Qt.AlignTop)

      # Настройка визуализации формы
      horizont_spacer = QSpacerItem(10, 100, QSizePolicy.Expanding, QSizePolicy.Minimum)
      layout.addItem(horizont_spacer)

      layout.setSpacing(10)
      layout.setContentsMargins(400, 0, 400, 100)
      # layout.addStretch(1)

      # Форма для ввода данных
      self.lbl_name = QLabel("Введите своё имя пользователя:", self)
      self.lbl_name.setFont(self.lbl_font)
      self.lbl_name.setStyleSheet("color: white")

      self.input1 = QLineEdit(self)
      self.input1.setFont(self.lbl_font)
      self.input1.setStyleSheet("color: white")
      
      self.lbl_password = QLabel("Введите пароль:", self)
      self.lbl_password.setFont(self.lbl_font)
      self.lbl_password.setStyleSheet("color: white")

      self.input2 = QLineEdit(self)
      self.input2.setFont(self.lbl_font)
      self.input2.setStyleSheet("color: white")

      self.button = QPushButton("Войти", self)
      self.button.setFont(self.lbl_font)
      self.button.setStyleSheet("color: white")
      self.button.clicked.connect(self.login)

      
      self.lbl_status = QLabel("",self)
      self.lbl_status.setFont(self.lbl_font)
      self.lbl_status.setStyleSheet("color: red")

      layout.addWidget(self.lbl)
      layout.addWidget(self.lbl_name)
      layout.addWidget(self.input1)
      layout.addWidget(self.lbl_password)
      layout.addWidget(self.input2)
      layout.addWidget(self.button)
      layout.addWidget(self.lbl_status)
   def login(self):
      username = self.input1.text()
      password = self.input2.text()
      if username!="pauel" or password!="123":
        self.lbl_status.setText("Данные введены неверно")
        self.lbl_status.setStyleSheet("color:red")
        print("данные введены неверно")
      else:
        self.lbl_status.setText("Данные введены верно")
        self.lbl_status.setStyleSheet("color:green")

        timer=QTimer(self)
        timer.singleShot(5000,self.close_app)
   def close_app(self):
        self.close()


app = QApplication(sys.argv)
win = MyWindow()

win.show()

sys.exit(app.exec_())