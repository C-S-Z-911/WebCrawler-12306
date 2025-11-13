# 添加功能包
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
# 从生成的Py文件中调用类
from ui import Ui_Form


# 创建一个类，引入了Ui文件生成的Py文件
class MyWin(QMainWindow, Ui_Form):
    def __init__(self, ):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.rowData(self.lineEdit_2.text(),self.lineEdit.text(),self.lineEdit_3.text()))


# 添加主函数
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mywin = MyWin()
    mywin.show()
    sys.exit(app.exec_())
