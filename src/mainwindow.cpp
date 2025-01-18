#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QtWidgets>
using namespace std;

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent)
    , ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    // Initializing the qtable header and size
    ui->phoneBookTable->setColumnCount(4);
    QStringList list = {"id", "Name", "PhoneNo", "Email"};
    ui->phoneBookTable->setHorizontalHeaderLabels(list);

    ui->phoneBookTable->horizontalHeader()->setStretchLastSection(true);
}

MainWindow::~MainWindow()
{
    delete ui;
}

QString verifyName(QString& name){
    // if(name.isEmpty()){
    //     return "Name cannot be empty.";
    // }
    if(name.length()>=30){
        return "Name field exceeds limit of 30 characters.";
    }

    return QString();
}

QString verifyPhoneNo(QString& phone){
    if(phone.isEmpty()){
        return "Phone number cannot be empty.";
    }

    if(phone.toInt() == 0){
        return "Incorrect phone number";
    }
    // Phone number contains exactly 11 numbers assuming Egyptian numbers only are allowed
    QRegularExpression phoneReg ("^(010|011|012)\\d{8}$");
    QRegularExpressionMatch match = phoneReg.match(phone);
    if(!match.hasMatch()){
        return "Incorrect phone number";
    }

    return QString();
}

QString verifyEmail(QString& email){
    // Email make sure email structure is followed and it doesn't exceed limit
    // Email is optional so check first that it exists
    QRegularExpression emailRegex("^[a-zA-Z]{1,}[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$");
    QRegularExpressionMatch match = emailRegex.match(email);
    if(!email.isEmpty()){
        if(!match.hasMatch()){
            return "Incorrect email address";
        }
        if(email.length() > 50){
            return "Email exceeds 50 characters limit";
        }
    }

    return QString();
}

QString checkIfExists(QString& name,QString& phone,QString& email, QTableWidget* phoneTable){
    for (int row = 0; row < phoneTable->rowCount(); ++row) {
        QString existingName = phoneTable->item(row, 1)->text();
        QString existingPhone = phoneTable->item(row, 2)->text();
        QString existingEmail = phoneTable->item(row, 3)->text();

        if (existingName == name) {
            return "Name already exists.";
        }
        if (existingPhone == phone) {
            return "Phone number already exists.";
        }
        // if (existingEmail == email && !email.isEmpty()) {
        //     return "Email address already exists.";
        // }
    }

    return "";
}


void MainWindow::on_addBtn_clicked()
{
    // Reading input from form
    QString name = ui->nameTxt->toPlainText();
    QString phone = ui->phoneTxt->toPlainText();
    QString email = ui->emailTxt->toPlainText();

    //Verifying input forms
    QString nameError = verifyName(name);
    if(!nameError.isEmpty()){
        QMessageBox::warning(this, "Error", nameError);
        return;
    }

    QString phoneError = verifyPhoneNo(phone);
    if(!phoneError.isEmpty()){
        QMessageBox::warning(this, "Error", phoneError);
        return;
    }

    QString emailError = verifyEmail(email);
    if(!emailError.isEmpty()){
        QMessageBox::warning(this, "Error", emailError);
        return;
    }

    //Check if the info added already exists
    QString existError = checkIfExists(name, phone, email, ui->phoneBookTable);
    if(!existError.isEmpty()){
        QMessageBox::warning(this, "Error", existError);
        return;
    }

    //Inserting a new row
    int row = ui->phoneBookTable->rowCount();
    ui->phoneBookTable->insertRow(row);


    //Adding data to row
    //Get last row Id if exists
    int lastRow = 0;
    if(row>0){
        QTableWidgetItem* lastItem = ui->phoneBookTable->item(row-1,0);
        lastRow = lastItem->text().toInt();
    }

    ui->phoneBookTable->setItem(row, 0, new QTableWidgetItem(QString::number(lastRow + 1)));
    ui->phoneBookTable->setItem(row, 1, new QTableWidgetItem(name));
    ui->phoneBookTable->setItem(row, 2, new QTableWidgetItem(phone));
    ui->phoneBookTable->setItem(row, 3, new QTableWidgetItem(email));

    //Disable the edit mode per row
    for (int col = 0; col < ui->phoneBookTable->columnCount(); ++col) {
        QTableWidgetItem* item = ui->phoneBookTable->item(row, col);
        if (item) {
            item->setFlags(item->flags() & ~Qt::ItemIsEditable | Qt::ItemIsEnabled | Qt::ItemIsSelectable);
        }
    }

    //Clear form
    ui->nameTxt->clear();
    ui->phoneTxt->clear();
    ui->emailTxt->clear();
}


void MainWindow::on_removeBtn_clicked()
{
    //If table is empty return
    if(ui->phoneBookTable->rowCount()==0){
        QMessageBox::information(this, "Info", "Table is empty!");
        return;
    }

    //Remove all selected rows
    QList<QTableWidgetItem *> itemsList = ui->phoneBookTable->selectedItems();

    //Show any response if remove button is clicked while nothing is selected
    if(itemsList.empty()){
        QMessageBox::information(this, "Info", "Please select a row to be removed!");
        return;
    }
    for(int i=0; i<itemsList.length(); i++){
        int row = itemsList[i]->row();
        ui->phoneBookTable->removeRow(row);
    }
}

void MainWindow::on_removeAllBtn_clicked()
{
    //If table is empty return
    if(ui->phoneBookTable->rowCount()==0){
        QMessageBox::information(this, "Info", "Table is empty!");
        return;
    }

    // Ask for confirmation
    int reply = QMessageBox::question(this, "Confirm Remove All",
                                      "Are you sure you want to remove all contacts?",
                                      QMessageBox::Yes | QMessageBox::No);

    if (reply == QMessageBox::Yes) {
        for(int i = ui->phoneBookTable->rowCount() - 1; i >= 0; --i){
            ui->phoneBookTable->removeRow(i);
        }
    }
}

