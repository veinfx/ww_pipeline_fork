from PySide2.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton
from controller import Converter_controller
# from model import MyExistingUI  # 기존 UI 클래스 import

class AllUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('IO MANAGER')
        self.layout = QVBoxLayout()
        self.button = QPushButton('My Button')
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        # 컨트롤러 인스턴스 생성
        self.controller = Converter_controller()

        # 버튼 클릭 시 컨트롤러의 메서드 호출
        self.button.clicked.connect(self.controller.do_something)


class IntegrationView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Integration UI')
        self.layout = QHBoxLayout()  # 수평 레이아웃으로 변경
        self.layout.setSpacing(20)  # 버튼 사이 간격 조정

        self.ui1_button = QPushButton('Open Excel File')
        self.ui2_button = QPushButton('Upload to Shotgrid')
        self.ui3_button = QPushButton('Convert to .jpg / .mp4')

        self.layout.addWidget(self.ui1_button)
        self.layout.addWidget(self.ui2_button)
        self.layout.addWidget(self.ui3_button)

        self.setLayout(self.layout)

        self.ui1_button.clicked.connect(self.open_my_ui)
        self.ui2_button.clicked.connect(self.open_ui2)

    def open_my_ui(self):
        self.my_ui = AllUI()  # AllUI 인스턴스 생성
        self.my_ui.show()

    def open_ui2(self):
        self.controller = Converter_controller()  # Converter_controller 인스턴스 생성
        self.controller.show()


def main():
    app = QApplication([])
    integration_view = IntegrationView()
    integration_view.show()
    app.exec_()


if __name__ == '__main__':
    main()
