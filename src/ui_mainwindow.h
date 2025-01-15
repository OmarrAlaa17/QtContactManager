/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 6.8.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPlainTextEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QVBoxLayout *verticalLayout_4;
    QVBoxLayout *verticalLayout_3;
    QHBoxLayout *horizontalLayout;
    QVBoxLayout *verticalLayout;
    QLabel *nameLabel;
    QLabel *phoneLabel;
    QLabel *emailLabel;
    QVBoxLayout *verticalLayout_2;
    QPlainTextEdit *nameTxt;
    QPlainTextEdit *phoneTxt;
    QPlainTextEdit *emailTxt;
    QPushButton *addBtn;
    QSpacerItem *verticalSpacer;
    QTableWidget *phoneBookTable;
    QHBoxLayout *horizontalLayout_2;
    QPushButton *removeBtn;
    QPushButton *removeAllBtn;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName("MainWindow");
        MainWindow->resize(424, 583);
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName("centralwidget");
        verticalLayout_4 = new QVBoxLayout(centralwidget);
        verticalLayout_4->setObjectName("verticalLayout_4");
        verticalLayout_3 = new QVBoxLayout();
        verticalLayout_3->setObjectName("verticalLayout_3");
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName("horizontalLayout");
        verticalLayout = new QVBoxLayout();
        verticalLayout->setObjectName("verticalLayout");
        nameLabel = new QLabel(centralwidget);
        nameLabel->setObjectName("nameLabel");

        verticalLayout->addWidget(nameLabel);

        phoneLabel = new QLabel(centralwidget);
        phoneLabel->setObjectName("phoneLabel");

        verticalLayout->addWidget(phoneLabel);

        emailLabel = new QLabel(centralwidget);
        emailLabel->setObjectName("emailLabel");

        verticalLayout->addWidget(emailLabel);


        horizontalLayout->addLayout(verticalLayout);

        verticalLayout_2 = new QVBoxLayout();
        verticalLayout_2->setObjectName("verticalLayout_2");
        nameTxt = new QPlainTextEdit(centralwidget);
        nameTxt->setObjectName("nameTxt");
        QSizePolicy sizePolicy(QSizePolicy::Policy::Preferred, QSizePolicy::Policy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(nameTxt->sizePolicy().hasHeightForWidth());
        nameTxt->setSizePolicy(sizePolicy);
        nameTxt->setMaximumSize(QSize(16777215, 35));
        nameTxt->setFrameShadow(QFrame::Shadow::Sunken);
        nameTxt->setMidLineWidth(0);
        nameTxt->setVerticalScrollBarPolicy(Qt::ScrollBarPolicy::ScrollBarAlwaysOff);
        nameTxt->setHorizontalScrollBarPolicy(Qt::ScrollBarPolicy::ScrollBarAlwaysOff);
        nameTxt->setSizeAdjustPolicy(QAbstractScrollArea::SizeAdjustPolicy::AdjustToContents);
        nameTxt->setTabChangesFocus(true);
        nameTxt->setLineWrapMode(QPlainTextEdit::LineWrapMode::WidgetWidth);
        nameTxt->setOverwriteMode(false);
        nameTxt->setMaximumBlockCount(10);

        verticalLayout_2->addWidget(nameTxt);

        phoneTxt = new QPlainTextEdit(centralwidget);
        phoneTxt->setObjectName("phoneTxt");
        phoneTxt->setMaximumSize(QSize(16777215, 35));
        phoneTxt->setVerticalScrollBarPolicy(Qt::ScrollBarPolicy::ScrollBarAlwaysOff);
        phoneTxt->setHorizontalScrollBarPolicy(Qt::ScrollBarPolicy::ScrollBarAlwaysOff);
        phoneTxt->setSizeAdjustPolicy(QAbstractScrollArea::SizeAdjustPolicy::AdjustToContents);
        phoneTxt->setTabChangesFocus(true);
        phoneTxt->setMaximumBlockCount(10);

        verticalLayout_2->addWidget(phoneTxt);

        emailTxt = new QPlainTextEdit(centralwidget);
        emailTxt->setObjectName("emailTxt");
        emailTxt->setMaximumSize(QSize(16777215, 35));
        emailTxt->setVerticalScrollBarPolicy(Qt::ScrollBarPolicy::ScrollBarAlwaysOff);
        emailTxt->setHorizontalScrollBarPolicy(Qt::ScrollBarPolicy::ScrollBarAlwaysOff);
        emailTxt->setSizeAdjustPolicy(QAbstractScrollArea::SizeAdjustPolicy::AdjustToContents);
        emailTxt->setTabChangesFocus(true);
        emailTxt->setMaximumBlockCount(10);

        verticalLayout_2->addWidget(emailTxt);


        horizontalLayout->addLayout(verticalLayout_2);


        verticalLayout_3->addLayout(horizontalLayout);

        addBtn = new QPushButton(centralwidget);
        addBtn->setObjectName("addBtn");

        verticalLayout_3->addWidget(addBtn);

        verticalSpacer = new QSpacerItem(20, 40, QSizePolicy::Policy::Minimum, QSizePolicy::Policy::Minimum);

        verticalLayout_3->addItem(verticalSpacer);


        verticalLayout_4->addLayout(verticalLayout_3);

        phoneBookTable = new QTableWidget(centralwidget);
        phoneBookTable->setObjectName("phoneBookTable");
        sizePolicy.setHeightForWidth(phoneBookTable->sizePolicy().hasHeightForWidth());
        phoneBookTable->setSizePolicy(sizePolicy);
        phoneBookTable->setMinimumSize(QSize(300, 320));
        phoneBookTable->setVerticalScrollBarPolicy(Qt::ScrollBarPolicy::ScrollBarAlwaysOff);
        phoneBookTable->setSizeAdjustPolicy(QAbstractScrollArea::SizeAdjustPolicy::AdjustToContents);
        phoneBookTable->setAutoScroll(false);
        phoneBookTable->setDragEnabled(true);
        phoneBookTable->setDragDropMode(QAbstractItemView::DragDropMode::DragDrop);
        phoneBookTable->setSelectionMode(QAbstractItemView::SelectionMode::ContiguousSelection);
        phoneBookTable->setVerticalScrollMode(QAbstractItemView::ScrollMode::ScrollPerItem);

        verticalLayout_4->addWidget(phoneBookTable);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName("horizontalLayout_2");
        removeBtn = new QPushButton(centralwidget);
        removeBtn->setObjectName("removeBtn");

        horizontalLayout_2->addWidget(removeBtn);

        removeAllBtn = new QPushButton(centralwidget);
        removeAllBtn->setObjectName("removeAllBtn");
        QFont font;
        font.setBold(true);
        removeAllBtn->setFont(font);
        removeAllBtn->setCursor(QCursor(Qt::CursorShape::ArrowCursor));
        removeAllBtn->setMouseTracking(false);
        removeAllBtn->setFocusPolicy(Qt::FocusPolicy::WheelFocus);
        removeAllBtn->setCheckable(false);

        horizontalLayout_2->addWidget(removeAllBtn);


        verticalLayout_4->addLayout(horizontalLayout_2);

        MainWindow->setCentralWidget(centralwidget);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QCoreApplication::translate("MainWindow", "MainWindow", nullptr));
        nameLabel->setText(QCoreApplication::translate("MainWindow", "Name", nullptr));
        phoneLabel->setText(QCoreApplication::translate("MainWindow", "Phone Number", nullptr));
        emailLabel->setText(QCoreApplication::translate("MainWindow", "Email (Optional)", nullptr));
        addBtn->setText(QCoreApplication::translate("MainWindow", "Add", nullptr));
        removeBtn->setText(QCoreApplication::translate("MainWindow", "Remove", nullptr));
        removeAllBtn->setText(QCoreApplication::translate("MainWindow", "Remove All", nullptr));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
