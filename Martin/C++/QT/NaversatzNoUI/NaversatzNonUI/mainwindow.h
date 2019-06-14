#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QMenuBar>
#include <QStatusBar>
#include <QMessageBox>
#include <QPushButton>
#include <QAbstractButton>
#include <QtGlobal>
#include <QtWidgets>
#include <QLineEdit>
#include <QWindow>

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    // Construct and Destruct
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    // Actions

    //void OnFileNew();
    //void OnFileOpen();
    //void OnFileSave();

    void OnSetUDP();
};
#endif // MAINWINDOW_H
