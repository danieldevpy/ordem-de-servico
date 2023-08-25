from PySide6.QtWidgets import QMessageBox, QInputDialog

def show_message(tipo, titulo, mensagem):
    msg_box = QMessageBox()

    if tipo == 'error':
        msg_box.setIcon(QMessageBox.Critical)
    elif tipo == 'sucess':
        msg_box.setIcon(QMessageBox.Information)
    elif tipo == 'information':
        msg_box.setIcon(QMessageBox.Information)
    else:
        raise ValueError("Tipo de mensagem inválido.")

    msg_box.setWindowTitle(titulo)
    msg_box.setText(mensagem)
    msg_box.exec()


def show_message_with_confirmation(tipo, titulo, mensagem):
    msg_box = QMessageBox()

    if tipo == 'error':
        msg_box.setIcon(QMessageBox.Critical)
    elif tipo == 'success':
        msg_box.setIcon(QMessageBox.Information)
    elif tipo == 'information':
        msg_box.setIcon(QMessageBox.Information)
    else:
        raise ValueError("Tipo de mensagem inválido.")

    msg_box.setWindowTitle(titulo)
    msg_box.setText(mensagem)

    # Adicionando os botões "OK" e "Cancelar" à caixa de diálogo
    msg_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    # Exibe a caixa de diálogo e aguarda a resposta do usuário
    button_clicked = msg_box.exec()

    # Verifica a resposta do usuário
    if button_clicked == QMessageBox.Ok:
        return True
    else:
        return False


def get_text(title: str, field: str):
    name, ok = QInputDialog.getText(None, title, field)
    if ok:
        return name, True
    else:
        return name, False