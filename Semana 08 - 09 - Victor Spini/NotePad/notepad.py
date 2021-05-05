# Victor Spini Paranaiba - 11611EMT005

# Bibliotecas
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import * 
from PyQt5.QtPrintSupport import * 
import os
import sys
  
# Criando janela principal do bloco de notas
class MainWindow(QMainWindow):
  
    # Construção
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
  
        # Tamanho da janela
        self.setGeometry(100, 100, 600, 400)
  
  
        self.editor = QPlainTextEdit()
  
        # Layout da janela
        layout = QVBoxLayout()
        layout.addWidget(self.editor)
    
        # Fonte para o editor
        fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixedfont.setPointSize(12)
        self.editor.setFont(fixedfont)
  
        self.path = None
  
        container = QWidget()
  
        # Layout container
        container.setLayout(layout) 
        # making container as central widget
        self.setCentralWidget(container) 
        # Objetos da barra de tarefa
        self.status = QStatusBar()
        # definindo a barra de estatísticas para a janela
        self.setStatusBar(self.status)
        # criando uma barra de ferramentas de arquivo
        file_toolbar = QToolBar("Arquivo")
        # adicionando a barra de ferramentas de arquivo à janela
        self.addToolBar(file_toolbar)
        
        # criando um menu
        file_menu = self.menuBar().addMenu("&Arquivo")
        # criando ações
        open_file_action = QAction("Abrir arquivo", self)
        open_file_action.setStatusTip("Abrir arquivo")
        open_file_action.triggered.connect(self.file_open)
        file_menu.addAction(open_file_action)
        file_toolbar.addAction(open_file_action)
  
        # Similarmente criando ação de salvar
        save_file_action = QAction("Salvar", self)
        save_file_action.setStatusTip("Salvar página atual")
        save_file_action.triggered.connect(self.file_save)
        file_menu.addAction(save_file_action)
        file_toolbar.addAction(save_file_action)

        saveas_file_action = QAction("Savlvar como", self)
        saveas_file_action.setStatusTip("Salvar a página atual no arquivo específico")
        saveas_file_action.triggered.connect(self.file_saveas)
        file_menu.addAction(saveas_file_action)
        file_toolbar.addAction(saveas_file_action)
  
        # Ação de imprimir
        print_action = QAction("Imprimir", self)
        print_action.setStatusTip("Imprimir página atual")
        print_action.triggered.connect(self.file_print)
        file_menu.addAction(print_action)
        file_toolbar.addAction(print_action)
  
        # Criando barra de editar
        edit_toolbar = QToolBar("Editar")
  
        # Adicionando à janela
        self.addToolBar(edit_toolbar)
        
        edit_menu = self.menuBar().addMenu("&Editar")
  
        # adding actions to the tool bar and menu bar
  
        # Ação desfazer
        undo_action = QAction("Desfazer", self)
        undo_action.setStatusTip("Desfazer última alteração")
        undo_action.triggered.connect(self.editor.undo)
  
        edit_toolbar.addAction(undo_action)
        edit_menu.addAction(undo_action)
  
        # Ação refazer
        redo_action = QAction("Refazer", self)
        redo_action.setStatusTip("Refazer última alteração")
        redo_action.triggered.connect(self.editor.redo)
  
        edit_toolbar.addAction(redo_action)
        edit_menu.addAction(redo_action)
  
        # Ação recortar
        cut_action = QAction("Recortar", self)
        cut_action.setStatusTip("Recortar texto")
  
        cut_action.triggered.connect(self.editor.cut)
        edit_toolbar.addAction(cut_action)
        edit_menu.addAction(cut_action)
  
        # Ação copiar
        copy_action = QAction("Copiar", self)
        copy_action.setStatusTip("Copiar texto")
  
        copy_action.triggered.connect(self.editor.copy)
        edit_toolbar.addAction(copy_action)
        edit_menu.addAction(copy_action)
  
        # Ação colar
        paste_action = QAction("Colar", self)
        paste_action.setStatusTip("Colar da área de transferência")
  
        paste_action.triggered.connect(self.editor.paste)
        edit_toolbar.addAction(paste_action)
        edit_menu.addAction(paste_action)
  
        # Ação selecionar tudo
        select_action = QAction("Selecionar tudo", self)
        select_action.setStatusTip("Selecionar todo texto")
  
        select_action.triggered.connect(self.editor.selectAll)
        edit_toolbar.addAction(select_action)
        edit_menu.addAction(select_action)
  
  
        # Demais ações
        wrap_action = QAction("Quebrar texto na janela", self)
        wrap_action.setStatusTip("Qubrar texto para próxima linha")
        
        wrap_action.setCheckable(True)
        wrap_action.setChecked(True)
  

        wrap_action.triggered.connect(self.edit_toggle_wrap)
        edit_menu.addAction(wrap_action)
        self.update_title()
        self.show()
  
    # Caixa de diálogo
    # Mostrando erros
    def dialog_critical(self, s):
  
        dlg = QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()
  
    # Chama ação para abertura de arquivo
    def file_open(self):
  
        path, _ = QFileDialog.getOpenFileName(self, "Abrir arquivo", "", 
                             "Documentos de texto (*.txt);Todos arquivos (*.*)")
  
        if path:
            try:
                with open(path, 'rU') as f:
                    # Lê o arquivo
                    text = f.read()
  
            except Exception as e:
                # Mostra erro
                self.dialog_critical(str(e))
                
            else:
                self.path = path
                self.editor.setPlainText(text)
                self.update_title()
  
    # Chama ação para salvar arquivo
    def file_save(self):

        if self.path is None:
            return self.file_saveas()

        self._save_to_path(self.path)
  
    # Chama ação para salvar como
    def file_saveas(self):
  

        path, _ = QFileDialog.getSaveFileName(self, "Salvar arquivo", "", 
                             "Documentos de texto (*.txt);Todos arquivos (*.*)")
  
        if not path:
            return

        self._save_to_path(path)

    def _save_to_path(self, path):
        text = self.editor.toPlainText()
        
        try:
  
            # Abre arquivo para escrever
            with open(path, 'w') as f:
                f.write(text)

        except Exception as e:
            self.dialog_critical(str(e))
  
        else:
            self.path = path
            self.update_title()
  
    # Chama ação para imprimir
    def file_print(self):
        dlg = QPrintDialog()

        if dlg.exec_():
            self.editor.print_(dlg.printer())

    def update_title(self):

        self.setWindowTitle("%s - Bloco de Notas" %(os.path.basename(self.path) 
                                                  if self.path else "Sem título"))
  
    # Chama ação para edição
    def edit_toggle_wrap(self):
  
        self.editor.setLineWrapMode(1 if self.editor.lineWrapMode() == 0 else 0 )
  
if __name__ == '__main__':
  
    app = QApplication(sys.argv)
  
    # Nome da aplicação
    app.setApplicationName("Bloco de Notas")
    window = MainWindow()
  
    app.exec_()