# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QStackedWidget, QTreeWidget, QTreeWidgetItem,
    QWidget)

class Ui_Porn_Fetch_Widget(object):
    def setupUi(self, Porn_Fetch_Widget):
        if not Porn_Fetch_Widget.objectName():
            Porn_Fetch_Widget.setObjectName(u"Porn_Fetch_Widget")
        Porn_Fetch_Widget.resize(1758, 829)
        icon = QIcon()
        icon.addFile(u"graphics/logo_transparent.png", QSize(), QIcon.Normal, QIcon.Off)
        Porn_Fetch_Widget.setWindowIcon(icon)
        self.gridLayout_8 = QGridLayout(Porn_Fetch_Widget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.widget = QWidget(Porn_Fetch_Widget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(34, 34, 34);\n"
"border-radius: 10px;")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.button_switch_credits = QPushButton(self.widget)
        self.button_switch_credits.setObjectName(u"button_switch_credits")
        self.button_switch_credits.setMinimumSize(QSize(50, 50))
        self.button_switch_credits.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_switch_credits.setStyleSheet(u"border: none;")
        self.button_switch_credits.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.button_switch_credits, 3, 0, 1, 1)

        self.button_switch_home = QPushButton(self.widget)
        self.button_switch_home.setObjectName(u"button_switch_home")
        self.button_switch_home.setMinimumSize(QSize(50, 50))
        self.button_switch_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_switch_home.setStyleSheet(u"border: none")
        self.button_switch_home.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.button_switch_home, 0, 0, 1, 1)

        self.button_switch_settings = QPushButton(self.widget)
        self.button_switch_settings.setObjectName(u"button_switch_settings")
        self.button_switch_settings.setMinimumSize(QSize(50, 50))
        self.button_switch_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_switch_settings.setStyleSheet(u"border: none;")
        self.button_switch_settings.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.button_switch_settings, 2, 0, 1, 1)

        self.button_switch_search = QPushButton(self.widget)
        self.button_switch_search.setObjectName(u"button_switch_search")
        self.button_switch_search.setMinimumSize(QSize(50, 50))
        self.button_switch_search.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_switch_search.setStyleSheet(u"border: none;")
        self.button_switch_search.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.button_switch_search, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.widget, 0, 0, 3, 2)

        self.widget_status = QWidget(Porn_Fetch_Widget)
        self.widget_status.setObjectName(u"widget_status")
        self.widget_status.setStyleSheet(u"background-color: rgb(34, 34, 34);\n"
"border-radius: 5px;")
        self.gridLayout_5 = QGridLayout(self.widget_status)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_current_progress = QLabel(self.widget_status)
        self.label_current_progress.setObjectName(u"label_current_progress")

        self.gridLayout_2.addWidget(self.label_current_progress, 0, 0, 1, 1)

        self.progressbar_current = QProgressBar(self.widget_status)
        self.progressbar_current.setObjectName(u"progressbar_current")
        self.progressbar_current.setValue(0)

        self.gridLayout_2.addWidget(self.progressbar_current, 0, 1, 1, 1)

        self.label_total_progress = QLabel(self.widget_status)
        self.label_total_progress.setObjectName(u"label_total_progress")

        self.gridLayout_2.addWidget(self.label_total_progress, 1, 0, 1, 1)

        self.progressbar_total = QProgressBar(self.widget_status)
        self.progressbar_total.setObjectName(u"progressbar_total")
        self.progressbar_total.setValue(0)

        self.gridLayout_2.addWidget(self.progressbar_total, 1, 1, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.gridlayout_status = QGridLayout()
        self.gridlayout_status.setObjectName(u"gridlayout_status")
        self.label_total = QLabel(self.widget_status)
        self.label_total.setObjectName(u"label_total")

        self.gridlayout_status.addWidget(self.label_total, 0, 2, 1, 1)

        self.lineedit_error = QLineEdit(self.widget_status)
        self.lineedit_error.setObjectName(u"lineedit_error")
        self.lineedit_error.setReadOnly(True)

        self.gridlayout_status.addWidget(self.lineedit_error, 1, 1, 1, 1)

        self.label_error = QLabel(self.widget_status)
        self.label_error.setObjectName(u"label_error")

        self.gridlayout_status.addWidget(self.label_error, 1, 0, 1, 1)

        self.label_debug = QLabel(self.widget_status)
        self.label_debug.setObjectName(u"label_debug")

        self.gridlayout_status.addWidget(self.label_debug, 1, 2, 1, 1)

        self.label_status = QLabel(self.widget_status)
        self.label_status.setObjectName(u"label_status")

        self.gridlayout_status.addWidget(self.label_status, 0, 0, 1, 1)

        self.lineedit_status = QLineEdit(self.widget_status)
        self.lineedit_status.setObjectName(u"lineedit_status")
        self.lineedit_status.setReadOnly(True)

        self.gridlayout_status.addWidget(self.lineedit_status, 0, 1, 1, 1)

        self.lineedit_total = QLineEdit(self.widget_status)
        self.lineedit_total.setObjectName(u"lineedit_total")
        self.lineedit_total.setReadOnly(True)

        self.gridlayout_status.addWidget(self.lineedit_total, 0, 3, 1, 1)

        self.lineedit_debug = QLineEdit(self.widget_status)
        self.lineedit_debug.setObjectName(u"lineedit_debug")
        self.lineedit_debug.setReadOnly(True)

        self.gridlayout_status.addWidget(self.lineedit_debug, 1, 3, 1, 1)


        self.gridLayout_5.addLayout(self.gridlayout_status, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.widget_status, 2, 2, 1, 1)

        self.stacked_widget_main = QStackedWidget(Porn_Fetch_Widget)
        self.stacked_widget_main.setObjectName(u"stacked_widget_main")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_7 = QGridLayout(self.page_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.stacked_widget_top = QStackedWidget(self.page_3)
        self.stacked_widget_top.setObjectName(u"stacked_widget_top")
        self.stacked_widget_top.setCursor(QCursor(Qt.ArrowCursor))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_6 = QGridLayout(self.page)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridlayout_login_box = QGridLayout()
        self.gridlayout_login_box.setObjectName(u"gridlayout_login_box")
        self.button_get_recommended_videos = QPushButton(self.page)
        self.button_get_recommended_videos.setObjectName(u"button_get_recommended_videos")
        self.button_get_recommended_videos.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_get_recommended_videos.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #444;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    color: #DDD;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                stop:0 #78909C, stop:1 #90A4AE);\n"
"}")

        self.gridlayout_login_box.addWidget(self.button_get_recommended_videos, 3, 2, 1, 1)

        self.label_password = QLabel(self.page)
        self.label_password.setObjectName(u"label_password")

        self.gridlayout_login_box.addWidget(self.label_password, 1, 0, 1, 1)

        self.button_get_liked_videos = QPushButton(self.page)
        self.button_get_liked_videos.setObjectName(u"button_get_liked_videos")
        self.button_get_liked_videos.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_get_liked_videos.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #444;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    color: #DDD;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                stop:0 #78909C, stop:1 #90A4AE);\n"
"}")

        self.gridlayout_login_box.addWidget(self.button_get_liked_videos, 3, 0, 1, 1)

        self.label_username = QLabel(self.page)
        self.label_username.setObjectName(u"label_username")

        self.gridlayout_login_box.addWidget(self.label_username, 0, 0, 1, 1)

        self.button_get_watched_videos = QPushButton(self.page)
        self.button_get_watched_videos.setObjectName(u"button_get_watched_videos")
        self.button_get_watched_videos.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_get_watched_videos.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #444;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    color: #DDD;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                stop:0 #78909C, stop:1 #90A4AE);\n"
"}")

        self.gridlayout_login_box.addWidget(self.button_get_watched_videos, 3, 1, 1, 1)

        self.button_login = QPushButton(self.page)
        self.button_login.setObjectName(u"button_login")
        self.button_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_login.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #444;\n"
"    border-radius: 8px;\n"
"    padding: 5px;\n"
"    color: #DDD;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                stop:0 #5555FF, stop:1 #AA55FF);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                stop:0 #6666FF, stop:1 #BB66FF);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                stop:0 #4444DD, stop:1 #9944DD);\n"
"}")

        self.gridlayout_login_box.addWidget(self.button_login, 2, 0, 1, 4)

        self.lineedit_password = QLineEdit(self.page)
        self.lineedit_password.setObjectName(u"lineedit_password")
        self.lineedit_password.setEchoMode(QLineEdit.Password)

        self.gridlayout_login_box.addWidget(self.lineedit_password, 1, 1, 1, 3)

        self.lineedit_username = QLineEdit(self.page)
        self.lineedit_username.setObjectName(u"lineedit_username")

        self.gridlayout_login_box.addWidget(self.lineedit_username, 0, 1, 1, 3)


        self.gridLayout_6.addLayout(self.gridlayout_login_box, 0, 1, 1, 1)

        self.treeWidget = QTreeWidget(self.page)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setStyleSheet(u"QWidget {\n"
"color: white;\n"
"background-color: rgb(60, 60, 60);\n"
"border: none;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 2px solid #444;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    background-color: #333;\n"
"    color: #DDD;\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid #5599FF;\n"
"}\n"
"\n"
"\n"
"QProgressBar {\n"
"	color: rgb(255, 153, 0);\n"
"    border: 2px solid #5a2a82;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"    background-color: rgb(74, 74, 74);\n"
"    color: #ffffff;  /* Adding text color for better visibility */\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: rgb(0, 255, 224);\n"
"    width: 10px; /* Adjust this to change the width of the 'chunk' */\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: #dcdcdc; /* Light grey text */\n"
"    spacing: 5px; /* Space between the radio button and its label */\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"    border-radius: 7px; /* Circular indicator */\n"
""
                        "}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color: #555; /* Dark background for unchecked state */\n"
"    border: 2px solid #777; /* Slightly lighter border */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #7a7aff; /* Bright color for checked state */\n"
"    border: 2px solid #5a5aff; /* Border slightly darker than the background */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover,\n"
"QRadioButton::indicator:unchecked:hover {\n"
"    border-color: #9a9aff; /* Change border color on hover */\n"
"}\n"
"\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border: 1px solid #5a2a82;\n"
"    height: 8px;\n"
"    background: #e0e0e0;\n"
"    margin: 0px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background: #5a2a82;\n"
"    border: 1px solid #5a2a82;\n"
"    width: 18px;\n"
"    margin: -6px 0;\n"
"    border-radius: 9px;\n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: #e0e0e0;\n"
"}\n"
"\n"
"QSlider::sub-page"
                        ":horizontal {\n"
"    background: #5a2a82;\n"
"}\n"
"QTreeWidget {\n"
"    show-decoration-selected: 1; /* Show selection as a border when the widget is out of focus. */\n"
"    color: #dcdcdc; /* Light grey text */\n"
"    background-color: #555; /* Dark background for the tree */\n"
"    border: 2px solid #777; /* Slightly lighter border for the tree */\n"
"    padding: 5px; /* Space inside the tree */\n"
"}\n"
"\n"
"QTreeWidget::item {\n"
"    border-radius: 7px; /* Rounded corners for each item */\n"
"    border: 2px solid transparent; /* No border by default */\n"
"    padding: 5px; /* Space inside each item */\n"
"    margin: 2px; /* Space between items */\n"
"}\n"
"\n"
"QTreeWidget::item:selected {\n"
"    background-color: #7a7aff; /* Bright color for selected item */\n"
"    border: 2px solid #5a5aff; /* Border slightly darker than the background for selected item */\n"
"}\n"
"\n"
"QTreeWidget::item:hover {\n"
"    border-color: #9a9aff; /* Change border color on hover */\n"
"}\n"
"\n"
"QTreeWidget::b"
                        "ranch {\n"
"    background: #555; /* Background color for branch lines */\n"
"}\n"
"\n"
"QTreeWidget::branch:has-siblings:!adjoins-item {\n"
"    border-image: url(:/images/branch-more.png) 0; /* Custom image for branch lines with more siblings */\n"
"}\n"
"\n"
"QTreeWidget::branch:has-siblings:adjoins-item {\n"
"    border-image: url(:/images/branch-end.png) 0; /* Custom image for last branch line */\n"
"}\n"
"\n"
"QTreeWidget::branch:!has-children:!has-siblings:adjoins-item {\n"
"    border-image: url(:/images/branch-end.png) 0; /* Custom image for a lone branch line */\n"
"}\n"
"\n"
"QGroupBox {\n"
"        border: 0px;\n"
"        margin-top: 1ex; /* Adjust as needed */\n"
"    }\n"
"    QGroupBox::title {\n"
"        subcontrol-origin: margin;\n"
"        subcontrol-position: top center;\n"
"        padding: 0 3px;\n"
"    }\n"
"\n"
"QLabel {\n"
"    color: #DDD;\n"
"    padding: 2px;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid #444;\n"
"    border-radius: 4px;\n"
"    "
                        "padding: 5px;\n"
"    background-color: #333;\n"
"    color: #DDD;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #555;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #5599FF;\n"
"}")

        self.gridLayout_6.addWidget(self.treeWidget, 1, 0, 1, 2)

        self.gridlayout_start_download_box = QGridLayout()
        self.gridlayout_start_download_box.setObjectName(u"gridlayout_start_download_box")
        self.label_file = QLabel(self.page)
        self.label_file.setObjectName(u"label_file")

        self.gridlayout_start_download_box.addWidget(self.label_file, 3, 0, 1, 1)

        self.button_open_file = QPushButton(self.page)
        self.button_open_file.setObjectName(u"button_open_file")
        self.button_open_file.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_open_file.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #444;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    color: #DDD;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                stop:0 #5555FF, stop:1 #AA55FF);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                stop:0 #6666FF, stop:1 #BB66FF);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                stop:0 #4444DD, stop:1 #9944DD);\n"
"}")

        self.gridlayout_start_download_box.addWidget(self.button_open_file, 3, 2, 1, 1)

        self.lineedit_url = QLineEdit(self.page)
        self.lineedit_url.setObjectName(u"lineedit_url")

        self.gridlayout_start_download_box.addWidget(self.lineedit_url, 0, 1, 1, 1)

        self.button_search_videos = QPushButton(self.page)
        self.button_search_videos.setObjectName(u"button_search_videos")
        self.button_search_videos.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_search_videos.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #444;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    color: #DDD;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                stop:0 #5555FF, stop:1 #AA55FF);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                stop:0 #6666FF, stop:1 #BB66FF);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                stop:0 #4444DD, stop:1 #9944DD);\n"
"}")

        self.gridlayout_start_download_box.addWidget(self.button_search_videos, 4, 2, 1, 1)

        self.lineedit_file = QLineEdit(self.page)
        self.lineedit_file.setObjectName(u"lineedit_file")

        self.gridlayout_start_download_box.addWidget(self.lineedit_file, 3, 1, 1, 1)

        self.lineedit_search_query = QLineEdit(self.page)
        self.lineedit_search_query.setObjectName(u"lineedit_search_query")

        self.gridlayout_start_download_box.addWidget(self.lineedit_search_query, 4, 1, 1, 1)

        self.label_model_url = QLabel(self.page)
        self.label_model_url.setObjectName(u"label_model_url")

        self.gridlayout_start_download_box.addWidget(self.label_model_url, 2, 0, 1, 1)

        self.butgton_download = QPushButton(self.page)
        self.butgton_download.setObjectName(u"butgton_download")
        self.butgton_download.setCursor(QCursor(Qt.PointingHandCursor))
        self.butgton_download.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #444;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    color: #DDD;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                stop:0 #5555FF, stop:1 #AA55FF);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                stop:0 #6666FF, stop:1 #BB66FF);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                stop:0 #4444DD, stop:1 #9944DD);\n"
"}")

        self.gridlayout_start_download_box.addWidget(self.butgton_download, 0, 2, 1, 1)

        self.label_search_query = QLabel(self.page)
        self.label_search_query.setObjectName(u"label_search_query")

        self.gridlayout_start_download_box.addWidget(self.label_search_query, 4, 0, 1, 1)

        self.label_url = QLabel(self.page)
        self.label_url.setObjectName(u"label_url")

        self.gridlayout_start_download_box.addWidget(self.label_url, 0, 0, 1, 1)

        self.button_model = QPushButton(self.page)
        self.button_model.setObjectName(u"button_model")
        self.button_model.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_model.setStyleSheet(u"QPushButton {\n"
"    border: 2px solid #444;\n"
"    border-radius: 4px;\n"
"    padding: 5px;\n"
"    color: #DDD;\n"
"    font-weight: bold;\n"
"    font-size: 14px;\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                stop:0 #5555FF, stop:1 #AA55FF);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                stop:0 #6666FF, stop:1 #BB66FF);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,\n"
"                                stop:0 #4444DD, stop:1 #9944DD);\n"
"}")

        self.gridlayout_start_download_box.addWidget(self.button_model, 2, 2, 1, 1)

        self.lineedit_model_url = QLineEdit(self.page)
        self.lineedit_model_url.setObjectName(u"lineedit_model_url")

        self.gridlayout_start_download_box.addWidget(self.lineedit_model_url, 2, 1, 1, 1)


        self.gridLayout_6.addLayout(self.gridlayout_start_download_box, 0, 0, 1, 1)

        self.stacked_widget_top.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_17 = QGridLayout(self.page_2)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridlayout_search_videos = QGridLayout()
        self.gridlayout_search_videos.setObjectName(u"gridlayout_search_videos")
        self.label_search_users = QLabel(self.page_2)
        self.label_search_users.setObjectName(u"label_search_users")

        self.gridlayout_search_videos.addWidget(self.label_search_users, 1, 0, 1, 1)

        self.label_search_pornstars = QLabel(self.page_2)
        self.label_search_pornstars.setObjectName(u"label_search_pornstars")

        self.gridlayout_search_videos.addWidget(self.label_search_pornstars, 2, 0, 1, 1)

        self.lineedit_search_users_query = QLineEdit(self.page_2)
        self.lineedit_search_users_query.setObjectName(u"lineedit_search_users_query")

        self.gridlayout_search_videos.addWidget(self.lineedit_search_users_query, 1, 1, 1, 1)

        self.button_search_category_filters = QPushButton(self.page_2)
        self.button_search_category_filters.setObjectName(u"button_search_category_filters")

        self.gridlayout_search_videos.addWidget(self.button_search_category_filters, 0, 3, 1, 1)

        self.lineedit_search_videos_query = QLineEdit(self.page_2)
        self.lineedit_search_videos_query.setObjectName(u"lineedit_search_videos_query")

        self.gridlayout_search_videos.addWidget(self.lineedit_search_videos_query, 0, 1, 1, 1)

        self.button_filter_users = QPushButton(self.page_2)
        self.button_filter_users.setObjectName(u"button_filter_users")

        self.gridlayout_search_videos.addWidget(self.button_filter_users, 1, 3, 1, 1)

        self.label_search_videos = QLabel(self.page_2)
        self.label_search_videos.setObjectName(u"label_search_videos")

        self.gridlayout_search_videos.addWidget(self.label_search_videos, 0, 0, 1, 1)

        self.button_search_pornstar = QPushButton(self.page_2)
        self.button_search_pornstar.setObjectName(u"button_search_pornstar")

        self.gridlayout_search_videos.addWidget(self.button_search_pornstar, 2, 2, 1, 2)

        self.button_search_users = QPushButton(self.page_2)
        self.button_search_users.setObjectName(u"button_search_users")

        self.gridlayout_search_videos.addWidget(self.button_search_users, 1, 2, 1, 1)

        self.button_search_filters = QPushButton(self.page_2)
        self.button_search_filters.setObjectName(u"button_search_filters")

        self.gridlayout_search_videos.addWidget(self.button_search_filters, 0, 2, 1, 1)

        self.lineedit_search_pornstar_query = QLineEdit(self.page_2)
        self.lineedit_search_pornstar_query.setObjectName(u"lineedit_search_pornstar_query")

        self.gridlayout_search_videos.addWidget(self.lineedit_search_pornstar_query, 2, 1, 1, 1)


        self.gridLayout_17.addLayout(self.gridlayout_search_videos, 0, 0, 1, 1)

        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.groupBox_7 = QGroupBox(self.page_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.gridLayout_13 = QGridLayout(self.groupBox_7)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.radio_memberInterests_into_none = QRadioButton(self.groupBox_7)
        self.radio_memberInterests_into_none.setObjectName(u"radio_memberInterests_into_none")

        self.gridLayout_13.addWidget(self.radio_memberInterests_into_none, 2, 1, 1, 1)

        self.radio_memberInterests_into_male = QRadioButton(self.groupBox_7)
        self.radio_memberInterests_into_male.setObjectName(u"radio_memberInterests_into_male")

        self.gridLayout_13.addWidget(self.radio_memberInterests_into_male, 1, 1, 1, 1)

        self.radio_memberInterests_none = QRadioButton(self.groupBox_7)
        self.radio_memberInterests_none.setObjectName(u"radio_memberInterests_none")

        self.gridLayout_13.addWidget(self.radio_memberInterests_none, 0, 1, 1, 1)

        self.radio_memberInterests_into_female = QRadioButton(self.groupBox_7)
        self.radio_memberInterests_into_female.setObjectName(u"radio_memberInterests_into_female")

        self.gridLayout_13.addWidget(self.radio_memberInterests_into_female, 0, 2, 1, 1)

        self.radio_memberInterests_into_all = QRadioButton(self.groupBox_7)
        self.radio_memberInterests_into_all.setObjectName(u"radio_memberInterests_into_all")

        self.gridLayout_13.addWidget(self.radio_memberInterests_into_all, 1, 2, 1, 1)


        self.gridLayout_16.addWidget(self.groupBox_7, 0, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.page_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setStyleSheet(u"")
        self.gridLayout_15 = QGridLayout(self.groupBox_3)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.radio_otherFilters_none = QRadioButton(self.groupBox_3)
        self.radio_otherFilters_none.setObjectName(u"radio_otherFilters_none")

        self.gridLayout_15.addWidget(self.radio_otherFilters_none, 0, 1, 1, 1)

        self.radio_otherFilters_user_popular = QRadioButton(self.groupBox_3)
        self.radio_otherFilters_user_popular.setObjectName(u"radio_otherFilters_user_popular")

        self.gridLayout_15.addWidget(self.radio_otherFilters_user_popular, 0, 2, 1, 1)

        self.radio_otherFilters_user_newest = QRadioButton(self.groupBox_3)
        self.radio_otherFilters_user_newest.setObjectName(u"radio_otherFilters_user_newest")

        self.gridLayout_15.addWidget(self.radio_otherFilters_user_newest, 1, 1, 1, 1)


        self.gridLayout_16.addWidget(self.groupBox_3, 0, 1, 1, 1)


        self.gridLayout_17.addLayout(self.gridLayout_16, 0, 1, 1, 1)

        self.gridLayout_14 = QGridLayout()
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.groupBox_2 = QGroupBox(self.page_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_3 = QGridLayout(self.groupBox_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.radio_production_none = QRadioButton(self.groupBox_2)
        self.radio_production_none.setObjectName(u"radio_production_none")

        self.gridLayout_3.addWidget(self.radio_production_none, 1, 1, 1, 1)

        self.radio_production_homemade = QRadioButton(self.groupBox_2)
        self.radio_production_homemade.setObjectName(u"radio_production_homemade")

        self.gridLayout_3.addWidget(self.radio_production_homemade, 0, 1, 1, 1)

        self.radio_production_professional = QRadioButton(self.groupBox_2)
        self.radio_production_professional.setObjectName(u"radio_production_professional")

        self.gridLayout_3.addWidget(self.radio_production_professional, 0, 2, 1, 1)


        self.gridLayout_14.addWidget(self.groupBox_2, 0, 1, 1, 1)

        self.groupbox_member_relationship = QGroupBox(self.page_2)
        self.groupbox_member_relationship.setObjectName(u"groupbox_member_relationship")
        self.gridLayout_4 = QGridLayout(self.groupbox_member_relationship)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.radio_memberRelation_single = QRadioButton(self.groupbox_member_relationship)
        self.radio_memberRelation_single.setObjectName(u"radio_memberRelation_single")

        self.gridLayout_4.addWidget(self.radio_memberRelation_single, 0, 3, 1, 1)

        self.radio_memberRelation_open = QRadioButton(self.groupbox_member_relationship)
        self.radio_memberRelation_open.setObjectName(u"radio_memberRelation_open")

        self.gridLayout_4.addWidget(self.radio_memberRelation_open, 0, 2, 1, 1)

        self.radio_memberRelation_taken = QRadioButton(self.groupbox_member_relationship)
        self.radio_memberRelation_taken.setObjectName(u"radio_memberRelation_taken")

        self.gridLayout_4.addWidget(self.radio_memberRelation_taken, 0, 1, 1, 1)

        self.radio_memberRelation_none = QRadioButton(self.groupbox_member_relationship)
        self.radio_memberRelation_none.setObjectName(u"radio_memberRelation_none")

        self.gridLayout_4.addWidget(self.radio_memberRelation_none, 0, 4, 1, 1)


        self.gridLayout_14.addWidget(self.groupbox_member_relationship, 1, 1, 1, 1)

        self.groupBox_4 = QGroupBox(self.page_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_9 = QGridLayout(self.groupBox_4)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.radio_memberType_is_staff = QRadioButton(self.groupBox_4)
        self.radio_memberType_is_staff.setObjectName(u"radio_memberType_is_staff")

        self.gridLayout_9.addWidget(self.radio_memberType_is_staff, 1, 0, 1, 1)

        self.radio_memberType_none = QRadioButton(self.groupBox_4)
        self.radio_memberType_none.setObjectName(u"radio_memberType_none")

        self.gridLayout_9.addWidget(self.radio_memberType_none, 0, 0, 1, 1)

        self.radio_memberType_is_model = QRadioButton(self.groupBox_4)
        self.radio_memberType_is_model.setObjectName(u"radio_memberType_is_model")

        self.gridLayout_9.addWidget(self.radio_memberType_is_model, 0, 1, 1, 1)

        self.radio_memberType_is_online = QRadioButton(self.groupBox_4)
        self.radio_memberType_is_online.setObjectName(u"radio_memberType_is_online")

        self.gridLayout_9.addWidget(self.radio_memberType_is_online, 1, 1, 1, 1)


        self.gridLayout_14.addWidget(self.groupBox_4, 0, 2, 1, 1)

        self.groupBox_6 = QGroupBox(self.page_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setStyleSheet(u"/* QGroupBox */\n"
"QGroupBox {\n"
"    border: 2px solid #4CAF50; /* Border color for the group box */\n"
"    border-radius: 5px;\n"
"    margin-top: 10px; /* Adjust top margin as needed */\n"
"    padding: 0px; /* Add some padding inside the group box */\n"
"}\n"
"\n"
"/* Title text of the QGroupBox */\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center;\n"
"    padding: 0 5px; /* Add padding for title text */\n"
"    background-color: #4CAF50; /* Background color for the title bar */\n"
"    color: white; /* Title text color */\n"
"    border: 1px solid #4CAF50; /* Border color for the title bar */\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"/* Apply style to all child widgets within the QGroupBox */\n"
"QGroupBox QWidget {\n"
"    margin: 5px; /* Adjust margin for child widgets */\n"
"}\n"
"\n"
"/* Style for child QLabel elements within the QGroupBox */\n"
"QGroupBox QLabel {\n"
"    font-weight: bold; /* Make text"
                        " bold for labels */\n"
"}\n"
"\n"
"/* Style for child QPushButton elements within the QGroupBox */\n"
"QGroupBox QPushButton {\n"
"    background-color: #4CAF50; /* Background color for buttons */\n"
"    color: white; /* Button text color */\n"
"    border: 1px solid #4CAF50; /* Button border color */\n"
"    border-radius: 3px; /* Button border radius */\n"
"    padding: 5px 10px; /* Add padding to buttons */\n"
"}\n"
"\n"
"/* Style for child QComboBox elements within the QGroupBox */\n"
"QGroupBox QComboBox {\n"
"    border: 1px solid #4CAF50; /* Border color for combo boxes */\n"
"    border-radius: 3px; /* Combo box border radius */\n"
"    padding: 3px; /* Add padding to combo boxes */\n"
"}\n"
"")
        self.gridLayout_11 = QGridLayout(self.groupBox_6)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.radio_memberGender_trans_male = QRadioButton(self.groupBox_6)
        self.radio_memberGender_trans_male.setObjectName(u"radio_memberGender_trans_male")

        self.gridLayout_11.addWidget(self.radio_memberGender_trans_male, 1, 4, 1, 1)

        self.radio_memberGender_none = QRadioButton(self.groupBox_6)
        self.radio_memberGender_none.setObjectName(u"radio_memberGender_none")

        self.gridLayout_11.addWidget(self.radio_memberGender_none, 0, 4, 1, 1)

        self.radio_memberGender_female_couple = QRadioButton(self.groupBox_6)
        self.radio_memberGender_female_couple.setObjectName(u"radio_memberGender_female_couple")

        self.gridLayout_11.addWidget(self.radio_memberGender_female_couple, 0, 1, 1, 1)

        self.radio_memberGender_female = QRadioButton(self.groupBox_6)
        self.radio_memberGender_female.setObjectName(u"radio_memberGender_female")

        self.gridLayout_11.addWidget(self.radio_memberGender_female, 0, 2, 1, 1)

        self.radio_memberGender_other = QRadioButton(self.groupBox_6)
        self.radio_memberGender_other.setObjectName(u"radio_memberGender_other")

        self.gridLayout_11.addWidget(self.radio_memberGender_other, 0, 3, 1, 1)

        self.radio_memberGender_couple = QRadioButton(self.groupBox_6)
        self.radio_memberGender_couple.setObjectName(u"radio_memberGender_couple")

        self.gridLayout_11.addWidget(self.radio_memberGender_couple, 1, 2, 1, 1)

        self.radio_memberGender_male = QRadioButton(self.groupBox_6)
        self.radio_memberGender_male.setObjectName(u"radio_memberGender_male")

        self.gridLayout_11.addWidget(self.radio_memberGender_male, 1, 3, 1, 1)

        self.radio_memberGender_trans_female = QRadioButton(self.groupBox_6)
        self.radio_memberGender_trans_female.setObjectName(u"radio_memberGender_trans_female")

        self.gridLayout_11.addWidget(self.radio_memberGender_trans_female, 1, 1, 1, 1)

        self.radio_memberGender_non_binary = QRadioButton(self.groupBox_6)
        self.radio_memberGender_non_binary.setObjectName(u"radio_memberGender_non_binary")

        self.gridLayout_11.addWidget(self.radio_memberGender_non_binary, 0, 5, 1, 1)


        self.gridLayout_14.addWidget(self.groupBox_6, 1, 2, 1, 1)

        self.groupBox = QGroupBox(self.page_2)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_12 = QGridLayout(self.groupBox)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.checkbox_sorting_top_rated = QCheckBox(self.groupBox)
        self.checkbox_sorting_top_rated.setObjectName(u"checkbox_sorting_top_rated")

        self.gridLayout_12.addWidget(self.checkbox_sorting_top_rated, 2, 0, 1, 1)

        self.checkbox_sorting_yearly = QCheckBox(self.groupBox)
        self.checkbox_sorting_yearly.setObjectName(u"checkbox_sorting_yearly")

        self.gridLayout_12.addWidget(self.checkbox_sorting_yearly, 1, 0, 1, 1)

        self.checkbox_sorting_views = QCheckBox(self.groupBox)
        self.checkbox_sorting_views.setObjectName(u"checkbox_sorting_views")

        self.gridLayout_12.addWidget(self.checkbox_sorting_views, 1, 3, 1, 1)

        self.checkbox_sorting_all_time = QCheckBox(self.groupBox)
        self.checkbox_sorting_all_time.setObjectName(u"checkbox_sorting_all_time")

        self.gridLayout_12.addWidget(self.checkbox_sorting_all_time, 2, 4, 1, 1)

        self.checkbox_sorting_hd = QCheckBox(self.groupBox)
        self.checkbox_sorting_hd.setObjectName(u"checkbox_sorting_hd")

        self.gridLayout_12.addWidget(self.checkbox_sorting_hd, 1, 4, 1, 1)

        self.checkbox_sorting_weekly = QCheckBox(self.groupBox)
        self.checkbox_sorting_weekly.setObjectName(u"checkbox_sorting_weekly")

        self.gridLayout_12.addWidget(self.checkbox_sorting_weekly, 1, 2, 1, 1)

        self.checkbox_sorting_longest = QCheckBox(self.groupBox)
        self.checkbox_sorting_longest.setObjectName(u"checkbox_sorting_longest")

        self.gridLayout_12.addWidget(self.checkbox_sorting_longest, 2, 3, 1, 1)

        self.checkbox_sorting_recent = QCheckBox(self.groupBox)
        self.checkbox_sorting_recent.setObjectName(u"checkbox_sorting_recent")

        self.gridLayout_12.addWidget(self.checkbox_sorting_recent, 2, 2, 1, 1)

        self.checkbox_sorting_daily = QCheckBox(self.groupBox)
        self.checkbox_sorting_daily.setObjectName(u"checkbox_sorting_daily")

        self.gridLayout_12.addWidget(self.checkbox_sorting_daily, 1, 5, 1, 1)


        self.gridLayout_14.addWidget(self.groupBox, 1, 0, 1, 1)

        self.groupBox_5 = QGroupBox(self.page_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_10 = QGridLayout(self.groupBox_5)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.radio_memberContent_has_playlists = QRadioButton(self.groupBox_5)
        self.radio_memberContent_has_playlists.setObjectName(u"radio_memberContent_has_playlists")

        self.gridLayout_10.addWidget(self.radio_memberContent_has_playlists, 1, 2, 1, 1)

        self.radio_memberContent_none = QRadioButton(self.groupBox_5)
        self.radio_memberContent_none.setObjectName(u"radio_memberContent_none")

        self.gridLayout_10.addWidget(self.radio_memberContent_none, 0, 2, 1, 1)

        self.radio_memberContent_has_videos = QRadioButton(self.groupBox_5)
        self.radio_memberContent_has_videos.setObjectName(u"radio_memberContent_has_videos")

        self.gridLayout_10.addWidget(self.radio_memberContent_has_videos, 0, 0, 1, 1)

        self.radio_memberContent_has_avatar = QRadioButton(self.groupBox_5)
        self.radio_memberContent_has_avatar.setObjectName(u"radio_memberContent_has_avatar")

        self.gridLayout_10.addWidget(self.radio_memberContent_has_avatar, 1, 1, 1, 1)

        self.radio_memberContent_custom_videos = QRadioButton(self.groupBox_5)
        self.radio_memberContent_custom_videos.setObjectName(u"radio_memberContent_custom_videos")

        self.gridLayout_10.addWidget(self.radio_memberContent_custom_videos, 1, 0, 1, 1)

        self.radio_memberContent_has_photos = QRadioButton(self.groupBox_5)
        self.radio_memberContent_has_photos.setObjectName(u"radio_memberContent_has_photos")

        self.gridLayout_10.addWidget(self.radio_memberContent_has_photos, 0, 1, 1, 1)

        self.radio_memberContent_offers_fan_club = QRadioButton(self.groupBox_5)
        self.radio_memberContent_offers_fan_club.setObjectName(u"radio_memberContent_offers_fan_club")

        self.gridLayout_10.addWidget(self.radio_memberContent_offers_fan_club, 0, 3, 1, 1)


        self.gridLayout_14.addWidget(self.groupBox_5, 0, 0, 1, 1)


        self.gridLayout_17.addLayout(self.gridLayout_14, 1, 0, 1, 2)

        self.stacked_widget_top.addWidget(self.page_2)

        self.gridLayout_7.addWidget(self.stacked_widget_top, 0, 0, 1, 1)

        self.stacked_widget_main.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_28 = QGridLayout(self.page_4)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_27 = QGridLayout()
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.groupbox_PERFORMANCE = QGroupBox(self.page_4)
        self.groupbox_PERFORMANCE.setObjectName(u"groupbox_PERFORMANCE")
        self.gridLayout_25 = QGridLayout(self.groupbox_PERFORMANCE)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.groupbox_performance_semaphore = QGroupBox(self.groupbox_PERFORMANCE)
        self.groupbox_performance_semaphore.setObjectName(u"groupbox_performance_semaphore")
        self.gridLayout_22 = QGridLayout(self.groupbox_performance_semaphore)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_semaphore = QLabel(self.groupbox_performance_semaphore)
        self.label_semaphore.setObjectName(u"label_semaphore")

        self.gridLayout_22.addWidget(self.label_semaphore, 0, 0, 1, 1)

        self.button_semaphore_help = QPushButton(self.groupbox_performance_semaphore)
        self.button_semaphore_help.setObjectName(u"button_semaphore_help")

        self.gridLayout_22.addWidget(self.button_semaphore_help, 1, 0, 1, 2)

        self.spinbox_semaphore = QSpinBox(self.groupbox_performance_semaphore)
        self.spinbox_semaphore.setObjectName(u"spinbox_semaphore")
        self.spinbox_semaphore.setMaximum(10)

        self.gridLayout_22.addWidget(self.spinbox_semaphore, 0, 1, 1, 1)


        self.gridLayout_25.addWidget(self.groupbox_performance_semaphore, 1, 1, 1, 1)

        self.groupbox_performance_threading_mode = QGroupBox(self.groupbox_PERFORMANCE)
        self.groupbox_performance_threading_mode.setObjectName(u"groupbox_performance_threading_mode")
        self.gridLayout_19 = QGridLayout(self.groupbox_performance_threading_mode)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.radio_threading_mode_high_performance = QRadioButton(self.groupbox_performance_threading_mode)
        self.radio_threading_mode_high_performance.setObjectName(u"radio_threading_mode_high_performance")

        self.gridLayout_19.addWidget(self.radio_threading_mode_high_performance, 0, 0, 1, 1)

        self.radio_threading_mode_default = QRadioButton(self.groupbox_performance_threading_mode)
        self.radio_threading_mode_default.setObjectName(u"radio_threading_mode_default")

        self.gridLayout_19.addWidget(self.radio_threading_mode_default, 0, 2, 1, 1)

        self.radio_threading_mode_ffmpeg = QRadioButton(self.groupbox_performance_threading_mode)
        self.radio_threading_mode_ffmpeg.setObjectName(u"radio_threading_mode_ffmpeg")

        self.gridLayout_19.addWidget(self.radio_threading_mode_ffmpeg, 0, 1, 1, 1)

        self.button_threading_mode_help = QPushButton(self.groupbox_performance_threading_mode)
        self.button_threading_mode_help.setObjectName(u"button_threading_mode_help")

        self.gridLayout_19.addWidget(self.button_threading_mode_help, 0, 3, 1, 1)


        self.gridLayout_25.addWidget(self.groupbox_performance_threading_mode, 1, 0, 1, 1)

        self.groupbox_performance_threading = QGroupBox(self.groupbox_PERFORMANCE)
        self.groupbox_performance_threading.setObjectName(u"groupbox_performance_threading")
        self.gridLayout_20 = QGridLayout(self.groupbox_performance_threading)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.radio_threading_no = QRadioButton(self.groupbox_performance_threading)
        self.radio_threading_no.setObjectName(u"radio_threading_no")

        self.gridLayout_20.addWidget(self.radio_threading_no, 0, 1, 1, 1)

        self.radio_threading_yes = QRadioButton(self.groupbox_performance_threading)
        self.radio_threading_yes.setObjectName(u"radio_threading_yes")

        self.gridLayout_20.addWidget(self.radio_threading_yes, 0, 0, 1, 1)


        self.gridLayout_25.addWidget(self.groupbox_performance_threading, 0, 0, 1, 2)

        self.groupbox_VIDEO = QGroupBox(self.groupbox_PERFORMANCE)
        self.groupbox_VIDEO.setObjectName(u"groupbox_VIDEO")
        self.gridLayout_26 = QGridLayout(self.groupbox_VIDEO)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.groupbox_video_output = QGroupBox(self.groupbox_VIDEO)
        self.groupbox_video_output.setObjectName(u"groupbox_video_output")
        self.gridLayout_21 = QGridLayout(self.groupbox_video_output)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.label_directory_system = QLabel(self.groupbox_video_output)
        self.label_directory_system.setObjectName(u"label_directory_system")

        self.gridLayout_21.addWidget(self.label_directory_system, 1, 0, 1, 1)

        self.radio_directory_system_yes = QRadioButton(self.groupbox_video_output)
        self.radio_directory_system_yes.setObjectName(u"radio_directory_system_yes")

        self.gridLayout_21.addWidget(self.radio_directory_system_yes, 1, 1, 1, 1)

        self.radio_directory_system_no = QRadioButton(self.groupbox_video_output)
        self.radio_directory_system_no.setObjectName(u"radio_directory_system_no")

        self.gridLayout_21.addWidget(self.radio_directory_system_no, 1, 2, 1, 1)

        self.lineedit_output_path = QLineEdit(self.groupbox_video_output)
        self.lineedit_output_path.setObjectName(u"lineedit_output_path")

        self.gridLayout_21.addWidget(self.lineedit_output_path, 0, 1, 1, 3)

        self.label_output_path = QLabel(self.groupbox_video_output)
        self.label_output_path.setObjectName(u"label_output_path")

        self.gridLayout_21.addWidget(self.label_output_path, 0, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.groupbox_video_output)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_21.addWidget(self.pushButton_3, 0, 4, 1, 1)

        self.pushButton_2 = QPushButton(self.groupbox_video_output)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_21.addWidget(self.pushButton_2, 1, 4, 1, 1)


        self.gridLayout_26.addWidget(self.groupbox_video_output, 1, 0, 1, 1)

        self.groupbox_video_language = QGroupBox(self.groupbox_VIDEO)
        self.groupbox_video_language.setObjectName(u"groupbox_video_language")
        self.gridLayout_24 = QGridLayout(self.groupbox_video_language)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.radio_api_language_german = QRadioButton(self.groupbox_video_language)
        self.radio_api_language_german.setObjectName(u"radio_api_language_german")

        self.gridLayout_24.addWidget(self.radio_api_language_german, 1, 0, 1, 1)

        self.radio_api_language_french = QRadioButton(self.groupbox_video_language)
        self.radio_api_language_french.setObjectName(u"radio_api_language_french")

        self.gridLayout_24.addWidget(self.radio_api_language_french, 2, 0, 1, 1)

        self.radio_api_language_english = QRadioButton(self.groupbox_video_language)
        self.radio_api_language_english.setObjectName(u"radio_api_language_english")

        self.gridLayout_24.addWidget(self.radio_api_language_english, 0, 0, 1, 1)

        self.radio_api_language_chinese = QRadioButton(self.groupbox_video_language)
        self.radio_api_language_chinese.setObjectName(u"radio_api_language_chinese")

        self.gridLayout_24.addWidget(self.radio_api_language_chinese, 0, 1, 1, 1)

        self.radio_api_language_russian = QRadioButton(self.groupbox_video_language)
        self.radio_api_language_russian.setObjectName(u"radio_api_language_russian")

        self.gridLayout_24.addWidget(self.radio_api_language_russian, 1, 1, 1, 1)

        self.radio_language_custom = QRadioButton(self.groupbox_video_language)
        self.radio_language_custom.setObjectName(u"radio_language_custom")

        self.gridLayout_24.addWidget(self.radio_language_custom, 2, 1, 1, 1)


        self.gridLayout_26.addWidget(self.groupbox_video_language, 0, 1, 2, 1)

        self.groupbox_video_quality = QGroupBox(self.groupbox_VIDEO)
        self.groupbox_video_quality.setObjectName(u"groupbox_video_quality")
        self.gridLayout_18 = QGridLayout(self.groupbox_video_quality)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.radio_quality_half = QRadioButton(self.groupbox_video_quality)
        self.radio_quality_half.setObjectName(u"radio_quality_half")

        self.gridLayout_18.addWidget(self.radio_quality_half, 0, 1, 1, 1)

        self.radio_quality_best = QRadioButton(self.groupbox_video_quality)
        self.radio_quality_best.setObjectName(u"radio_quality_best")

        self.gridLayout_18.addWidget(self.radio_quality_best, 0, 0, 1, 1)

        self.radio_quality_least = QRadioButton(self.groupbox_video_quality)
        self.radio_quality_least.setObjectName(u"radio_quality_least")

        self.gridLayout_18.addWidget(self.radio_quality_least, 0, 2, 1, 1)


        self.gridLayout_26.addWidget(self.groupbox_video_quality, 0, 0, 1, 1)


        self.gridLayout_25.addWidget(self.groupbox_VIDEO, 2, 0, 1, 2)

        self.groupbox_searching = QGroupBox(self.groupbox_PERFORMANCE)
        self.groupbox_searching.setObjectName(u"groupbox_searching")
        self.gridLayout_23 = QGridLayout(self.groupbox_searching)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.spinbox_searching = QSpinBox(self.groupbox_searching)
        self.spinbox_searching.setObjectName(u"spinbox_searching")
        self.spinbox_searching.setMaximum(10)

        self.gridLayout_23.addWidget(self.spinbox_searching, 0, 1, 1, 1)

        self.label_searching_limit = QLabel(self.groupbox_searching)
        self.label_searching_limit.setObjectName(u"label_searching_limit")

        self.gridLayout_23.addWidget(self.label_searching_limit, 0, 0, 1, 1)


        self.gridLayout_25.addWidget(self.groupbox_searching, 3, 0, 1, 1)

        self.groupbox_GUI_language = QGroupBox(self.groupbox_PERFORMANCE)
        self.groupbox_GUI_language.setObjectName(u"groupbox_GUI_language")
        self.gridLayout_29 = QGridLayout(self.groupbox_GUI_language)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.radio_ui_language_french = QRadioButton(self.groupbox_GUI_language)
        self.radio_ui_language_french.setObjectName(u"radio_ui_language_french")

        self.gridLayout_29.addWidget(self.radio_ui_language_french, 0, 2, 1, 1)

        self.radio_ui_language_german = QRadioButton(self.groupbox_GUI_language)
        self.radio_ui_language_german.setObjectName(u"radio_ui_language_german")

        self.gridLayout_29.addWidget(self.radio_ui_language_german, 0, 1, 1, 1)

        self.radio_ui_language_english = QRadioButton(self.groupbox_GUI_language)
        self.radio_ui_language_english.setObjectName(u"radio_ui_language_english")

        self.gridLayout_29.addWidget(self.radio_ui_language_english, 0, 0, 1, 1)


        self.gridLayout_25.addWidget(self.groupbox_GUI_language, 3, 1, 1, 1)


        self.gridLayout_27.addWidget(self.groupbox_PERFORMANCE, 0, 0, 1, 1)


        self.gridLayout_28.addLayout(self.gridLayout_27, 0, 0, 1, 1)

        self.stacked_widget_main.addWidget(self.page_4)

        self.gridLayout_8.addWidget(self.stacked_widget_main, 0, 2, 1, 1)


        self.retranslateUi(Porn_Fetch_Widget)

        self.stacked_widget_main.setCurrentIndex(1)
        self.stacked_widget_top.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Porn_Fetch_Widget)
    # setupUi

    def retranslateUi(self, Porn_Fetch_Widget):
        Porn_Fetch_Widget.setWindowTitle(QCoreApplication.translate("Porn_Fetch_Widget", u"Porn_Fetch_Widget", None))
        self.button_switch_credits.setText("")
        self.button_switch_home.setText("")
        self.button_switch_settings.setText("")
        self.button_switch_search.setText("")
        self.label_current_progress.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Current Progress:", None))
        self.label_total_progress.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Total:", None))
        self.label_total.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Total:", None))
        self.label_error.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Error:", None))
        self.label_debug.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Debug:", None))
        self.label_status.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Status:", None))
        self.button_get_recommended_videos.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Get recommended videos", None))
        self.label_password.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Password:", None))
        self.button_get_liked_videos.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Get Liked videos", None))
        self.label_username.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Username:", None))
        self.button_get_watched_videos.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Get watched videos", None))
        self.button_login.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Login", None))
        self.lineedit_password.setPlaceholderText(QCoreApplication.translate("Porn_Fetch_Widget", u"Enter your PornHub Password", None))
        self.lineedit_username.setPlaceholderText(QCoreApplication.translate("Porn_Fetch_Widget", u"Enter your PornHub Username", None))
        self.label_file.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"File:", None))
        self.button_open_file.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Open File", None))
        self.lineedit_url.setPlaceholderText(QCoreApplication.translate("Porn_Fetch_Widget", u"Enter PornHub or HQPorner Video URL", None))
        self.button_search_videos.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Get Videos", None))
        self.lineedit_file.setPlaceholderText(QCoreApplication.translate("Porn_Fetch_Widget", u"Click Open File to select a file, or write the location here and click Open File.    URLs need to be separated with a new line. Supports HQPorner and PornHub", None))
        self.lineedit_search_query.setPlaceholderText(QCoreApplication.translate("Porn_Fetch_Widget", u"Enter a Search Query for PornHub  You can define filters in the settings. The returned videos will be listed down below and you can select them.", None))
        self.label_model_url.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Model URL:", None))
        self.butgton_download.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Download", None))
        self.label_search_query.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Search Query:", None))
        self.label_url.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"URL:", None))
        self.button_model.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Get Videos", None))
        self.lineedit_model_url.setPlaceholderText(QCoreApplication.translate("Porn_Fetch_Widget", u"Enter PornHub Model URL. This can be a Pornstar Account or a PornHub Channel. The videos will be listed down in the TreeWidget", None))
        self.label_search_users.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Search Users", None))
        self.label_search_pornstars.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Search Pornstars", None))
        self.button_search_category_filters.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Category Filter", None))
        self.button_filter_users.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Filters", None))
        self.label_search_videos.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Search Videos", None))
        self.button_search_pornstar.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Search", None))
        self.button_search_users.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Search", None))
        self.button_search_filters.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Search", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Porn_Fetch_Widget", u"Member Interests", None))
        self.radio_memberInterests_into_none.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Into None", None))
        self.radio_memberInterests_into_male.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Into Male", None))
        self.radio_memberInterests_none.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"None", None))
        self.radio_memberInterests_into_female.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Into Female", None))
        self.radio_memberInterests_into_all.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Into All", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Porn_Fetch_Widget", u"Other Filters", None))
        self.radio_otherFilters_none.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"None", None))
        self.radio_otherFilters_user_popular.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"User Popular", None))
        self.radio_otherFilters_user_newest.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"User Newest", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Porn_Fetch_Widget", u"Production Filters (Videos)", None))
        self.radio_production_none.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"None", None))
        self.radio_production_homemade.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Homemade", None))
        self.radio_production_professional.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Professional", None))
        self.groupbox_member_relationship.setTitle(QCoreApplication.translate("Porn_Fetch_Widget", u"Member Relationship", None))
        self.radio_memberRelation_single.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Single", None))
        self.radio_memberRelation_open.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Open Relation", None))
        self.radio_memberRelation_taken.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Taken", None))
        self.radio_memberRelation_none.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"None", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Porn_Fetch_Widget", u"Member Type", None))
        self.radio_memberType_is_staff.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Is Staff", None))
        self.radio_memberType_none.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"None", None))
        self.radio_memberType_is_model.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Is Model", None))
        self.radio_memberType_is_online.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Is Online", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Porn_Fetch_Widget", u"Member Gender", None))
        self.radio_memberGender_trans_male.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Trans Male", None))
        self.radio_memberGender_none.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"None", None))
        self.radio_memberGender_female_couple.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Female Couple", None))
        self.radio_memberGender_female.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Female", None))
        self.radio_memberGender_other.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Other", None))
        self.radio_memberGender_couple.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Couple", None))
        self.radio_memberGender_male.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Male", None))
        self.radio_memberGender_trans_female.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Trans Female", None))
        self.radio_memberGender_non_binary.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Non Binary", None))
        self.groupBox.setTitle(QCoreApplication.translate("Porn_Fetch_Widget", u"Sorting Filters (Videos)", None))
        self.checkbox_sorting_top_rated.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Top rated", None))
        self.checkbox_sorting_yearly.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Yearly", None))
        self.checkbox_sorting_views.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Views", None))
        self.checkbox_sorting_all_time.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"All Time", None))
        self.checkbox_sorting_hd.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"HD", None))
        self.checkbox_sorting_weekly.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Weekly", None))
        self.checkbox_sorting_longest.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Longest", None))
        self.checkbox_sorting_recent.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Recent", None))
        self.checkbox_sorting_daily.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Daily", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Porn_Fetch_Widget", u"Member Content", None))
        self.radio_memberContent_has_playlists.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Has Playlists", None))
        self.radio_memberContent_none.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"None", None))
        self.radio_memberContent_has_videos.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Has Videos", None))
        self.radio_memberContent_has_avatar.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Has Avatar", None))
        self.radio_memberContent_custom_videos.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Offers custom Videos", None))
        self.radio_memberContent_has_photos.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Has Photos", None))
        self.radio_memberContent_offers_fan_club.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Offers Fan Club", None))
        self.groupbox_PERFORMANCE.setTitle(QCoreApplication.translate("Porn_Fetch_Widget", u"Performance Settings", None))
        self.groupbox_performance_semaphore.setTitle(QCoreApplication.translate("Porn_Fetch_Widget", u"Semaphore", None))
        self.label_semaphore.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Semaphore:", None))
        self.button_semaphore_help.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Help", None))
        self.groupbox_performance_threading_mode.setTitle(QCoreApplication.translate("Porn_Fetch_Widget", u"Threading Mode", None))
        self.radio_threading_mode_high_performance.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"High Performance", None))
        self.radio_threading_mode_default.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Default", None))
        self.radio_threading_mode_ffmpeg.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"FFMPEG", None))
        self.button_threading_mode_help.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Help", None))
        self.groupbox_performance_threading.setTitle(QCoreApplication.translate("Porn_Fetch_Widget", u"Threading?", None))
        self.radio_threading_no.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"No", None))
        self.radio_threading_yes.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Yes", None))
        self.groupbox_VIDEO.setTitle(QCoreApplication.translate("Porn_Fetch_Widget", u"Video Settings", None))
        self.groupbox_video_output.setTitle(QCoreApplication.translate("Porn_Fetch_Widget", u"Output", None))
        self.label_directory_system.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Use Directory system? ", None))
        self.radio_directory_system_yes.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Yes", None))
        self.radio_directory_system_no.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"No", None))
        self.lineedit_output_path.setPlaceholderText(QCoreApplication.translate("Porn_Fetch_Widget", u"Enter \"./\" for current directory", None))
        self.label_output_path.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Output path:", None))
        self.pushButton_3.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Select", None))
        self.pushButton_2.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Help", None))
        self.groupbox_video_language.setTitle(QCoreApplication.translate("Porn_Fetch_Widget", u"Language", None))
        self.radio_api_language_german.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"German", None))
        self.radio_api_language_french.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"French", None))
        self.radio_api_language_english.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"English", None))
        self.radio_api_language_chinese.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Chinese", None))
        self.radio_api_language_russian.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Russian", None))
        self.radio_language_custom.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Custom", None))
        self.groupbox_video_quality.setTitle(QCoreApplication.translate("Porn_Fetch_Widget", u"Quality", None))
        self.radio_quality_half.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Half", None))
        self.radio_quality_best.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Best", None))
        self.radio_quality_least.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Least", None))
        self.groupbox_searching.setTitle(QCoreApplication.translate("Porn_Fetch_Widget", u"Searching", None))
        self.label_searching_limit.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"Search Limit:", None))
        self.groupbox_GUI_language.setTitle(QCoreApplication.translate("Porn_Fetch_Widget", u"Graphical User Interface Language", None))
        self.radio_ui_language_french.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"French", None))
        self.radio_ui_language_german.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"German", None))
        self.radio_ui_language_english.setText(QCoreApplication.translate("Porn_Fetch_Widget", u"English", None))
    # retranslateUi

