/********************************************************************************
** Form generated from reading UI file 'udpdialog.ui'
**
** Created by: Qt User Interface Compiler version 5.12.3
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_UDPDIALOG_H
#define UI_UDPDIALOG_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QDialog>
#include <QtWidgets/QDialogButtonBox>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QVBoxLayout>

QT_BEGIN_NAMESPACE

class Ui_UDPDialog
{
public:
    QVBoxLayout *verticalLayout;
    QLabel *label;
    QLineEdit *lineEdit;
    QDialogButtonBox *buttonBox;

    void setupUi(QDialog *UDPDialog)
    {
        if (UDPDialog->objectName().isEmpty())
            UDPDialog->setObjectName(QString::fromUtf8("UDPDialog"));
        UDPDialog->resize(400, 100);
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(UDPDialog->sizePolicy().hasHeightForWidth());
        UDPDialog->setSizePolicy(sizePolicy);
        verticalLayout = new QVBoxLayout(UDPDialog);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        label = new QLabel(UDPDialog);
        label->setObjectName(QString::fromUtf8("label"));

        verticalLayout->addWidget(label);

        lineEdit = new QLineEdit(UDPDialog);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));

        verticalLayout->addWidget(lineEdit);

        buttonBox = new QDialogButtonBox(UDPDialog);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);

        verticalLayout->addWidget(buttonBox);


        retranslateUi(UDPDialog);
        QObject::connect(buttonBox, SIGNAL(accepted()), UDPDialog, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), UDPDialog, SLOT(reject()));

        QMetaObject::connectSlotsByName(UDPDialog);
    } // setupUi

    void retranslateUi(QDialog *UDPDialog)
    {
        UDPDialog->setWindowTitle(QApplication::translate("UDPDialog", "Dialog", nullptr));
        label->setText(QApplication::translate("UDPDialog", "Enter UDP Target here:", nullptr));
    } // retranslateUi

};

namespace Ui {
    class UDPDialog: public Ui_UDPDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_UDPDIALOG_H
