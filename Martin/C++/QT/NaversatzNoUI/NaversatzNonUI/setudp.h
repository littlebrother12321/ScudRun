#ifndef SETUDP_H
#define SETUDP_H
#include "mainwindow.h"
#include <QObject>
#include <iostream>

class udpWindow : QObject
{
public:
    udpWindow();
    ~udpWindow();

    QPushButton *yes = new QPushButton;
    QPushButton *no = new QPushButton;

private slots:
    void OnConfirm();
    void OnDeny();

private:
    bool affirm;
    bool deny;
};

udpWindow::udpWindow()
{
    yes->setText("Confirm");
    yes->setDefault(true);
    no->setText("Cancel");

    QWidget *setUDP = new QWidget;
    QLabel *label = new QLabel("UDP Target: ");
    QLineEdit *ipField = new QLineEdit();
    QHBoxLayout *layout = new QHBoxLayout();

    QMainWindow *window = new QMainWindow();
    window->setCentralWidget(setUDP);
    window->setWindowTitle("Set UDP Target");
    connect(yes, SIGNAL(yes->clicked()), this, SLOT(udpTarget::OnConfirm()));
    connect(no, SIGNAL(yes->clicked()), this, SLOT(close()));

    label->setBaseSize(300, 25);

    ipField->setInputMask("000.000.000.000:0000;#");

    layout->addWidget(label);
    layout->addWidget(ipField);
    layout->addWidget(yes);
    layout->addWidget(no);

    setUDP->setLayout(layout);
    setUDP->show();

    window->show();
}

udpWindow::~udpWindow()
{}

void udpWindow::OnConfirm()
{
    affirm = true;

    std::cout << affirm << std::endl;
}

void udpWindow::OnDeny()
{
    deny = true;
}
#endif // SETUDP_H
