#include "udptarget.h"
#include "ui_udptarget.h"

UDPTarget::UDPTarget(QWidget *parent) :
    QMainWindow(parent),
    fill(new Fill::UDPTarget)
{
    fill->setupUi(this);
}

UDPTarget::~UDPTarget()
{
    delete fill;
}
