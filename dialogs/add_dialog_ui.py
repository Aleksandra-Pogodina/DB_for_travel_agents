# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_dialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QFrame,
    QHBoxLayout, QPushButton, QSizePolicy, QWidget)

class Ui_dialog(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(797, 538)
        dialog.setStyleSheet(u" background: qlineargradient(\n"
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
        self.widget_dialog = QWidget(dialog)
        self.widget_dialog.setObjectName(u"widget_dialog")
        self.widget_dialog.setGeometry(QRect(10, 10, 771, 431))
        self.widget_dialog.setStyleSheet(u"background-color: rgba(0, 0, 0, 0.6);           /* \u0437\u0430\u0442\u0435\u043c\u043d\u0451\u043d\u043d\u044b\u0439 \u043f\u043e\u043b\u0443\u043f\u0440\u043e\u0437\u0440\u0430\u0447\u043d\u044b\u0439 \u0444\u043e\u043d */\n"
"    border: 1px solid rgba(255, 255, 255, 0.8);     /* \u0442\u043e\u043d\u043a\u0430\u044f, \u043d\u043e \u0447\u0451\u0442\u043a\u0430\u044f \u0440\u0430\u043c\u043a\u0430 */\n"
"    border-radius: 12px;\n"
"    padding: 15px;")
        self.formLayoutWidget = QWidget(self.widget_dialog)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(40, 30, 701, 361))
        self.formLayout_dialog = QFormLayout(self.formLayoutWidget)
        self.formLayout_dialog.setObjectName(u"formLayout_dialog")
        self.formLayout_dialog.setContentsMargins(0, 0, 0, 0)
        self.frame_dialog = QFrame(dialog)
        self.frame_dialog.setObjectName(u"frame_dialog")
        self.frame_dialog.setGeometry(QRect(543, 450, 241, 61))
        self.frame_dialog.setStyleSheet(u"background-color: transparent;\n"
"    border: none;")
        self.horizontalLayout = QHBoxLayout(self.frame_dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_save = QPushButton(self.frame_dialog)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;       /* \u043d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u044b\u0439 \u0441\u0438\u043d\u0438\u0439 */\n"
"    color: white;                    /* \u0431\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: 2px solid white;         /* \u0431\u0435\u043b\u044b\u0439 \u043a\u0440\u0430\u0439 */\n"
"    border-radius: 8px;              /* \u0441\u043a\u0440\u0443\u0433\u043b\u0451\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 6px 12px;               /* \u0443\u043c\u0435\u043d\u044c\u0448\u0435\u043d\u043d\u044b\u0435 \u0432\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b (\u0441\u0432\u0435\u0440\u0445\u0443/\u0441\u043d\u0438\u0437\u0443 \u0438 \u0441\u043b\u0435\u0432\u0430/\u0441\u043f\u0440\u0430\u0432\u0430) */\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"
"    min-width: 80px;                 /* \u0443\u043c\u0435\u043d\u044c\u0448\u0435\u043d\u043d\u0430\u044f"
                        " \u043c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0448\u0438\u0440\u0438\u043d\u0430 */\n"
"    transition: background-color 0.3s ease;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;       /* \u0447\u0443\u0442\u044c \u0442\u0435\u043c\u043d\u0435\u0435 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    border: 2px solid white;         /* \u0431\u0435\u043b\u044b\u0439 \u043a\u0440\u0430\u0439 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c5980;       /* \u0435\u0449\u0451 \u0442\u0435\u043c\u043d\u0435\u0435 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    border: 2px solid white;         /* \u0431\u0435\u043b\u044b\u0439 \u043a\u0440\u0430\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btn_save)

        self.btn_cancel = QPushButton(self.frame_dialog)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setStyleSheet(u"QPushButton {\n"
"    background-color: #3498db;       /* \u043d\u0430\u0441\u044b\u0449\u0435\u043d\u043d\u044b\u0439 \u0441\u0438\u043d\u0438\u0439 */\n"
"    color: white;                    /* \u0431\u0435\u043b\u044b\u0439 \u0442\u0435\u043a\u0441\u0442 */\n"
"    border: 2px solid white;         /* \u0431\u0435\u043b\u044b\u0439 \u043a\u0440\u0430\u0439 */\n"
"    border-radius: 8px;              /* \u0441\u043a\u0440\u0443\u0433\u043b\u0451\u043d\u043d\u044b\u0435 \u0443\u0433\u043b\u044b */\n"
"    padding: 6px 12px;               /* \u0443\u043c\u0435\u043d\u044c\u0448\u0435\u043d\u043d\u044b\u0435 \u0432\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0435 \u043e\u0442\u0441\u0442\u0443\u043f\u044b (\u0441\u0432\u0435\u0440\u0445\u0443/\u0441\u043d\u0438\u0437\u0443 \u0438 \u0441\u043b\u0435\u0432\u0430/\u0441\u043f\u0440\u0430\u0432\u0430) */\n"
"    font-size: 16px;\n"
"    font-weight: 600;\n"
"    min-width: 80px;                 /* \u0443\u043c\u0435\u043d\u044c\u0448\u0435\u043d\u043d\u0430\u044f"
                        " \u043c\u0438\u043d\u0438\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0448\u0438\u0440\u0438\u043d\u0430 */\n"
"    transition: background-color 0.3s ease;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #2980b9;       /* \u0447\u0443\u0442\u044c \u0442\u0435\u043c\u043d\u0435\u0435 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"    border: 2px solid white;         /* \u0431\u0435\u043b\u044b\u0439 \u043a\u0440\u0430\u0439 \u043f\u0440\u0438 \u043d\u0430\u0432\u0435\u0434\u0435\u043d\u0438\u0438 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #1c5980;       /* \u0435\u0449\u0451 \u0442\u0435\u043c\u043d\u0435\u0435 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"    border: 2px solid white;         /* \u0431\u0435\u043b\u044b\u0439 \u043a\u0440\u0430\u0439 \u043f\u0440\u0438 \u043d\u0430\u0436\u0430\u0442\u0438\u0438 */\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btn_cancel)


        self.retranslateUi(dialog)

        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0437\u0430\u043f\u0438\u0441\u0438 \u0432 \u0442\u0430\u0431\u043b\u0438\u0446\u0443", None))
        self.btn_save.setText(QCoreApplication.translate("dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.btn_cancel.setText(QCoreApplication.translate("dialog", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
    # retranslateUi

