#ifndef UDPTARGET_H
#define UDPTARGET_H

#include <QMainWindow>
#include <QtGui>
#include <QLineEdit>

class UDPTarget : public QMainWindow
{
    Q_OBJECT

public:
    UDPTarget(QWidget *parent = nullptr);
    ~UDPTarget();
};

#endif // UDPTARGET_H
