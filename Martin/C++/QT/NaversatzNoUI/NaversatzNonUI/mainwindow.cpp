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

    QPushButton *yes = new QPushButton;
    QPushButton *no = new QPushButton;

    yes->setText(tr("Confirm"));
    yes->setDefault(true);
    no->setText(tr("Cancel"));    

    QWidget *setUDP = new QWidget;
    QLabel *label = new QLabel(tr("UDP Target: "));
    QLineEdit *ipField = new QLineEdit();
    QHBoxLayout *layout = new QHBoxLayout();

    QMainWindow *window = new QMainWindow();
    window->setCentralWidget(setUDP);
    window->setWindowTitle(tr("Set UDP Target"));
    QObject::connect(yes, SIGNAL(yes->clicked()), this, SLOT(MainWindow::OnSetUDP()));
    QObject::connect(no, SIGNAL(yes->clicked()), this, SLOT(MainWindow::~MainWindow()));

    label->setBaseSize(300, 25);

    ipField->setInputMask(tr("000.000.000.000:0000;*"));

    layout->addWidget(label);
    layout->addWidget(ipField);
    layout->addWidget(yes);
    layout->addWidget(no);

    setUDP->setLayout(layout);
    setUDP->show();

    window->show();

    //connect(yes, yes->released(), this, )
}
