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
#include <QtWidgets/QComboBox>
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
    QComboBox *comboBox;
    QDialogButtonBox *buttonBox;
    QLineEdit *lineEdit;

    void setupUi(QDialog *UDPDialog)
    {
        if (UDPDialog->objectName().isEmpty())
            UDPDialog->setObjectName(QString::fromUtf8("UDPDialog"));
        UDPDialog->resize(179, 98);
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(UDPDialog->sizePolicy().hasHeightForWidth());
        UDPDialog->setSizePolicy(sizePolicy);
        UDPDialog->setMaximumSize(QSize(443, 218));
        verticalLayout = new QVBoxLayout(UDPDialog);
        verticalLayout->setObjectName(QString::fromUtf8("verticalLayout"));
        label = new QLabel(UDPDialog);
        label->setObjectName(QString::fromUtf8("label"));

        verticalLayout->addWidget(label);

        comboBox = new QComboBox(UDPDialog);
        comboBox->setObjectName(QString::fromUtf8("comboBox"));

        verticalLayout->addWidget(comboBox);

        buttonBox = new QDialogButtonBox(UDPDialog);
        buttonBox->setObjectName(QString::fromUtf8("buttonBox"));
        buttonBox->setOrientation(Qt::Horizontal);
        buttonBox->setStandardButtons(QDialogButtonBox::Cancel|QDialogButtonBox::Ok);
        buttonBox->setCenterButtons(true);

        verticalLayout->addWidget(buttonBox);

        lineEdit = new QLineEdit(UDPDialog);
        lineEdit->setObjectName(QString::fromUtf8("lineEdit"));

        verticalLayout->addWidget(lineEdit);


        retranslateUi(UDPDialog);
        QObject::connect(buttonBox, SIGNAL(accepted()), UDPDialog, SLOT(accept()));
        QObject::connect(buttonBox, SIGNAL(rejected()), UDPDialog, SLOT(reject()));

        QMetaObject::connectSlotsByName(UDPDialog);
    } // setupUi

    void retranslateUi(QDialog *UDPDialog)
    {
        UDPDialog->setWindowTitle(QApplication::translate("UDPDialog", "Set UDP Target", nullptr));
        label->setText(QApplication::translate("UDPDialog", "Enter UDP Target here:", nullptr));
    } // retranslateUi

};

namespace Ui {
    class UDPDialog: public Ui_UDPDialog {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_UDPDIALOG_H
