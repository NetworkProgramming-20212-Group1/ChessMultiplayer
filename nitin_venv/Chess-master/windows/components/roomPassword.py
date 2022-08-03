from PyQt5.QtWidgets import QDialog, QLineEdit, QDialogButtonBox, QFormLayout

class RoomPassword(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.password = QLineEdit(self)
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self);

        layout = QFormLayout(self)
        layout.addRow("Enter room password: ", self.password)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self):
        if not self.password.text():
            return None
        else:
            return self.password.text()