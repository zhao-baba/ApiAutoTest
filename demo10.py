'''
计算器
'''

import sys
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QGridLayout,QLineEdit,qApp
from PyQt5.QtCore import Qt

class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.screen = QLineEdit('')
        self.screen.setAlignment(Qt.AlignRight)
        self.screen.setReadOnly(True)

        #创建表格布局
        grid = QGridLayout()
        self.setLayout(grid)

        # 按钮标签
        names = ['Cls','Bck','','Close',
                '7','8','9','/',
                '4','5','6','*',
                '1','2','3','-',
                '0','.','=','+'
        ]

        # 将显示器添加到网格中
        grid.addWidget(self.screen,0,0,1,4)
        # 按钮位置从第二行开始
        positions = [(i,j) for i in range(1,6) for j in range(4)]

        # print(tuple(zip(positions,names)))
        # 创建按钮并添加到布局中
        for position,name in zip(positions,names):
            if name=='':
                continue
            #创建按钮
            btn = QPushButton(name)
            # 给按钮绑定操作
            btn.clicked.connect(self.action)
            #将按钮添加到布局中
            grid.addWidget(btn,*position)

        self.move(300,15)
        self.setWindowTitle('计算器')
        self.show()
        
    # 根据按键进行操作
    def action(self):
        # 获取按键的内容
        text = self.sender().text()
        if text == 'Cls':
            self.clear()
        elif text == 'Bck':
            self.backsapce()
        elif text == 'Close':
            qApp.exit()
        elif text == '=':
            self.cacl()
        else:
            self.show_msg(text)

    # 显示信息
    def show_msg(self,text):
        self.screen.setText(self.screen.text()+text)

    # 计算表达式
    def cacl(self):
        try:
            result = eval(self.screen.text())
        except:
            result = 'error'
        finally:
            self.screen.setText(str(result))

    # 清除显示器内容
    def clear(self):
        pass

    # 将屏幕的最后一个字符删除
    def backspace(self):
        pass
      

if __name__ == "__main__":
    app = QApplication(sys.argv)
    example = Example()
    sys.exit(app.exec_())
