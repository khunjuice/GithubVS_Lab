import sys
import random
from PySide.QtCore import*
from PySide.QtGui import*
    

class Animation_area(QWidget):
    def __init__(self):
        super().__init__(None)
        self.setMinimumSize(500,500)

        self.arena_w=500
        self.arena_h=500
        self.x=0
        self.y=0
        self.listy= []
        self.listx= []
        self.timer =QTimer(self)
        self.timer.timeout.connect(self.update_value)
        self.timer.start(5)
        self.press=0
    def Clear(self):
        self.listy= []
        self.listx= []
    def mousePressEvent(self,e):
        self.x =e.pos().x()
        self.y =e.pos().y()
        self.listx.append(self.x)
        self.listy.append(self.y)
        self.press=1
    def mouseReleaseEvent ( self,e ) :
        self.x =e.pos().x()
        self.y =e.pos().y()
        self.listx.append(self.x)
        self.listy.append(self.y)
        self.press=0
    def mouseMoveEvent ( self,e ) :
        self.x =e.pos().x()
        self.y =e.pos().y()
        self.listx.append(self.x)
        self.listy.append(self.y)
    def paintEvent(self,e):
        p = QPainter(self)
        p.setPen(QColor(255,55,140))
        p.setBrush(QColor(255,55,140))
        for i in range(len(self.listx)):
            p.drawEllipse(self.listx[i],self.listy[i],20,20)
        p.end()
    def update_value(self):
        self.update()
class simple_animatoin_window(QWidget):
    def __init__(self):
        super().__init__(None)
        self.anim_area = Animation_area()

        layout = QVBoxLayout()
        layout.addWidget(self.anim_area)
        
        self.setLayout(layout)
        self.setMinimumSize(530,600)
        
        
        self.label = QLabel("Drag the mouse to draw")
        layout.addWidget(self.label)

        self.button = QPushButton("Clear")
        self.button.clicked.connect(self.b_push)
        layout.addWidget(self.button)

        self.setLayout(layout)
    def b_push(self):
        self.anim_area.Clear()

    
def main():
    app= QApplication(sys.argv)
    w = simple_animatoin_window()
    w.show()

    return app.exec_()
if __name__ == "__main__":
    sys.exit(main())
