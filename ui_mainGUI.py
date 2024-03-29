from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QPropertyAnimation
import mysql.connector


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 624)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 500))
        MainWindow.setStyleSheet("background-color: rgb(45, 45, 45);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.top_bar = QtWidgets.QFrame(self.centralwidget)
        self.top_bar.setMaximumSize(QtCore.QSize(16777215, 40))
        self.top_bar.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.top_bar.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.top_bar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.top_bar.setObjectName("top_bar")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.top_bar)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.toggle_frame = QtWidgets.QFrame(self.top_bar)
        self.toggle_frame.setMaximumSize(QtCore.QSize(70, 40))
        self.toggle_frame.setStyleSheet("background-color: rgb(62, 187, 255);")
        self.toggle_frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.toggle_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.toggle_frame.setObjectName("toggle_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.toggle_frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.btn_toggle = QtWidgets.QPushButton(self.toggle_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding,
                                           QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle.sizePolicy().hasHeightForWidth())
        self.btn_toggle.setSizePolicy(sizePolicy)
        self.btn_toggle.setStyleSheet("QPushbutton{\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    border: 0px solid;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "    \n"
                                      "    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.744, y2:0.869818, stop:0 rgba(0, 111, 255, 255), stop:1 rgba(102, 255, 176, 255));\n"
                                      "}")
        self.btn_toggle.setObjectName("btn_toggle")
        self.verticalLayout_2.addWidget(self.btn_toggle)
        self.horizontalLayout.addWidget(self.toggle_frame)
        self.top_frame = QtWidgets.QFrame(self.top_bar)
        self.top_frame.setMaximumSize(QtCore.QSize(16777215, 40))
        self.top_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.top_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.top_frame.setObjectName("top_frame")
        self.horizontalLayout.addWidget(self.top_frame)
        self.verticalLayout.addWidget(self.top_bar)
        self.content = QtWidgets.QFrame(self.centralwidget)
        self.content.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.content.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.content.setObjectName("content")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.content)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.content)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_left_menu.setStyleSheet("background-color: rgb(35, 35, 35);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_left_buttons = QtWidgets.QFrame(self.frame_left_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_left_buttons.sizePolicy().hasHeightForWidth())
        self.frame_left_buttons.setSizePolicy(sizePolicy)
        self.frame_left_buttons.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_left_buttons.setObjectName("frame_left_buttons")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_left_buttons)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.btn_add = QtWidgets.QPushButton(self.frame_left_buttons)
        self.btn_add.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_add.setStyleSheet("QPushButton{\n"
                                   "    \n"
                                   "    background-color: rgb(45, 45, 45);\n"
                                   "    color: rgb(255, 255, 255);\n"
                                   "    border: 1px rgb(255, 255, 255) solid;\n"
                                   "}\n"
                                   "\n"
                                   "QPushButton:hover{\n"
                                   "    \n"
                                   "    background-color: rgb(85, 175, 255);\n"
                                   "}")
        self.btn_add.setObjectName("btn_add")
        self.verticalLayout_4.addWidget(self.btn_add)
        self.btn_search = QtWidgets.QPushButton(self.frame_left_buttons)
        self.btn_search.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_search.setStyleSheet("QPushButton{\n"
                                      "    \n"
                                      "    background-color: rgb(45, 45, 45);\n"
                                      "    color: rgb(255, 255, 255);\n"
                                      "    border: 1px rgb(255, 255, 255) solid;\n"
                                      "}\n"
                                      "\n"
                                      "QPushButton:hover{\n"
                                      "    \n"
                                      "    background-color: rgb(85, 175, 255);\n"
                                      "}")
        self.btn_search.setObjectName("btn_search")
        self.verticalLayout_4.addWidget(self.btn_search)
        self.btn_sell = QtWidgets.QPushButton(self.frame_left_buttons)
        self.btn_sell.setMinimumSize(QtCore.QSize(0, 40))
        self.btn_sell.setStyleSheet("QPushButton{\n"
                                    "    \n"
                                    "    background-color: rgb(45, 45, 45);\n"
                                    "    color: rgb(255, 255, 255);\n"
                                    "    border: 1px rgb(255, 255, 255) solid;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover{\n"
                                    "    \n"
                                    "    background-color: rgb(85, 175, 255);\n"
                                    "}")
        self.btn_sell.setObjectName("btn_sell")
        self.verticalLayout_4.addWidget(self.btn_sell)
        self.verticalLayout_6.addWidget(self.frame_left_buttons, 0, QtCore.Qt.AlignmentFlag.AlignTop)
        self.horizontalLayout_2.addWidget(self.frame_left_menu)
        self.frame_pages = QtWidgets.QFrame(self.content)
        self.frame_pages.setStyleSheet("")
        self.frame_pages.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_pages)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_pages)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidget.setStyleSheet("background-color: rgb(84, 0, 69);")
        self.add_page = QtWidgets.QWidget()
        self.add_page.setObjectName("add_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.add_page)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_addpage_title = QtWidgets.QLabel(self.add_page)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_addpage_title.setFont(font)
        self.label_addpage_title.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_addpage_title.setObjectName("label_addpage_title")
        self.verticalLayout_3.addWidget(self.label_addpage_title)
        self.frame = QtWidgets.QFrame(self.add_page)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_addpage_name = QtWidgets.QLabel(self.frame)
        self.label_addpage_name.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.label_addpage_name.setFont(font)
        self.label_addpage_name.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_addpage_name.setObjectName("label_addpage_name")
        self.horizontalLayout_3.addWidget(self.label_addpage_name)
        self.textEdit_addpage_name = QtWidgets.QTextEdit(self.frame)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        self.textEdit_addpage_name.setFont(font)
        self.textEdit_addpage_name.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                 "font-size: 30px;")
        self.textEdit_addpage_name.setObjectName("textEdit_addpage_name")
        self.horizontalLayout_3.addWidget(self.textEdit_addpage_name)
        self.label_addpage_qty = QtWidgets.QLabel(self.frame)
        self.label_addpage_qty.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.label_addpage_qty.setFont(font)
        self.label_addpage_qty.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_addpage_qty.setObjectName("label_addpage_qty")
        self.horizontalLayout_3.addWidget(self.label_addpage_qty)
        self.textEdit_addpage_qty = QtWidgets.QTextEdit(self.frame)
        self.textEdit_addpage_qty.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        self.textEdit_addpage_qty.setFont(font)
        self.textEdit_addpage_qty.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                "font-size: 30px;")
        self.textEdit_addpage_qty.setObjectName("textEdit_addpage_qty")
        self.horizontalLayout_3.addWidget(self.textEdit_addpage_qty)
        self.verticalLayout_3.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.add_page)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_addpage_price = QtWidgets.QLabel(self.frame_2)
        self.label_addpage_price.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.label_addpage_price.setFont(font)
        self.label_addpage_price.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_addpage_price.setObjectName("label_addpage_price")
        self.horizontalLayout_4.addWidget(self.label_addpage_price)
        self.textEdit_addpage_price = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_addpage_price.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        self.textEdit_addpage_price.setFont(font)
        self.textEdit_addpage_price.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                  "font-size: 30px;")
        self.textEdit_addpage_price.setObjectName("textEdit_addpage_price")
        self.horizontalLayout_4.addWidget(self.textEdit_addpage_price)
        self.label_addpage_strg = QtWidgets.QLabel(self.frame_2)
        self.label_addpage_strg.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.label_addpage_strg.setFont(font)
        self.label_addpage_strg.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_addpage_strg.setObjectName("label_addpage_strg")
        self.horizontalLayout_4.addWidget(self.label_addpage_strg)
        self.textEdit_addpage_storage = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit_addpage_storage.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        self.textEdit_addpage_storage.setFont(font)
        self.textEdit_addpage_storage.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                    "font-size: 30px;")
        self.textEdit_addpage_storage.setObjectName("textEdit_addpage_storage")
        self.horizontalLayout_4.addWidget(self.textEdit_addpage_storage)
        self.btn_addpage_nextItem = QtWidgets.QPushButton(self.frame_2)
        self.btn_addpage_nextItem.setMinimumSize(QtCore.QSize(0, 50))
        self.btn_addpage_nextItem.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.btn_addpage_nextItem.setFont(font)
        self.btn_addpage_nextItem.setStyleSheet("QPushButton{\n"
                                                "    \n"
                                                "    background-color: rgb(45, 45, 45);\n"
                                                "    color: rgb(255, 255, 255);\n"
                                                "    border: 3px rgb(255, 255, 255) solid;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover{\n"
                                                "    \n"
                                                "    background-color: rgb(131, 255, 199);\n"
                                                "}")
        self.btn_addpage_nextItem.setObjectName("btn_addpage_nextItem")
        self.horizontalLayout_4.addWidget(self.btn_addpage_nextItem)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.textEdit_addpage_diplay = QtWidgets.QTextEdit(self.add_page)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        self.textEdit_addpage_diplay.setFont(font)
        self.textEdit_addpage_diplay.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                   "font-size: 30px;")
        self.textEdit_addpage_diplay.setReadOnly(True)
        self.textEdit_addpage_diplay.setObjectName("textEdit_addpage_diplay")
        self.verticalLayout_3.addWidget(self.textEdit_addpage_diplay)
        self.frame_6 = QtWidgets.QFrame(self.add_page)
        self.frame_6.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.btn_addpage_addItems = QtWidgets.QPushButton(self.frame_6)
        self.btn_addpage_addItems.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.btn_addpage_addItems.setFont(font)
        self.btn_addpage_addItems.setStyleSheet("QPushButton{\n"
                                                "    \n"
                                                "    background-color: rgb(45, 45, 45);\n"
                                                "    color: rgb(255, 255, 255);\n"
                                                "    border: 1px rgb(255, 255, 255) solid;\n"
                                                "}\n"
                                                "\n"
                                                "QPushButton:hover{\n"
                                                "    \n"
                                                "    background-color: rgb(131, 255, 199);\n"
                                                "}")
        self.btn_addpage_addItems.setObjectName("btn_addpage_addItems")
        self.horizontalLayout_8.addWidget(self.btn_addpage_addItems)
        self.btn_addpage_clear = QtWidgets.QPushButton(self.frame_6)
        self.btn_addpage_clear.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.btn_addpage_clear.setFont(font)
        self.btn_addpage_clear.setStyleSheet("QPushButton{\n"
                                             "    \n"
                                             "    background-color: rgb(45, 45, 45);\n"
                                             "    color: rgb(255, 255, 255);\n"
                                             "    border: 1px rgb(255, 255, 255) solid;\n"
                                             "}\n"
                                             "\n"
                                             "QPushButton:hover{\n"
                                             "    \n"
                                             "    background-color: rgb(131, 255, 199);\n"
                                             "}")
        self.btn_addpage_clear.setObjectName("btn_addpage_clear")
        self.horizontalLayout_8.addWidget(self.btn_addpage_clear)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.stackedWidget.addWidget(self.add_page)
        self.search_page = QtWidgets.QWidget()
        self.search_page.setObjectName("search_page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.search_page)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_6 = QtWidgets.QLabel(self.search_page)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_7.addWidget(self.label_6)
        self.frame_3 = QtWidgets.QFrame(self.search_page)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_5.addWidget(self.label_7)
        self.textEdit_searchpage_name = QtWidgets.QTextEdit(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        self.textEdit_searchpage_name.setFont(font)
        self.textEdit_searchpage_name.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                    "font-size:30px;")
        self.textEdit_searchpage_name.setObjectName("textEdit_searchpage_name")
        self.horizontalLayout_5.addWidget(self.textEdit_searchpage_name)
        self.verticalLayout_7.addWidget(self.frame_3)
        self.btn_searchpage_searchItem = QtWidgets.QPushButton(self.search_page)
        self.btn_searchpage_searchItem.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.btn_searchpage_searchItem.setFont(font)
        self.btn_searchpage_searchItem.setStyleSheet("QPushButton{\n"
                                                     "    \n"
                                                     "    background-color: rgb(45, 45, 45);\n"
                                                     "    color: rgb(255, 255, 255);\n"
                                                     "    border: 1px rgb(255, 255, 255) solid;\n"
                                                     "}\n"
                                                     "\n"
                                                     "QPushButton:hover{\n"
                                                     "    \n"
                                                     "    background-color: rgb(131, 255, 199);\n"
                                                     "}")
        self.btn_searchpage_searchItem.setObjectName("btn_searchpage_searchItem")
        self.verticalLayout_7.addWidget(self.btn_searchpage_searchItem)
        self.textEdit_searchpage_display = QtWidgets.QTextEdit(self.search_page)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        self.textEdit_searchpage_display.setFont(font)
        self.textEdit_searchpage_display.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                       "font-size:30px;")
        self.textEdit_searchpage_display.setReadOnly(True)
        self.textEdit_searchpage_display.setObjectName("textEdit_searchpage_display")
        self.verticalLayout_7.addWidget(self.textEdit_searchpage_display)
        self.stackedWidget.addWidget(self.search_page)
        self.sell_page = QtWidgets.QWidget()
        self.sell_page.setObjectName("sell_page")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.sell_page)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_10 = QtWidgets.QLabel(self.sell_page)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_10.setObjectName("label_10")
        self.verticalLayout_8.addWidget(self.label_10)
        self.frame_4 = QtWidgets.QFrame(self.sell_page)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        self.label_8.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.textEdit_sellpage_name = QtWidgets.QTextEdit(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        self.textEdit_sellpage_name.setFont(font)
        self.textEdit_sellpage_name.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                  "font-size: 30px;")
        self.textEdit_sellpage_name.setObjectName("textEdit_sellpage_name")
        self.horizontalLayout_6.addWidget(self.textEdit_sellpage_name)
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_6.addWidget(self.label_9)
        self.textEdit_sellpage_qty = QtWidgets.QTextEdit(self.frame_4)
        self.textEdit_sellpage_qty.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        self.textEdit_sellpage_qty.setFont(font)
        self.textEdit_sellpage_qty.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                 "font-size: 30px;")
        self.textEdit_sellpage_qty.setObjectName("textEdit_sellpage_qty")
        self.horizontalLayout_6.addWidget(self.textEdit_sellpage_qty)
        self.btn_sellpage_nextItem = QtWidgets.QPushButton(self.frame_4)
        self.btn_sellpage_nextItem.setMinimumSize(QtCore.QSize(100, 50))
        self.btn_sellpage_nextItem.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.btn_sellpage_nextItem.setFont(font)
        self.btn_sellpage_nextItem.setStyleSheet("QPushButton{\n"
                                                 "    \n"
                                                 "    background-color: rgb(45, 45, 45);\n"
                                                 "    color: rgb(255, 255, 255);\n"
                                                 "    border: 3px rgb(255, 255, 255) solid;\n"
                                                 "}\n"
                                                 "\n"
                                                 "QPushButton:hover{\n"
                                                 "    \n"
                                                 "    background-color: rgb(131, 255, 199);\n"
                                                 "}")
        self.btn_sellpage_nextItem.setObjectName("btn_sellpage_nextItem")
        self.horizontalLayout_6.addWidget(self.btn_sellpage_nextItem)
        self.verticalLayout_8.addWidget(self.frame_4)
        self.textEdit_sellpage_display = QtWidgets.QTextEdit(self.sell_page)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        self.textEdit_sellpage_display.setFont(font)
        self.textEdit_sellpage_display.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                     "font-size: 30px;")
        self.textEdit_sellpage_display.setReadOnly(True)
        self.textEdit_sellpage_display.setObjectName("textEdit_sellpage_display")
        self.verticalLayout_8.addWidget(self.textEdit_sellpage_display)
        self.frame_5 = QtWidgets.QFrame(self.sell_page)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 100))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.frame_5)
        self.label_11.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_7.addWidget(self.label_11)
        self.textEdit_sellpage_total = QtWidgets.QTextEdit(self.frame_5)
        self.textEdit_sellpage_total.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(True)
        self.textEdit_sellpage_total.setFont(font)
        self.textEdit_sellpage_total.setStyleSheet("color: rgb(255, 255, 255);\n"
                                                   "font-size: 30px;")
        self.textEdit_sellpage_total.setReadOnly(True)
        self.textEdit_sellpage_total.setObjectName("textEdit_sellpage_total")
        self.horizontalLayout_7.addWidget(self.textEdit_sellpage_total)
        self.btn_sellpage_sellItems = QtWidgets.QPushButton(self.frame_5)
        self.btn_sellpage_sellItems.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.btn_sellpage_sellItems.setFont(font)
        self.btn_sellpage_sellItems.setStyleSheet("QPushButton{\n"
                                                  "    \n"
                                                  "    background-color: rgb(45, 45, 45);\n"
                                                  "    color: rgb(255, 255, 255);\n"
                                                  "    border: 1px rgb(255, 255, 255) solid;\n"
                                                  "}\n"
                                                  "\n"
                                                  "QPushButton:hover{\n"
                                                  "    \n"
                                                  "    background-color: rgb(131, 255, 199);\n"
                                                  "}")
        self.btn_sellpage_sellItems.setObjectName("btn_sellpage_sellItems")
        self.horizontalLayout_7.addWidget(self.btn_sellpage_sellItems)
        self.btn_sellpage_clear = QtWidgets.QPushButton(self.frame_5)
        self.btn_sellpage_clear.setMinimumSize(QtCore.QSize(100, 50))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        self.btn_sellpage_clear.setFont(font)
        self.btn_sellpage_clear.setStyleSheet("QPushButton{\n"
                                              "    \n"
                                              "    background-color: rgb(45, 45, 45);\n"
                                              "    color: rgb(255, 255, 255);\n"
                                              "    border: 1px rgb(255, 255, 255) solid;\n"
                                              "}\n"
                                              "\n"
                                              "QPushButton:hover{\n"
                                              "    \n"
                                              "    background-color: rgb(131, 255, 199);\n"
                                              "}")
        self.btn_sellpage_clear.setObjectName("btn_sellpage_clear")
        self.horizontalLayout_7.addWidget(self.btn_sellpage_clear)
        self.verticalLayout_8.addWidget(self.frame_5)
        self.stackedWidget.addWidget(self.sell_page)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.horizontalLayout_2.addWidget(self.frame_pages)
        self.verticalLayout.addWidget(self.content)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btn_toggle.clicked.connect(lambda: self.toggle_clicked(140, True))

        #     Pages Management +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.btn_add.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.add_page))
        self.btn_search.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.search_page))
        self.btn_sell.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.sell_page))

        #   functionality section ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        self.btn_addpage_addItems.clicked.connect(lambda: self.addpage_addItems_clicked())
        self.btn_addpage_nextItem.clicked.connect(lambda: self.addpage_nextItem_clicked())
        self.btn_addpage_clear.clicked.connect(lambda: self.addpage_clear_clicked())

        self.btn_searchpage_searchItem.clicked.connect(lambda: self.searchpage_searchItem())

        self.btn_sellpage_nextItem.clicked.connect(lambda: self.sellpage_nextItem_clicked())
        self.btn_sellpage_clear.clicked.connect(lambda: self.sellpage_clear_clicked())
        self.btn_sellpage_sellItems.clicked.connect(lambda: self.sellpage_sellItems_clicked())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Argosy - Manager"))
        self.btn_toggle.setText(_translate("MainWindow", "Menu"))

        self.btn_add.setText(_translate("MainWindow", ""))
        self.btn_add.setIcon(QtGui.QIcon('images/icons8-plus-64.png'))

        self.btn_search.setText(_translate("MainWindow", ""))
        self.btn_search.setIcon(QtGui.QIcon('images/icons8-search-64.png'))

        self.btn_sell.setText(_translate("MainWindow", ""))
        self.btn_sell.setIcon(QtGui.QIcon('images/icons8-minus-64.png'))

        self.label_addpage_title.setText(_translate("MainWindow", "Add Items To Storage"))
        self.label_addpage_name.setText(_translate("MainWindow", "Item Name :"))
        self.label_addpage_qty.setText(_translate("MainWindow", "Quantity :"))
        self.label_addpage_price.setText(_translate("MainWindow", "Price :"))
        self.label_addpage_strg.setText(_translate("MainWindow", "Storage Location :"))
        self.btn_addpage_nextItem.setText(_translate("MainWindow", "Next Item"))
        self.btn_addpage_addItems.setText(_translate("MainWindow", "Add Items"))
        self.btn_addpage_clear.setText(_translate("MainWindow", "Clear"))
        self.label_6.setText(_translate("MainWindow", "Search Items From Storage"))
        self.label_7.setText(_translate("MainWindow", "Item Name :"))
        self.btn_searchpage_searchItem.setText(_translate("MainWindow", "Search Item"))
        self.label_10.setText(_translate("MainWindow", "Sell Items From Storage"))
        self.label_8.setText(_translate("MainWindow", "Item Name :"))
        self.label_9.setText(_translate("MainWindow", "Quantity :"))
        self.btn_sellpage_nextItem.setText(_translate("MainWindow", "Next Item"))
        self.label_11.setText(_translate("MainWindow", "Total Amount :"))
        self.btn_sellpage_sellItems.setText(_translate("MainWindow", "Sell/Remove Items"))
        self.btn_sellpage_clear.setText(_translate("MainWindow", "Clear"))

    def toggle_clicked(self, maxWidth, enable):
        if enable:

            # GET WIDTH
            wid = self.frame_left_menu.width()
            maxExtend = maxWidth
            standard = 70

            # Set Max Width
            if wid == standard:
                widthExtend = maxExtend
                self.btn_add.setText("Add To Storage")
                self.btn_search.setText("Search Storage")
                self.btn_sell.setText("Sell/Remove Item")

            else:
                widthExtend = standard
                self.btn_add.setText("")
                self.btn_search.setIcon(QtGui.QIcon('images/icons8-search-64.png'))
                self.btn_search.setText("")
                self.btn_search.setIcon(QtGui.QIcon('images/icons8-search-64.png'))
                self.btn_sell.setText("")
                self.btn_sell.setIcon(QtGui.QIcon('images/icons8-minus-64.png'))

            # animation
            self.animation = QPropertyAnimation(self.frame_left_menu, b"minimumWidth")
            self.animation.setDuration(400)
            self.animation.setStartValue(wid)
            self.animation.setEndValue(widthExtend)
            self.animation.start()

            if wid == standard:
                self.btn_add.setText("Add To Storage")
                self.btn_search.setText("Search Storage")
                self.btn_sell.setText("Sell/Remove Item")

            else:
                self.btn_add.setText("")
                self.btn_search.setIcon(QtGui.QIcon('images/icons8-search-64.png'))
                self.btn_search.setText("")
                self.btn_search.setIcon(QtGui.QIcon('images/icons8-search-64.png'))
                self.btn_sell.setText("")
                self.btn_sell.setIcon(QtGui.QIcon('images/icons8-minus-64.png'))

    # FUNCTIONALITY PART

    # ADD PAGE

    add_page_buffer_list = list()

    def addpage_nextItem_clicked(self):
        # getting the values
        itemName = self.textEdit_addpage_name.toPlainText()
        quantity = self.textEdit_addpage_qty.toPlainText()
        price = self.textEdit_addpage_price.toPlainText()
        location = self.textEdit_addpage_storage.toPlainText()
        n = self.textEdit_addpage_diplay.toPlainText()

        # clearing everything but display

        self.textEdit_addpage_name.setText("")
        self.textEdit_addpage_price.setText("")
        self.textEdit_addpage_qty.setText("")
        self.textEdit_addpage_storage.setText("")

        if len(itemName) > 49 or len(location) > 4:
            self.textEdit_addpage_name.setText("!enter smaller value!")
            self.textEdit_addpage_storage.setText("!enter smaller value!")
            return

        try:
            self.add_page_buffer_list.append([itemName, int(quantity), int(price), location])
        except Exception:
            self.textEdit_addpage_price.setText("!enter integer value!")
            self.textEdit_addpage_qty.setText("!enter integer value!")
            return

        n = itemName + " " + quantity + " " + price + " " + location + "\n" + n
        self.textEdit_addpage_diplay.setText(n)

    def addpage_clear_clicked(self):
        self.textEdit_addpage_name.setText("")
        self.textEdit_addpage_qty.setText("")
        self.textEdit_addpage_price.setText("")
        self.textEdit_addpage_storage.setText("")
        self.textEdit_addpage_diplay.setText("")
        self.add_page_buffer_list.clear()

    def addpage_addItems_clicked(self):
        self.textEdit_addpage_diplay.setText("")
        try:
            connector = mysql.connector.connect(host="localhost", user="dhruv", password="DGupta@585",
                                                database="argosy")
            cur = connector.cursor()
        except Exception:
            print("failed to connect!")

        try:
            for i in self.add_page_buffer_list:
                cur.execute('''insert into shop_storage(Item_Name, Quantity, Price, Location) 
                value ("{}",{},{},"{}")'''.format(i[0], i[1], i[2], i[3]))
                connector.commit()
            connector.close()

        except Exception:
            print("dump failed")

    # SEARCH PAGE

    def searchpage_searchItem(self):
        itemName = self.textEdit_searchpage_name.toPlainText()
        try:
            connector = mysql.connector.connect(host="localhost", user="dhruv", password="DGupta@585",
                                                database="argosy")
            cur = connector.cursor()
        except Exception:
            print("failed to connect!")

        if itemName != "*":
            try:
                cur.execute('''select Item_Name, Quantity, Price, Location from shop_storage
                where item_Name = "{}"'''.format(itemName))

                rows = cur.fetchall()
                if len(rows) == 0:
                    self.textEdit_searchpage_display.setText("No Such Product Found")


                elif len(rows) >= 0:
                    self.textEdit_searchpage_display.setText("Name Qty Price Location")
                    for i in rows:
                        n = self.textEdit_searchpage_display.toPlainText()
                        n = n + "\n" + "'" + i[0] + "'" + " " + str(i[1]) + " " + str(i[2]) + " " + i[3] + "\n"
                        self.textEdit_searchpage_display.setText(n)
                connector.close()

            except Exception:
                print("failed here at searchpage")

        elif itemName == "*":
            try:
                n = "Name Qty Price Location \n"
                cur.execute("select * from shop_storage")
                rows = cur.fetchall()
                for i in rows:
                    for x in i:
                        if x == i[0]:
                            continue
                        n = n + str(x) + ", "
                    n = n + "\n"

                self.textEdit_searchpage_display.setText(n)

            except Exception:
                print("not working")


    # Sell\Remove PAGE

    sell_page_buffer_list = list()

    def sellpage_nextItem_clicked(self):
        # getting the values
        itemName = self.textEdit_sellpage_name.toPlainText().strip()
        quantity = self.textEdit_sellpage_qty.toPlainText().strip()
        n = self.textEdit_sellpage_display.toPlainText()

        # checks item existance
        try:
            connector = mysql.connector.connect(host="localhost", user="dhruv", password="DGupta@585",
                                                database="argosy")
            cur = connector.cursor()
        except Exception:
            print("failed to connect!")

        try:
            cur.execute('''select Item_Name, Quantity, Price, Location from shop_storage
            where item_Name = "{}"'''.format(itemName))

            rows = list(cur.fetchall())

            if len(rows) == 0:
                self.textEdit_sellpage_name.setText("No Such Product Found")
                self.textEdit_sellpage_qty.setText("")
                return

            if rows[0][1] < int(quantity):
                print("ok")
                self.textEdit_sellpage_qty.setText("Lower Quantity in Storage")
                return

            for i in self.sell_page_buffer_list:
                if i[0] == rows[0][0]:
                    self.textEdit_sellpage_name.setText("Product Already Selected")
                    return

            price = rows[0][2]


        except Exception:
            print("failed here at sellpage")

        # clearing everything but display

        self.textEdit_sellpage_name.setText("")
        self.textEdit_sellpage_qty.setText("")

        try:
            self.sell_page_buffer_list.append([rows[0][0], int(quantity), int(price)])
        except Exception:
            self.textEdit_sellpage_qty.setText("!enter integer value!")
            return

        n = itemName + " " + str(quantity) + " " + str(price) + "\n" + n

        try:
            self.textEdit_sellpage_display.setText(n)
        except Exception:
            print(n)

        x = 0
        for i in self.sell_page_buffer_list:
            x += i[2] * i[1]
        self.textEdit_sellpage_total.setText(str(x))
        connector.close()

    def sellpage_clear_clicked(self):
        self.textEdit_sellpage_name.setText("")
        self.textEdit_sellpage_qty.setText("")
        self.textEdit_sellpage_display.setText("")
        self.textEdit_sellpage_total.setText("")
        self.sell_page_buffer_list.clear()

    def sellpage_sellItems_clicked(self):
        try:
            connector = mysql.connector.connect(host="localhost", user="dhruv", password="DGupta@585",
                                                database="argosy")
            cur = connector.cursor()
        except Exception:
            print("failed to connect!")

        print(self.sell_page_buffer_list)

        for i in self.sell_page_buffer_list:
            cur.execute('select Quantity from shop_storage where Item_Name = "{}"'.format(i[0]))
            qval = cur.fetchone()
            qval = list(qval)

            if int(qval[0]) > i[1]:
                cur.execute(
                    '''update shop_storage set Quantity = Quantity - {} where Item_Name = "{}"'''.format(str(i[1]),
                                                                                                         i[0]))
            elif int(qval[0]) == i[1]:
                cur.execute('delete from shop_storage where Item_Name = "{}"'.format(i[0]))
            else:
                print("unexpected")
            connector.commit()

        # End Step
        connector.close()
        self.sellpage_clear_clicked()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
