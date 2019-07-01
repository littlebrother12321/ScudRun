#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "udpdialog.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    QSettings settings(QString("config.ini"), QSettings::IniFormat);
    QString someValue = settings.value("some/config/key", "default value if unset").toString();
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_actionUDP_Target_triggered()
{
    UDPDialog *setUDP = new UDPDialog(this);
    setUDP->show();
}
