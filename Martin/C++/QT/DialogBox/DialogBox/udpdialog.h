#ifndef UDPDIALOG_H
#define UDPDIALOG_H

#include <QDialog>

namespace Ui {
class UDPDialog;
}

class UDPDialog : public QDialog
{
    Q_OBJECT

public:
    explicit UDPDialog(QWidget *parent = nullptr);
    ~UDPDialog();

private slots:
    void on_buttonBox_accepted();

private:
    Ui::UDPDialog *ui;
};

#endif // UDPDIALOG_H
