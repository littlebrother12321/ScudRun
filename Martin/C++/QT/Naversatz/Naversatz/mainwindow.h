#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QtGui>

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void OnFileNew();
    void OnFileOpen();
    void OnFileSave();

private:
    Ui::MainWindow *ui;
};

#endif // MAINWINDOW_H