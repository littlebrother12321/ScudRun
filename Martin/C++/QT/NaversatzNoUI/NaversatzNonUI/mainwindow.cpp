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
    menuBar->addMenu("&Set");

    // UDP
    action = new QAction("&UDP", this);
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
}
