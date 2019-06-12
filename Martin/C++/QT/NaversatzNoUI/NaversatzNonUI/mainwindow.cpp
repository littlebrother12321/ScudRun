#include "mainwindow.h"

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

    // File
    QMenu *menu = menuBar->addMenu("&File");

    // New
    QAction *action = new QAction("&New", this);
    connect(action, &QAction::triggered, this, &MainWindow::OnFileNew);
    menu->addAction(action);
    // Open
    action = new QAction("&Open", this);
    connect(action, &QAction::triggered, this, &MainWindow::OnFileOpen);
    menu->addAction(action);
    // Save
    action = new QAction("&Save", this);
    connect(action, &QAction::triggered, this, &MainWindow::OnFileSave);
    menu->addAction(action);
    // Exit
    action = new QAction("&Exit", this);
    connect(action, &QAction::triggered, this, &MainWindow::close);
    menu->addAction(action);

    // Set
    menu = menuBar->addMenu("&Set");

    // UDP
    action = new QAction("&UDP target", this);
    connect(action, &QAction::triggered, this, &MainWindow::OnSetUDP);
    menu->addAction(action);

//-------------------------------------------------------------------------------------

    // Status Bar
    QStatusBar *statusBar = new QStatusBar(this);
    setStatusBar(statusBar);
}

MainWindow::~MainWindow()
{

}

void MainWindow::OnFileNew()
{
    statusBar()->showMessage("File -> New");
}

void MainWindow::OnFileOpen()
{
    statusBar()->showMessage("File -> Open");
}

void MainWindow::OnFileSave()
{
    statusBar()->showMessage("File -> Save");
}

void MainWindow::OnSetUDP()
{
    statusBar()->showMessage("Set -> UDP");

    /*
    QMessageBox *msg = new QMessageBox(this);

    msg->setIcon(QMessageBox::Question);
    msg->setWindowTitle("Set UDP Port?");
    msg->setText("Do you want to set the UDP Port for Naversatz?");
    msg->setStandardButtons(QMessageBox::Yes | QMessageBox::No);
    msg->setDefaultButton(QMessageBox::Yes);

    msg->exec();
    */

    int ret = QMessageBox::question(this, tr("Set UDP Port"), tr("Do you want to set the UDP Port?")
                                    , QMessageBox::Yes | QMessageBox::No, QMessageBox::Yes)
}
