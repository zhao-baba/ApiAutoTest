import sys
from PyQt5.QtWidgets import QWidget,QApplication,QLineEdit,QTextEdit,QLabel,QGridLayout

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 创建标签
        title = QLabel('标题')
        author = QLabel('作者')
        text = QLabel('内容')

        # 创建输入框
        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        textEdit = QTextEdit()

        # 创建网格
        grid = QGridLayout()
        # 设定组件之间的距离
        grid.setSpacing(10)

        # 将组件添加到网格中
        grid.addWidget(title,1,1)
        grid.addWidget(titleEdit,1,2)

        grid.addWidget(author,2,1)
        grid.addWidget(authorEdit,2,2)

        grid.addWidget(text,3,1)
        grid.addWidget(textEdit,3,2)

        # 将网格添加到当前窗口中
        self.setLayout(grid)

        self.setGeometry(300,300,350,300)
        self.setWindowTitle('编辑器')
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = Example()
    sys.exit(app.exec_())