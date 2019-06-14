#include "mainwindow.h"
#include "ui_mainwindow.h"

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
    QWindow *udpSet = new QWindow();
    udpSet->setWidth(640);
    udpSet->setHeight(480);
    udpSet->setMinimumHeight(480);
    udpSet->setMinimumWidth(640);
    udpSet->setTitle("Set UDP Address");

    //QLineEdit *ipEdit = new QLineEdit(this);
    //ipEdit->setInputMask("000.000.000.000;_");
    //ipEdit->show();

    udpSet->show();
}
