#include "udpdialog.h"
#include "ui_udpdialog.h"
#include <QtDebug>
#include <QSettings>

UDPDialog::UDPDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::UDPDialog)
{
    ui->setupUi(this);
    ui->lineEdit->setInputMask("000.000.000.000:0000");
}

UDPDialog::~UDPDialog()
{
    delete ui;
}

void UDPDialog::on_buttonBox_accepted()
{
    //TODO save dialog entry
    QString stuff = this->ui->lineEdit->text();
    qInfo() << "UDP Target Returned Value: " << stuff << "\n";
}
