from PyQt5.QtWidgets import QDialog, QLineEdit, QDialogButtonBox, QFormLayout

class RoomConfiguration(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.roomID = QLineEdit(self)
        self.password = QLineEdit(self)
        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, self);

        layout = QFormLayout(self)
        layout.addRow("Enter room id: ", self.roomID)
        layout.addRow("Enter room password: ", self.password)
        layout.addWidget(buttonBox)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

    def getInputs(self):
        if not self.roomID.text() or not self.password.text():
            return None
        else:
            return (self.roomID.text(), self.password.text())