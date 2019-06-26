#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "udpdialog.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
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
