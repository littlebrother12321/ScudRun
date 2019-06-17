#include "mainwindow.h"
#include "setudp.h"
MainWindow::MainWindow(QWidget *parent) : QMainWindow(parent)
{
    // Window
    setWindowTitle("Naversatz UDP");

    setMinimumSize(800, 450);

//-------------------------------------------------------------------------------------

    // Menu Bar
    QMenuBar *menuBar = new QMenuBar(this);
    setMenuBar(menuBar);

    // Menu Items

    // Set
    QMenu *menu = menuBar->addMenu("&Set");

    // UDP
    QAction *action = new QAction("&UDP target", this);
    connect(action, &QAction::triggered, this, &MainWindow::OnSetUDP);
    menu->addAction(action);

//-------------------------------------------------------------------------------------

    // Status Bar
    QStatusBar *statusBar = new QStatusBar(this);
    setStatusBar(statusBar);
}

MainWindow::~MainWindow()
{}

void MainWindow::OnSetUDP()
{
    statusBar()->showMessage("Set -> UDP");

    udpWindow *window = new udpWindow();
    //QObject::connect(window, SIGNAL(udpWindow->yes->released()),
    //                 window,  SLOT(window.OnConfirm()));

    //connect(yes, yes->released(), this, )
}
