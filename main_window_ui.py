# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStackedWidget, QTableView,
    QVBoxLayout, QWidget)
import resourse_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u" background: qlineargradient(\n"
"        x1: 0, y1: 0,       /* \u0432\u0435\u0440\u0445\u043d\u0438\u0439 \u043b\u0435\u0432\u044b\u0439 \u0443\u0433\u043e\u043b */\n"
"        x2: 1, y2: 1,       /* \u043d\u0438\u0436\u043d\u0438\u0439 \u043f\u0440\u0430\u0432\u044b\u0439 \u0443\u0433\u043e\u043b */\n"
"        stop: 0 #1e3c72,    /* \u043d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u044b\u0439 \u0441\u0438\u043d\u0438\u0439 */\n"
"        stop: 0.5 #2a5298,  /* \u0431\u0438\u0440\u044e\u0437\u043e\u0432\u044b\u0439 */\n"
"        stop: 1 #1abc9c     /* \u0437\u0435\u043b\u0451\u043d\u044b\u0439, \u0430\u0441\u0441\u043e\u0446\u0438\u0438\u0440\u0443\u044e\u0449\u0438\u0439\u0441\u044f \u0441 \u043f\u0440\u0438\u0440\u043e\u0434\u043e\u0439 */\n"
"    );\n"
"    color: white;           /* \u0446\u0432\u0435\u0442 \u0442\u0435\u043a\u0441\u0442\u0430 \u0434\u043b\u044f \u043a\u043e\u043d\u0442\u0440\u0430\u0441\u0442\u0430 */\n"
"    font-family: \"Segoe UI\", Tahoma, Geneva, Verdana, sans-serif;\n"
"    font"
                        "-size: 14pt;\n"
"\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.pages.setGeometry(QRect(0, 0, 801, 611))
        self.mainpage = QWidget()
        self.mainpage.setObjectName(u"mainpage")
        self.main_buttons = QFrame(self.mainpage)
        self.main_buttons.setObjectName(u"main_buttons")
        self.main_buttons.setGeometry(QRect(270, 180, 271, 201))
        self.main_buttons.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.6);           /* \u0437\u0430\u0442\u0435\u043c\u043d\u0451\u043d\u043d\u044b\u0439 \u043f\u043e\u043b\u0443\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    border: 1px solid rgba(255, 255, 255, 0.8);     /* \u0442\u043e\u043d\u043a\u0430\u044f, \u043d\u043e \u0447\u0451\u0442\u043a\u0430\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    border-radius: 12px;\n"
"    padding: 15px;")
        self.buttonContainer = QVBoxLayout(self.main_buttons)
        self.buttonContainer.setObjectName(u"buttonContainer")
        self.btn_Tours = QPushButton(self.main_buttons)
        self.btn_Tours.setObjectName(u"btn_Tours")
        self.btn_Tours.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;       /* \u043d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u044b\u0439 \u0441\u0438\u043d\u0438\u0439 */\n"
"    color: white;                    /* \u0431\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: none;\n"
"    border-radius: 8px;              /* \u0441\u043a\u0440\u0443\u0433\u043b\u0451\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 10px 20px;              /* \u0432\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"
"    min-width: 120px;\n"
"    transition: background-color 0.3s ease;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;       /* \u0447\u0443\u0442\u044c \u0442\u0435\u043c\u043d\u0435\u0435 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c5980;       /* \u0435\u0449\u0451 \u0442\u0435"
                        "\u043c\u043d\u0435\u0435 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/icons/view_list_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_Tours.setIcon(icon)
        self.btn_Tours.setIconSize(QSize(30, 30))

        self.buttonContainer.addWidget(self.btn_Tours)

        self.btn_Clients = QPushButton(self.main_buttons)
        self.btn_Clients.setObjectName(u"btn_Clients")
        self.btn_Clients.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;       /* \u043d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u044b\u0439 \u0441\u0438\u043d\u0438\u0439 */\n"
"    color: white;                    /* \u0431\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: none;\n"
"    border-radius: 8px;              /* \u0441\u043a\u0440\u0443\u0433\u043b\u0451\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 10px 20px;              /* \u0432\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"
"    min-width: 120px;\n"
"    transition: background-color 0.3s ease;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;       /* \u0447\u0443\u0442\u044c \u0442\u0435\u043c\u043d\u0435\u0435 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c5980;       /* \u0435\u0449\u0451 \u0442\u0435"
                        "\u043c\u043d\u0435\u0435 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/description_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_Clients.setIcon(icon1)
        self.btn_Clients.setIconSize(QSize(30, 30))

        self.buttonContainer.addWidget(self.btn_Clients)

        self.pages.addWidget(self.mainpage)
        self.report_page = QWidget()
        self.report_page.setObjectName(u"report_page")
        self.frame_report = QFrame(self.report_page)
        self.frame_report.setObjectName(u"frame_report")
        self.frame_report.setGeometry(QRect(-10, -10, 811, 611))
        self.frame_report.setStyleSheet(u"background: transparent;")
        self.frame_report.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_report.setFrameShadow(QFrame.Shadow.Raised)
        self.comboBox_report = QComboBox(self.frame_report)
        self.comboBox_report.addItem("")
        self.comboBox_report.addItem("")
        self.comboBox_report.addItem("")
        self.comboBox_report.addItem("")
        self.comboBox_report.addItem("")
        self.comboBox_report.addItem("")
        self.comboBox_report.addItem("")
        self.comboBox_report.addItem("")
        self.comboBox_report.addItem("")
        self.comboBox_report.addItem("")
        self.comboBox_report.addItem("")
        self.comboBox_report.addItem("")
        self.comboBox_report.addItem("")
        self.comboBox_report.addItem("")
        self.comboBox_report.addItem("")
        self.comboBox_report.setObjectName(u"comboBox_report")
        self.comboBox_report.setGeometry(QRect(40, 100, 631, 61))
        self.comboBox_report.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.6);           /* \u0437\u0430\u0442\u0435\u043c\u043d\u0451\u043d\u043d\u044b\u0439 \u043f\u043e\u043b\u0443\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    border: 1px solid rgba(255, 255, 255, 0.8);     /* \u0442\u043e\u043d\u043a\u0430\u044f, \u043d\u043e \u0447\u0451\u0442\u043a\u0430\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    border-radius: 12px;\n"
"    padding: 15px;")
        self.label_report = QLabel(self.frame_report)
        self.label_report.setObjectName(u"label_report")
        self.label_report.setGeometry(QRect(170, 0, 441, 71))
        self.label_report.setStyleSheet(u"background: transparent;\n"
"    color: #ffffff;\n"
"    font-size: 22px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    qproperty-alignment: 'AlignCenter';   /* \u0426\u0435\u043d\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    letter-spacing: 1px;\n"
"    padding: 12px 0;\n"
"    text-shadow: 1px 1px 6px #185a9d;     /* \u041b\u0451\u0433\u043a\u0430\u044f \u0442\u0435\u043d\u044c \u0434\u043b\u044f \u0432\u044b\u0440\u0430\u0437\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438 */")
        self.tableView_report = QTableView(self.frame_report)
        self.tableView_report.setObjectName(u"tableView_report")
        self.tableView_report.setGeometry(QRect(30, 190, 771, 401))
        self.tableView_report.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.6);           /* \u0437\u0430\u0442\u0435\u043c\u043d\u0451\u043d\u043d\u044b\u0439 \u043f\u043e\u043b\u0443\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    border: 1px solid rgba(255, 255, 255, 0.8);     /* \u0442\u043e\u043d\u043a\u0430\u044f, \u043d\u043e \u0447\u0451\u0442\u043a\u0430\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    border-radius: 12px;\n"
"    padding: 15px;")
        self.btn_back_on_report = QPushButton(self.frame_report)
        self.btn_back_on_report.setObjectName(u"btn_back_on_report")
        self.btn_back_on_report.setGeometry(QRect(30, 20, 111, 41))
        self.btn_back_on_report.setStyleSheet(u"QPushButton {\n"
"    background-color: #245a8d;       /* \u0442\u0451\u043c\u043d\u043e-\u0441\u0438\u043d\u0438\u0439 \u0444\u043e\u043d */\n"
"    color: #e0e0e0;                  /* \u0441\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: 2px solid #bfbfbf;       /* \u0441\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u0430\u044f (\u043f\u043e\u0447\u0442\u0438 \u0431\u0435\u043b\u0430\u044f) \u0440\u0430\u043c\u043a\u0430 */\n"
"    border-radius: 8px;\n"
"    padding: 6px 12px;               /* \u0443\u043c\u0435\u043d\u044c\u0448\u0435\u043d\u043d\u044b\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b \u0434\u043b\u044f \u043a\u043e\u043c\u043f\u0430\u043a\u0442\u043d\u043e\u0441\u0442\u0438 */\n"
"    font-size: 16px;                 /* \u0443\u043c\u0435\u043d\u044c\u0448\u0435\u043d\u043d\u044b\u0439 \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    font-weight: 600;\n"
"    min-width: 80px;            "
                        "     /* \u0443\u043c\u0435\u043d\u044c\u0448\u0435\u043d\u043d\u0430\u044f \u043c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0448\u0438\u0440\u0438\u043d\u0430 */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1f4f7a;       /* \u0435\u0449\u0451 \u0442\u0435\u043c\u043d\u0435\u0435 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    border: 2px solid #a0a0a0;       /* \u0447\u0443\u0442\u044c \u0442\u0435\u043c\u043d\u0435\u0435 \u0440\u0430\u043c\u043a\u0430 */\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #173d5a;       /* \u0441\u0430\u043c\u044b\u0439 \u0442\u0451\u043c\u043d\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    border: 2px solid #808080;       /* \u0431\u043e\u043b\u0435\u0435 \u0442\u0451\u043c\u043d\u0430\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    color: #"
                        "dcdcdc;\n"
"}\n"
"\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/arrow_back_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_back_on_report.setIcon(icon2)
        self.pages.addWidget(self.report_page)
        self.table_page = QWidget()
        self.table_page.setObjectName(u"table_page")
        self.frame_table = QFrame(self.table_page)
        self.frame_table.setObjectName(u"frame_table")
        self.frame_table.setGeometry(QRect(0, 0, 801, 601))
        self.frame_table.setStyleSheet(u"background: transparent;")
        self.frame_table.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_table.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_change_table = QFrame(self.frame_table)
        self.frame_change_table.setObjectName(u"frame_change_table")
        self.frame_change_table.setGeometry(QRect(80, 500, 621, 91))
        self.frame_change_table.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.6);           /* \u0437\u0430\u0442\u0435\u043c\u043d\u0451\u043d\u043d\u044b\u0439 \u043f\u043e\u043b\u0443\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    border: 1px solid rgba(255, 255, 255, 0.8);     /* \u0442\u043e\u043d\u043a\u0430\u044f, \u043d\u043e \u0447\u0451\u0442\u043a\u0430\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    border-radius: 12px;\n"
"    padding: 15px;")
        self.horizontalLayout_2 = QHBoxLayout(self.frame_change_table)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_add = QPushButton(self.frame_change_table)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;       /* \u043d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u044b\u0439 \u0441\u0438\u043d\u0438\u0439 */\n"
"    color: white;                    /* \u0431\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: 2px solid white;         /* \u0431\u0435\u043b\u044b\u0439 \u043a\u0440\u0430\u0439 */\n"
"    border-radius: 8px;              /* \u0441\u043a\u0440\u0443\u0433\u043b\u0451\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 10px 20px;              /* \u0432\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"
"    min-width: 120px;\n"
"    transition: background-color 0.3s ease;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;       /* \u0447\u0443\u0442\u044c \u0442\u0435\u043c\u043d\u0435\u0435 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    border: 2px solid w"
                        "hite;         /* \u0431\u0435\u043b\u044b\u0439 \u043a\u0440\u0430\u0439 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c5980;       /* \u0435\u0449\u0451 \u0442\u0435\u043c\u043d\u0435\u0435 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    border: 2px solid white;         /* \u0431\u0435\u043b\u044b\u0439 \u043a\u0440\u0430\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/add_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_add.setIcon(icon3)
        self.btn_add.setIconSize(QSize(25, 25))

        self.horizontalLayout_2.addWidget(self.btn_add)

        self.btn_change = QPushButton(self.frame_change_table)
        self.btn_change.setObjectName(u"btn_change")
        self.btn_change.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;       /* \u043d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u044b\u0439 \u0441\u0438\u043d\u0438\u0439 */\n"
"    color: white;                    /* \u0431\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: 2px solid white;         /* \u0431\u0435\u043b\u044b\u0439 \u043a\u0440\u0430\u0439 */\n"
"    border-radius: 8px;              /* \u0441\u043a\u0440\u0443\u0433\u043b\u0451\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 10px 20px;              /* \u0432\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"
"    min-width: 120px;\n"
"    transition: background-color 0.3s ease;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;       /* \u0447\u0443\u0442\u044c \u0442\u0435\u043c\u043d\u0435\u0435 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    border: 2px solid w"
                        "hite;         /* \u0431\u0435\u043b\u044b\u0439 \u043a\u0440\u0430\u0439 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c5980;       /* \u0435\u0449\u0451 \u0442\u0435\u043c\u043d\u0435\u0435 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    border: 2px solid white;         /* \u0431\u0435\u043b\u044b\u0439 \u043a\u0440\u0430\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/edit_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_change.setIcon(icon4)
        self.btn_change.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btn_change)

        self.btn_delete = QPushButton(self.frame_change_table)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;       /* \u043d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u044b\u0439 \u0441\u0438\u043d\u0438\u0439 */\n"
"    color: white;                    /* \u0431\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: 2px solid white;         /* \u0431\u0435\u043b\u044b\u0439 \u043a\u0440\u0430\u0439 */\n"
"    border-radius: 8px;              /* \u0441\u043a\u0440\u0443\u0433\u043b\u0451\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 10px 20px;              /* \u0432\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b */\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"
"    min-width: 120px;\n"
"    transition: background-color 0.3s ease;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;       /* \u0447\u0443\u0442\u044c \u0442\u0435\u043c\u043d\u0435\u0435 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    border: 2px solid w"
                        "hite;         /* \u0431\u0435\u043b\u044b\u0439 \u043a\u0440\u0430\u0439 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c5980;       /* \u0435\u0449\u0451 \u0442\u0435\u043c\u043d\u0435\u0435 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    border: 2px solid white;         /* \u0431\u0435\u043b\u044b\u0439 \u043a\u0440\u0430\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}\n"
"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/delete_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_delete.setIcon(icon5)
        self.btn_delete.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btn_delete)

        self.tableView_table = QTableView(self.frame_table)
        self.tableView_table.setObjectName(u"tableView_table")
        self.tableView_table.setGeometry(QRect(30, 190, 751, 301))
        self.tableView_table.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.6);           /* \u0437\u0430\u0442\u0435\u043c\u043d\u0451\u043d\u043d\u044b\u0439 \u043f\u043e\u043b\u0443\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    border: 1px solid rgba(255, 255, 255, 0.8);     /* \u0442\u043e\u043d\u043a\u0430\u044f, \u043d\u043e \u0447\u0451\u0442\u043a\u0430\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    border-radius: 12px;\n"
"    padding: 15px;")
        self.comboBox_table = QComboBox(self.frame_table)
        self.comboBox_table.addItem("")
        self.comboBox_table.addItem("")
        self.comboBox_table.addItem("")
        self.comboBox_table.addItem("")
        self.comboBox_table.addItem("")
        self.comboBox_table.addItem("")
        self.comboBox_table.addItem("")
        self.comboBox_table.addItem("")
        self.comboBox_table.addItem("")
        self.comboBox_table.addItem("")
        self.comboBox_table.addItem("")
        self.comboBox_table.addItem("")
        self.comboBox_table.setObjectName(u"comboBox_table")
        self.comboBox_table.setGeometry(QRect(40, 100, 381, 60))
        self.comboBox_table.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.6);           /* \u0437\u0430\u0442\u0435\u043c\u043d\u0451\u043d\u043d\u044b\u0439 \u043f\u043e\u043b\u0443\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    border: 1px solid rgba(255, 255, 255, 0.8);     /* \u0442\u043e\u043d\u043a\u0430\u044f, \u043d\u043e \u0447\u0451\u0442\u043a\u0430\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    border-radius: 12px;\n"
"    padding: 15px;")
        self.label_table = QLabel(self.frame_table)
        self.label_table.setObjectName(u"label_table")
        self.label_table.setGeometry(QRect(130, 0, 511, 58))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(True)
        self.label_table.setFont(font)
        self.label_table.setStyleSheet(u"background: transparent;\n"
"    color: #ffffff;\n"
"    font-size: 22px;\n"
"    font-weight: bold;\n"
"    border: none;\n"
"    qproperty-alignment: 'AlignCenter';   /* \u0426\u0435\u043d\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u0435\u043a\u0441\u0442\u0430 */\n"
"    letter-spacing: 1px;\n"
"    padding: 12px 0;\n"
"    text-shadow: 1px 1px 6px #185a9d;     /* \u041b\u0451\u0433\u043a\u0430\u044f \u0442\u0435\u043d\u044c \u0434\u043b\u044f \u0432\u044b\u0440\u0430\u0437\u0438\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u0438 */")
        self.btn_back_on_table = QPushButton(self.frame_table)
        self.btn_back_on_table.setObjectName(u"btn_back_on_table")
        self.btn_back_on_table.setGeometry(QRect(20, 10, 108, 41))
        self.btn_back_on_table.setStyleSheet(u"QPushButton {\n"
"    background-color: #245a8d;       /* \u0442\u0451\u043c\u043d\u043e-\u0441\u0438\u043d\u0438\u0439 \u0444\u043e\u043d */\n"
"    color: #e0e0e0;                  /* \u0441\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: 2px solid #bfbfbf;       /* \u0441\u0432\u0435\u0442\u043b\u043e-\u0441\u0435\u0440\u0430\u044f (\u043f\u043e\u0447\u0442\u0438 \u0431\u0435\u043b\u0430\u044f) \u0440\u0430\u043c\u043a\u0430 */\n"
"    border-radius: 8px;\n"
"    padding: 6px 12px;               /* \u0443\u043c\u0435\u043d\u044c\u0448\u0435\u043d\u043d\u044b\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b \u0434\u043b\u044f \u043a\u043e\u043c\u043f\u0430\u043a\u0442\u043d\u043e\u0441\u0442\u0438 */\n"
"    font-size: 16px;                 /* \u0443\u043c\u0435\u043d\u044c\u0448\u0435\u043d\u043d\u044b\u0439 \u0440\u0430\u0437\u043c\u0435\u0440 \u0448\u0440\u0438\u0444\u0442\u0430 */\n"
"    font-weight: 600;\n"
"    min-width: 80px;            "
                        "     /* \u0443\u043c\u0435\u043d\u044c\u0448\u0435\u043d\u043d\u0430\u044f \u043c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0448\u0438\u0440\u0438\u043d\u0430 */\n"
"    transition: background-color 0.3s ease, border-color 0.3s ease;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #1f4f7a;       /* \u0435\u0449\u0451 \u0442\u0435\u043c\u043d\u0435\u0435 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    border: 2px solid #a0a0a0;       /* \u0447\u0443\u0442\u044c \u0442\u0435\u043c\u043d\u0435\u0435 \u0440\u0430\u043c\u043a\u0430 */\n"
"    color: #f0f0f0;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #173d5a;       /* \u0441\u0430\u043c\u044b\u0439 \u0442\u0451\u043c\u043d\u044b\u0439 \u0444\u043e\u043d \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    border: 2px solid #808080;       /* \u0431\u043e\u043b\u0435\u0435 \u0442\u0451\u043c\u043d\u0430\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    color: #"
                        "dcdcdc;\n"
"}\n"
"")
        self.btn_back_on_table.setIcon(icon2)
        self.btn_back_on_table.setIconSize(QSize(16, 16))
        self.lineEdit_search = QLineEdit(self.frame_table)
        self.lineEdit_search.setObjectName(u"lineEdit_search")
        self.lineEdit_search.setGeometry(QRect(482, 100, 261, 51))
        self.lineEdit_search.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgba(43, 43, 43, 0.3);\n"
"    color: #f0f0f0;\n"
"    border: 1px solid rgba(240, 240, 240, 0.3);\n"
"    border-radius: 5px;\n"
"    padding: 4px 8px;\n"
"    selection-background-color: rgba(240, 240, 240, 0.4);\n"
"    selection-color: #2b2b2b;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid #a0a0a0;\n"
"    background-color: rgba(43, 43, 43, 0.5);\n"
"}\n"
"")
        self.pages.addWidget(self.table_page)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0422\u0443\u0440\u0438\u0441\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u0430\u0433\u0435\u043d\u0442\u0441\u0442\u0432\u043e", None))
        self.btn_Tours.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0430\u0431\u043b\u0438\u0446\u044b", None))
        self.btn_Clients.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0451\u0442\u044b", None))
        self.comboBox_report.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0432\u0441\u0435\u0445 \u0442\u0443\u0440\u043e\u0432 \u0441 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0435\u0439 \u043e\u0431 \u043e\u0442\u0435\u043b\u0435 \u0438 \u043f\u0435\u0440\u0435\u0432\u043e\u0437\u0447\u0438\u043a\u0435", None))
        self.comboBox_report.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432 \u0441 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e\u043c \u043f\u043e\u043a\u0443\u043f\u043e\u043a", None))
        self.comboBox_report.setItemText(2, QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u044d\u043a\u0441\u043a\u0443\u0440\u0441\u0438\u0439 \u0434\u043b\u044f \u0442\u0443\u0440\u043e\u0432", None))
        self.comboBox_report.setItemText(3, QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u043e\u0432 \u0441 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0435\u0439 \u043e \u043a\u043b\u0438\u0435\u043d\u0442\u0435, \u0442\u0443\u0440\u0435 \u0438 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0435", None))
        self.comboBox_report.setItemText(4, QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u0432 \u0441 \u0443\u043a\u0430\u0437\u0430\u043d\u0438\u0435\u043c \u0438\u0445 \u0434\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u0435\u0439 \u0438 \u043e\u043a\u043b\u0430\u0434\u043e\u0432", None))
        self.comboBox_report.setItemText(5, QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u043e\u0432 \u0441 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0435\u0439 \u043e\u0431 \u043e\u0442\u0435\u043b\u0435 \u0438 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0435", None))
        self.comboBox_report.setItemText(6, QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u043e\u0432 \u0441 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0435\u0439 \u043e\u0431 \u044d\u043a\u0441\u043a\u0443\u0440\u0441\u0438\u0438 \u0438 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0435", None))
        self.comboBox_report.setItemText(7, QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u043e\u0432 \u0441 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0435\u0439 \u043e\u0431 \u043f\u0435\u0440\u0435\u0432\u043e\u0437\u0447\u0438\u043a\u0435 \u0438 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0435", None))
        self.comboBox_report.setItemText(8, QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u043e\u0432, \u043f\u043e \u043a\u043e\u0442\u043e\u0440\u044b\u043c \u043e\u043f\u043b\u0430\u0442\u0430 \u0435\u0449\u0451 \u043d\u0435 \u043f\u0440\u043e\u0438\u0437\u0432\u0435\u0434\u0435\u043d\u0430", None))
        self.comboBox_report.setItemText(9, QCoreApplication.translate("MainWindow", u"\u0421\u0440\u0435\u0434\u043d\u044f\u044f, \u043c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f, \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0446\u0435\u043d\u044b \u0442\u0443\u0440\u043e\u0432 \u043f\u043e \u043a\u0430\u0436\u0434\u043e\u0439 \u0441\u0442\u0440\u0430\u043d\u0435", None))
        self.comboBox_report.setItemText(10, QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043e\u0442\u0435\u043b\u0435\u0439 \u0441 \u043f\u0438\u0442\u0430\u043d\u0438\u0435\u043c \u0438 \u0438\u0445 \u0432\u043c\u0435\u0441\u0442\u0438\u043c\u043e\u0441\u0442\u044c\u044e", None))
        self.comboBox_report.setItemText(11, QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0434\u043e\u0433\u043e\u0432\u043e\u0440\u043e\u0432, \u0437\u0430\u043a\u043b\u044e\u0447\u0451\u043d\u043d\u044b\u0445 \u043a\u0430\u0436\u0434\u044b\u043c \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u043e\u043c", None))
        self.comboBox_report.setItemText(12, QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u043a\u043b\u0438\u0435\u043d\u0442\u043e\u0432, \u043a\u043e\u0442\u043e\u0440\u044b\u0435 \u043d\u0435 \u0441\u043e\u0432\u0435\u0440\u0448\u0430\u043b\u0438 \u043f\u043e\u043a\u0443\u043f\u043e\u043a", None))
        self.comboBox_report.setItemText(13, QCoreApplication.translate("MainWindow", u"\u0421\u043f\u0438\u0441\u043e\u043a \u0442\u0443\u0440\u043e\u0432 \u0441 \u043a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e\u043c \u044d\u043a\u0441\u043a\u0443\u0440\u0441\u0438\u0439 \u0432 \u043a\u0430\u0436\u0434\u043e\u043c", None))
        self.comboBox_report.setItemText(14, QCoreApplication.translate("MainWindow", u"\u041e\u0431\u0449\u0430\u044f \u0432\u044b\u0440\u0443\u0447\u043a\u0430 \u043f\u043e \u043a\u0430\u0436\u0434\u043e\u043c\u0443 \u0442\u0443\u0440\u0443 (\u0446\u0435\u043d\u0430 \u0442\u0443\u0440\u0430 + \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u043f\u0435\u0440\u0435\u0432\u043e\u0437\u043a\u0438 + \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u043f\u0440\u043e\u0436\u0438\u0432\u0430\u043d\u0438\u044f + \u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u044d\u043a\u0441\u043a\u0443\u0440\u0441\u0438\u0439)", None))

        self.label_report.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043e\u0442\u0447\u0451\u0442", None))
        self.btn_back_on_report.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0430\u0437\u0430\u0434", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.btn_change.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.comboBox_table.setItemText(0, QCoreApplication.translate("MainWindow", u"\u0422\u0443\u0440\u044b", None))
        self.comboBox_table.setItemText(1, QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0435\u043b\u0438", None))
        self.comboBox_table.setItemText(2, QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043a\u0443\u0440\u0441\u0438\u0438", None))
        self.comboBox_table.setItemText(3, QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043a\u0443\u0440\u0441\u0438\u0438_\u0442\u0443\u0440\u044b", None))
        self.comboBox_table.setItemText(4, QCoreApplication.translate("MainWindow", u"\u041f\u0435\u0440\u0435\u0432\u043e\u0437\u0447\u0438\u043a\u0438", None))
        self.comboBox_table.setItemText(5, QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0438\u0435\u043d\u0442\u044b", None))
        self.comboBox_table.setItemText(6, QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440\u044b_\u043a\u043b\u0438\u0435\u043d\u0442\u044b", None))
        self.comboBox_table.setItemText(7, QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438", None))
        self.comboBox_table.setItemText(8, QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u0436\u043d\u043e\u0441\u0442\u0438", None))
        self.comboBox_table.setItemText(9, QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440\u044b_\u043f\u0430\u0440\u0442\u043d\u0451\u0440\u044b_\u043e\u0442\u0435\u043b\u0438", None))
        self.comboBox_table.setItemText(10, QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440\u044b_\u043f\u0430\u0440\u0442\u043d\u0451\u0440\u044b_\u044d\u043a\u0441\u043a\u0443\u0440\u0441\u0438\u0438", None))
        self.comboBox_table.setItemText(11, QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0433\u043e\u0432\u043e\u0440\u044b_\u043f\u0430\u0440\u0442\u043d\u0451\u0440\u044b_\u043f\u0435\u0440\u0435\u0432\u043e\u0437\u0447\u0438\u043a\u0438", None))

        self.label_table.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
        self.btn_back_on_table.setText(QCoreApplication.translate("MainWindow", u"\u043d\u0430\u0437\u0430\u0434", None))
        self.lineEdit_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0438\u0441\u043a \u043f\u043e \u0442\u0430\u0431\u043b\u0438\u0446\u0435...", None))
    # retranslateUi

