from PySide6.QtWidgets import QPlainTextEdit
from PySide6.QtGui import QKeyEvent
from PySide6.QtCore import Qt

class MyPlainTextEdit(QPlainTextEdit):  #父类为QPlainTextEdit

    def __init__(self,parent=None):
        super(MyPlainTextEdit, self).__init__(parent)
        # self.setAcceptRichText(False)

    def keyPressEvent(self, event: QKeyEvent): #重写keyPressEvent方法
        if event.key() == Qt.Key_Return and event.modifiers() == Qt.ControlModifier:#ctrl+回车
            self.insertPlainText('\n')                                              #添加换行
        elif self.toPlainText() and event.key() == Qt.Key_Return:                                          #回车
            self.demo_function() # 调用 demo 函数
        else:
            super().keyPressEvent(event)

    def demo_function(self):
        self.setEnabled(False)          #主函数使用undoAvailable监听信号
        self.setUndoRedoEnabled(False)  #设置焦点
        self.setUndoRedoEnabled(True)   #设置焦点
