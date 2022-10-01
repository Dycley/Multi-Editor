# -*- coding: utf-8 -*-
# @Author: YokDen
# @Time: 2022/10/1
# @Email: dyk_693@qq.com

import os
import sys

import chardet
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QTextCursor, QPalette
from PyQt5.QtWidgets import QMdiSubWindow, QTextEdit, QFileDialog, QMainWindow, QWidget, QFontDialog, QColorDialog, \
    QMessageBox


class Ui_Editor(QWidget):
    def __init__(self):
        super(Ui_Editor, self).__init__()
        self.search_box = Ui_SearchBox()
        self.search_box.setWindowModality(Qt.ApplicationModal)
        self.search_box.setupUi(self.search_box)

    def setupUi(self, Editor):
        Editor.setObjectName("Editor")
        Editor.resize(1600, 1400)
        Editor.setWindowIcon(QIcon("images/note.png"))
        self.centralwidget = QtWidgets.QWidget(Editor)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName("mdiArea")
        self.verticalLayout.addWidget(self.mdiArea)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        Editor.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Editor)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 844, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menubar)
        self.menu_4.setObjectName("menu_4")
        Editor.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Editor)
        self.statusbar.setObjectName("statusbar")
        Editor.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(Editor)
        self.toolBar.setObjectName("toolBar")
        Editor.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.action_new = QtWidgets.QAction(Editor)
        self.action_new.setObjectName("action_new")
        self.action_open = QtWidgets.QAction(Editor)
        self.action_open.setObjectName("action_open")
        self.action_save = QtWidgets.QAction(Editor)
        self.action_save.setObjectName("action_save")
        self.action_saveas = QtWidgets.QAction(Editor)
        self.action_saveas.setObjectName("action_saveas")
        self.action_close = QtWidgets.QAction(Editor)
        self.action_close.setObjectName("action_close")
        self.action_about = QtWidgets.QAction(Editor)
        self.action_about.setObjectName("action_about")
        self.actioncascade = QtWidgets.QAction(Editor)
        self.actioncascade.setObjectName("actionpile")
        self.actiontile = QtWidgets.QAction(Editor)
        self.actiontile.setObjectName("actionverti")
        self.actioncut = QtWidgets.QAction(Editor)
        self.actioncut.setObjectName("actioncut")
        self.actioncopy = QtWidgets.QAction(Editor)
        self.actioncopy.setObjectName("actioncopy")
        self.actionpaste = QtWidgets.QAction(Editor)
        self.actionpaste.setObjectName("actionpaste")
        self.actionfont = QtWidgets.QAction(Editor)
        self.actionfont.setObjectName("actionfont")
        self.actioncolor = QtWidgets.QAction(Editor)
        self.actioncolor.setObjectName("actioncolor")
        self.actionsearch = QtWidgets.QAction(Editor)
        self.actionsearch.setObjectName("actionsearch")
        self.aleft = QtWidgets.QAction(Editor)
        self.aleft.setObjectName("aleft")
        self.amid = QtWidgets.QAction(Editor)
        self.amid.setObjectName("amid")
        self.aright = QtWidgets.QAction(Editor)
        self.aright.setObjectName("aright")
        self.undo = QtWidgets.QAction(Editor)
        self.undo.setObjectName("undo")
        self.redo = QtWidgets.QAction(Editor)
        self.redo.setObjectName("redo")
        self.menu.addAction(self.action_new)
        self.menu.addAction(self.action_open)
        self.menu.addAction(self.action_save)
        self.menu.addAction(self.action_saveas)
        self.menu.addSeparator()
        self.menu.addAction(self.action_close)
        self.menu_2.addAction(self.actioncut)
        self.menu_2.addAction(self.actioncopy)
        self.menu_2.addAction(self.actionpaste)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionfont)
        self.menu_2.addAction(self.actioncolor)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.undo)
        self.menu_2.addAction(self.redo)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.actionsearch)
        self.menu_3.addAction(self.actioncascade)
        self.menu_3.addAction(self.actiontile)
        self.menu_4.addAction(self.action_about)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())

        self.retranslateUi(Editor)
        QtCore.QMetaObject.connectSlotsByName(Editor)

        self.action_init()
        self.toolbar_init()
        self.connector()

    def retranslateUi(self, Editor):
        _translate = QtCore.QCoreApplication.translate
        Editor.setWindowTitle(_translate("Editor", "TextEditor"))
        self.menu.setTitle(_translate("Editor", "文件"))
        self.menu_2.setTitle(_translate("Editor", "编辑"))
        self.menu_3.setTitle(_translate("Editor", "视图"))
        self.menu_4.setTitle(_translate("Editor", "帮助"))
        self.toolBar.setWindowTitle(_translate("Editor", "toolBar"))
        self.action_new.setText(_translate("Editor", "新建"))
        self.action_open.setText(_translate("Editor", "打开"))
        self.action_save.setText(_translate("Editor", "保存"))
        self.action_saveas.setText(_translate("Editor", "另存为..."))
        self.action_close.setText(_translate("Editor", "关闭"))
        self.action_about.setText(_translate("Editor", "关于"))
        self.actioncascade.setText(_translate("Editor", "级联显示"))
        self.actiontile.setText(_translate("Editor", "平铺显示"))
        self.actioncut.setText(_translate("Editor", "剪切"))
        self.actioncopy.setText(_translate("Editor", "复制"))
        self.actionpaste.setText(_translate("Editor", "粘贴"))
        self.actionfont.setText(_translate("Editor", "字体"))
        self.actioncolor.setText(_translate("Editor", "颜色"))
        self.actionsearch.setText(_translate("Editor", "查找替换"))
        self.aleft.setText(_translate("Editor", "左对齐"))
        self.amid.setText(_translate("Editor", "居中对齐"))
        self.aright.setText(_translate("Editor", "右对齐"))
        self.undo.setText(_translate("Editor", "撤回"))
        self.redo.setText(_translate("Editor", "前进"))

    # 菜单栏初始化
    def action_init(self):
        self.action_new.setIcon(QIcon('images/new.png'))
        self.action_new.setShortcut('Ctrl+N')
        self.action_new.setToolTip('新建')
        self.action_new.setStatusTip('新建文件')

        self.action_open.setIcon(QIcon('images/open.png'))
        self.action_open.setShortcut('Ctrl+O')
        self.action_open.setToolTip('打开')
        self.action_open.setStatusTip('打开文件')

        self.action_save.setIcon(QIcon('images/save.png'))
        self.action_save.setShortcut('Ctrl+S')
        self.action_save.setToolTip('保存')
        self.action_save.setStatusTip('保存文件')

        self.action_saveas.setIcon(QIcon('images/saveas.png'))
        self.action_saveas.setStatusTip('保存文件')

        self.action_close.setIcon(QIcon('images/close.png'))

        self.actioncut.setIcon(QIcon('images/cut.png'))
        self.actioncut.setShortcut('Ctrl+X')
        self.actioncut.setToolTip('剪切')
        self.actioncut.setStatusTip('剪切选中部分')

        self.actioncopy.setIcon(QIcon('images/copy.png'))
        self.actioncopy.setShortcut('Ctrl+C')
        self.actioncopy.setToolTip('复制')
        self.actioncopy.setStatusTip('复制选中部分')

        self.actionpaste.setIcon(QIcon('images/paste.png'))
        self.actionpaste.setShortcut('Ctrl+V')
        self.actionpaste.setToolTip('粘贴')
        self.actionpaste.setStatusTip('粘贴文字')

        self.actioncascade.setIcon(QIcon('images/cascade.png'))
        self.actioncascade.setStatusTip('级联展示')

        self.actiontile.setIcon(QIcon('images/tile.png'))
        self.actiontile.setStatusTip('平铺展示')

        self.undo.setIcon(QIcon('images/undo.png'))
        self.undo.setShortcut('Ctrl+Z')
        self.undo.setToolTip('撤回')
        self.undo.setStatusTip('撤回')

        self.redo.setIcon(QIcon('images/redo.png'))
        self.redo.setShortcut('Ctrl+Y')
        self.redo.setToolTip('前进')
        self.redo.setStatusTip('取消撤回')

        self.aleft.setIcon(QIcon('images/left.png'))
        self.aleft.setToolTip('左对齐')
        self.aleft.setStatusTip('左对齐')
        self.aright.setIcon(QIcon('images/right.png'))
        self.aright.setToolTip('右对齐')
        self.aright.setStatusTip('右对齐')
        self.amid.setIcon(QIcon('images/center.png'))
        self.amid.setToolTip('居中对齐')
        self.amid.setStatusTip('居中对齐')

        self.actioncolor.setIcon(QIcon('images/color.png'))
        self.actioncolor.setToolTip('颜色')
        self.actioncolor.setStatusTip('设置颜色')

        self.actionfont.setIcon(QIcon('images/font.png'))
        self.actionfont.setToolTip('字体')
        self.actionfont.setStatusTip('设置字体')

        self.actionsearch.setIcon(QIcon('images/search.png'))
        self.actionsearch.setToolTip('查找替换')
        self.actionsearch.setStatusTip('查找替换')

        self.action_about.setIcon(QIcon('images/about.png'))
        self.action_about.setStatusTip('关于')

    # 工具栏初始化
    def toolbar_init(self):
        self.toolBar.addActions([self.action_new, self.action_open, self.action_save])
        self.toolBar.addActions([self.actionfont, self.actioncolor])
        self.toolBar.addActions([self.undo, self.redo])
        self.toolBar.addActions([self.aleft, self.amid, self.aright])
        self.toolBar.addActions([self.actioncut, self.actioncopy, self.actionpaste])
        self.toolBar.addActions([self.actionsearch])

    def connector(self):
        self.action_close.triggered.connect(sub.close)
        self.action_new.triggered.connect(self.new_fun)
        self.action_open.triggered.connect(self.open_fun)
        self.action_save.triggered.connect(self.save_fun)
        self.action_saveas.triggered.connect(self.saveas_fun)
        self.actioncut.triggered.connect(
            lambda: self.mdiArea.activeSubWindow().widget().cut() if self.mdiArea.subWindowList() else None)
        self.actioncopy.triggered.connect(
            lambda: self.mdiArea.activeSubWindow().widget().copy() if self.mdiArea.subWindowList() else None)
        self.actionpaste.triggered.connect(
            lambda: self.mdiArea.activeSubWindow().widget().paste() if self.mdiArea.subWindowList() else None)
        self.actioncascade.triggered.connect(self.mdiArea.cascadeSubWindows)
        self.actiontile.triggered.connect(self.mdiArea.tileSubWindows)
        self.undo.triggered.connect(
            lambda: self.mdiArea.activeSubWindow().widget().undo() if self.mdiArea.subWindowList() else None)
        self.redo.triggered.connect(
            lambda: self.mdiArea.activeSubWindow().widget().redo() if self.mdiArea.subWindowList() else None)
        self.aleft.triggered.connect(lambda: self.mdiArea.activeSubWindow().widget().setAlignment(
            Qt.AlignLeft) if self.mdiArea.subWindowList() else None)
        self.aright.triggered.connect(lambda: self.mdiArea.activeSubWindow().widget().setAlignment(
            Qt.AlignRight) if self.mdiArea.subWindowList() else None)
        self.amid.triggered.connect(lambda: self.mdiArea.activeSubWindow().widget().setAlignment(
            Qt.AlignCenter) if self.mdiArea.subWindowList() else None)
        self.actionfont.triggered.connect(self.set_font)
        self.actioncolor.triggered.connect(self.set_color)
        self.action_about.triggered.connect(self.about)
        self.actionsearch.triggered.connect(self.show_search_box)

        self.search_box.pub_search.clicked.connect(self.search)
        self.search_box.pub_replace.clicked.connect(self.replace)
        self.search_box.pub_replace_all.clicked.connect(self.replace_all)
        self.search_box.lineEdit_sec.textChanged.connect(
            lambda: self.mdiArea.activeSubWindow().widget().moveCursor(QTextCursor.Start))

    # 新建文件
    def new_fun(self):
        try:
            newDoc = MdiTextEdit()
            newDoc.setWindowTitle('Untitled-' + str(MdiTextEdit.newDocIndex))
            MdiTextEdit.newDocIndex += 1
            self.mdiArea.addSubWindow(newDoc)
            newDoc.show()
        except Exception as e:
            print(e)

    # 打开文件
    def open_fun(self):
        path, filetype = QFileDialog.getOpenFileName(self, "打开文件", "./",
                                                     "纯文本 (*.txt);;网页 (*.htm; *.html)")
        if path:
            filename = os.path.basename(path)
            try:
                def get_encoding(file):  # 获取文本编码方式
                    with open(file, 'rb') as f:
                        tmp = chardet.detect(f.read())
                        return tmp['encoding']

                with open(path, 'r', encoding=get_encoding(path)) as f:
                    content = f.read()
            except Exception as e:
                print(e)
            else:
                openDoc = MdiTextEdit()
                openDoc.path = path
                openDoc.setWindowTitle(filename)
                if "(*.txt)" in filetype:
                    openDoc.textedit.setPlainText(content)
                elif "(*.htm; *.html)" in filetype:
                    openDoc.textedit.setHtml(content)
                openDoc.textedit.document().setModified(False)
                self.mdiArea.addSubWindow(openDoc)
                openDoc.show()

    # 保存文件
    def save_fun(self):
        if self.mdiArea.subWindowList():
            activeWindow = self.mdiArea.activeSubWindow()
            if not activeWindow.path:
                return self.saveas_fun()
            else:
                with open(activeWindow.path, 'w', encoding='utf-8') as f:
                    if activeWindow.path.endswith(".txt"):
                        f.write(activeWindow.widget().toPlainText())
                    elif activeWindow.path.endswith(".htm") or activeWindow.path.endswith(".html"):
                        f.write(activeWindow.widget().toHtml())
                activeWindow.textedit.document().setModified(False)
                return True
        return False

    # 另存为文件
    def saveas_fun(self):
        if self.mdiArea.subWindowList():
            activeWindow = self.mdiArea.activeSubWindow()
            filename = activeWindow.windowTitle()
            path, filetype = QFileDialog.getSaveFileName(self, "保存文件", "./" + filename,
                                                         "纯文本 (*.txt);;网页 (*.html; *.htm)")
            if path:
                with open(path, 'w', encoding='utf-8') as f:
                    if "(*.txt)" in filetype:
                        f.write(activeWindow.widget().toPlainText())
                    elif "(*.html; *.htm)" in filetype:
                        f.write(activeWindow.widget().toHtml())
                activeWindow.path = path
                activeWindow.textedit.document().setModified(False)
                return True
        return False

    # 设置字体
    def set_font(self):
        if self.mdiArea.subWindowList():
            font, ok = QFontDialog.getFont()
            if ok:
                self.mdiArea.activeSubWindow().widget().setCurrentFont(font)

    # 设置颜色
    def set_color(self):
        if self.mdiArea.subWindowList():
            color = QColorDialog.getColor()
            if color.isValid():
                self.mdiArea.activeSubWindow().widget().setTextColor(color)

    # 关于
    def about(self):
        self.setWindowIcon(QIcon("images/about.png"))
        QMessageBox.about(self, "关于", "It is a simple Multi-Editor designed by YokDen")

    def show_search_box(self):
        if self.mdiArea.subWindowList():
            self.search_box.show()
            self.mdiArea.activeSubWindow().widget().moveCursor(QTextCursor.Start)

    def search(self):
        textedit = self.mdiArea.activeSubWindow().widget()
        search_text = self.search_box.lineEdit_sec.text()
        if search_text:
            if textedit.find(search_text):
                pass
            else:
                self.setWindowIcon(QIcon("images/search.png"))
                dlg = QMessageBox.question(self, "查找", "已经查找到最后，是否重头开始？",
                                           QMessageBox.Ok | QMessageBox.No)
                if dlg == QMessageBox.Ok:
                    textedit.moveCursor(QTextCursor.Start)

    def replace(self):
        textedit = self.mdiArea.activeSubWindow().widget()
        replace_text = self.search_box.lineEdit_rep.text()
        search_text = self.search_box.lineEdit_sec.text()
        if textedit.textCursor().selectedText() or textedit.find(search_text):
            textedit.textCursor().insertText(replace_text)
        else:
            self.setWindowIcon(QIcon("images/search.png"))
            dlg = QMessageBox.question(self, "替换", "已经替换到最后，是否重头开始？",
                                       QMessageBox.Ok | QMessageBox.No)
            if dlg == QMessageBox.Ok:
                textedit.moveCursor(QTextCursor.Start)

    def replace_all(self):
        textedit = self.mdiArea.activeSubWindow().widget()
        replace_text = self.search_box.lineEdit_rep.text()
        search_text = self.search_box.lineEdit_sec.text()
        if search_text:
            textedit.moveCursor(QTextCursor.Start)
            cnt = 0
            while textedit.find(search_text):
                textedit.textCursor().insertText(replace_text)
                cnt += 1
            self.setWindowIcon(QIcon("images/search.png"))
            if cnt == 0:
                QMessageBox.information(self, "替换", "未找到相关内容")
            else:
                QMessageBox.information(self, "替换", f"替换成功，共替换了{cnt}处内容")


# 子窗体
class MdiTextEdit(QMdiSubWindow):
    newDocIndex = 1  # 新建文件产生的编号

    def __init__(self):
        super(MdiTextEdit, self).__init__()
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.setWindowIcon(QIcon("images/note.png"))
        self.resize(782, 720)
        self.path = ''
        self.textedit = QTextEdit(self)
        self.textedit.document().setModified(False)  # 文档是否被编辑
        self.setWidget(self.textedit)
        palette = self.textedit.palette()
        palette.setColor(QPalette.Highlight, palette.color(QPalette.Active, QPalette.Highlight))
        self.textedit.setPalette(palette)

    def closeEvent(self, closeEvent: QtGui.QCloseEvent) -> None:  # 对子窗体closeEvent方法进行重写
        if self.textedit.document().isModified():
            dlg = QMessageBox.question(self, "TextEdit", f"是否保存对“{self.windowTitle()}”的修改?",
                                       QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
            if dlg == QMessageBox.Yes:
                if not ui.save_fun():
                    closeEvent.ignore()
            elif dlg == QMessageBox.Cancel:
                closeEvent.ignore()


class Editor(QMainWindow, QWidget):  # 对主窗体closeEvent方法进行重写
    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        unsaved_file = 0
        for window in ui.mdiArea.subWindowList():
            if window.textedit.document().isModified():
                unsaved_file += 1
        if unsaved_file:
            ui.setWindowIcon(QIcon("images/note.png"))
            dlg = QMessageBox.warning(ui, "TextEdit", f"还有{unsaved_file}个文件未保存,是否关闭?",
                                      QMessageBox.Yes | QMessageBox.No)
            if dlg == QMessageBox.No:
                a0.ignore()


class Ui_SearchBox(QMainWindow):
    def setupUi(self, SearchBox):
        SearchBox.setObjectName("SearchBox")
        SearchBox.resize(367, 142)
        SearchBox.setWindowIcon(QIcon("images/search.png"))
        self.centralwidget = QtWidgets.QWidget(SearchBox)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.lbl_search = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_search.sizePolicy().hasHeightForWidth())
        self.lbl_search.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lbl_search.setFont(font)
        self.lbl_search.setObjectName("lbl_search")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_search)
        self.lbl_replace = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_replace.sizePolicy().hasHeightForWidth())
        self.lbl_replace.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lbl_replace.setFont(font)
        self.lbl_replace.setObjectName("lbl_replace")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_replace)
        self.lineEdit_sec = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_sec.setFont(font)
        self.lineEdit_sec.setObjectName("lineEdit_sec")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_sec)
        self.lineEdit_rep = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lineEdit_rep.setFont(font)
        self.lineEdit_rep.setObjectName("lineEdit_rep")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_rep)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 11, -1, -1)
        self.horizontalLayout.setSpacing(38)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pub_search = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pub_search.setFont(font)
        self.pub_search.setObjectName("pub_search")
        self.horizontalLayout.addWidget(self.pub_search)
        self.pub_replace = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pub_replace.setFont(font)
        self.pub_replace.setObjectName("pub_replace")
        self.horizontalLayout.addWidget(self.pub_replace)
        self.pub_replace_all = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pub_replace_all.setFont(font)
        self.pub_replace_all.setObjectName("pub_replace_all")
        self.horizontalLayout.addWidget(self.pub_replace_all)
        self.verticalLayout.addLayout(self.horizontalLayout)
        SearchBox.setCentralWidget(self.centralwidget)

        self.retranslateUi(SearchBox)
        QtCore.QMetaObject.connectSlotsByName(SearchBox)

    def retranslateUi(self, SearchBox):
        _translate = QtCore.QCoreApplication.translate
        SearchBox.setWindowTitle(_translate("SearchBox", "查找替换"))
        self.lbl_search.setText(_translate("SearchBox", "查找内容："))
        self.lbl_replace.setText(_translate("SearchBox", "替换为："))
        self.pub_search.setText(_translate("SearchBox", "查找"))
        self.pub_replace.setText(_translate("SearchBox", "替换"))
        self.pub_replace_all.setText(_translate("SearchBox", "替换全部"))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    sub = Editor()
    ui = Ui_Editor()
    ui.setupUi(sub)
    sub.show()
    sys.exit(app.exec_())
