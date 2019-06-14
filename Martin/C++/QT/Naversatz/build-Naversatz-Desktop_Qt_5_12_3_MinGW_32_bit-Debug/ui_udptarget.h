/********************************************************************************
** Form generated from reading UI file 'udptarget.ui'
**
** Created by: Qt User Interface Compiler version 5.12.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_UDPTARGET_H
#define UI_UDPTARGET_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDialogButtonBox>
#include <QtWidgets/QPlainTextEdit>

QT_BEGIN_NAMESPACE

class Ui_Dialog
{
public:
    QDialogButtonBox *buttonBox;
    QPlainTextEdit *plainTextEdit;

    void setupUi(QDialog *Dialog)
    {
        if (Dialog->objectName().isEmpty())
            Dialog->setObjectName(QString::fromUtf8("Dialog"));
        Dialog->resize(199, 60);
        buttonBox = new QDialogButtonBox(Dialog);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setGeometry(QRect(-160, 30, 341, 32));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);
        plainTextEdit = new QPlainTextEdit(Dialog);
        plainTextEdit->setObjectName(QString::fromUtf8("plainTextEdit"));
        plainTextEdit->setGeometry(QRect(10, 10, 181, 21));

        retranslateUi(Dialog);
        QObject::connect(buttonBox, SIGNAL(accepted()), Dialog, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), Dialog, SLOT(reject()));

        QMetaObject::connectSlotsByName(Dialog);
    } // setupUi

    void retranslateUi(QDialog *Dialog)
    {
        Dialog->setWindowTitle(QApplication::translate("Dialog", "Dialog", nullptr));
    } // retranslateUi

};

namespace Ui {
    class Dialog: public Ui_Dialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_UDPTARGET_H
