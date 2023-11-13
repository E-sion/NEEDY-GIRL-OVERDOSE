from PySide6.QtWidgets import QApplication, QWidget
from ui.menu_easy import Ui_Form


# 显示人物数值的窗口
class menu(QWidget, Ui_Form):
    def __init__(self):
        super(menu, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('控制台')



if __name__ == '__main__':
    app = QApplication([])
    window = menu()
    window.show()
    app.exec()
