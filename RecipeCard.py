#!/usr/bin/env python
import PySide
from PySide import QtGui,QtCore

import configparser,sys,os
import NewCat
conf = configparser.ConfigParser()
conf.add_section("Recipe")
 
#savefile = 'GenericRecipe.ini'
 
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
 
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
 
 


class Ui_RecipeCard(QtGui.QWidget):  
    savefile = 'GenericRecipe.ini'
    def saveRecipe(self):
        dir = os.getcwd()
        if not str(dir).endswith("Recipes"):
            try:
                os.chdir("Recipes")
            except:
                os.chdir(os.pardir)        
        print("SaveButton Pressed :D")
        if not self.lineEdit.text() == None:
            self.savefile = self.lineEdit.text()+'.ini'
        conf.set("Recipe","Catagory",str(self.comboBox.currentText()) )      
        conf.set("Recipe","Name",self.lineEdit.text())
        conf.set("Recipe","Requirements", self.textEdit.toPlainText())
        conf.set("Recipe","Directions",self.textEdit_2.toPlainText())
        os.chdir( self.comboBox.currentText() )
        Recipe = open(self.savefile,'w')
        conf.write(Recipe)
       # savefile.close()
        Recipe.close()
        os.chdir(os.pardir)
        msg = QtGui.QMessageBox(self)
        
        msg.setWindowTitle("CookBook")
        msg.setText("Save Sucessful! - Close CookBook?")
        msg.NoRole=msg.addButton(QtGui.QMessageBox.NoButton)
        
        quit_msg = "Save Sucessful!\nClose CookBook?"
        reply = QtGui.QMessageBox.question(self, 'Message', 
                         quit_msg, QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
    
        if reply == QtGui.QMessageBox.Yes:    
            quit()
            #app.quit()
        else:
            pass
 
        '''
   def __init__(self):
       QWidget.__init__(self)
       self.setupUi(self)
       '''
    def setupUi(self, RecipeCard):
       # RecipeCard.setObjectName(_fromUtf8("RecipeCard"))
        RecipeCard.resize(640, 776)
       
        #self.resize(640,776)
        self.verticalLayout_2 = QtGui.QVBoxLayout(RecipeCard)
        #self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        #
        #
        '''
        self.img = QtGui.QLabel(Form)
        self.img.setPixmap('Creeper.png')
        self.verticalLayout.addWidget(self.img)
        self.img.show() 
        '''
        #
        #
               
        #self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.comboBox = QtGui.QComboBox(RecipeCard)
        #self.comboBox.setObjectName(_fromUtf8("comboBox"))
        
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
   
        self.verticalLayout.addWidget(self.comboBox)
    
        self.label = QtGui.QLabel(RecipeCard)
        #Here We Attempt To Allow User To Make New Catagories...
        self.newCat = QtGui.QPushButton("New Cataogry!?") 
        #self.verticalLayout.addWidget(self.newCat) 
        
        
        #self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        
   
        #
        
        self.lineEdit = QtGui.QLineEdit(RecipeCard)
        #self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.verticalLayout.addWidget(self.lineEdit)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.label_2 = QtGui.QLabel(RecipeCard)
        #self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_2.addWidget(self.label_2)
        self.textEdit = QtGui.QTextEdit(RecipeCard)
        #self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.verticalLayout_2.addWidget(self.textEdit)
        self.label_3 = QtGui.QLabel(RecipeCard)
        #self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_2.addWidget(self.label_3)
        self.textEdit_2 = QtGui.QTextEdit(RecipeCard)
        #self.textEdit_2.setObjectName(_fromUtf8("textEdit_2"))
        self.verticalLayout_2.addWidget(self.textEdit_2)
        self.pushButton = QtGui.QPushButton(RecipeCard)
        #self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.setText("Save Recipe!")
         #self.pushButton.setText(_translate("RecipeCard", "Save Recipe!", None))
        self.verticalLayout_2.addWidget(self.pushButton)
       
        """
        <:Testing Zone:>
        """
        #
        self.connect(self.pushButton,QtCore.SIGNAL("clicked()"),self.saveRecipe)
        self.connect(self.newCat,QtCore.SIGNAL("clicked()"),self.createCat)
        #self.pushButton.connect(self.pushButton, QtCore.SIGNAL('clicked()'), self.saveRecipe(self.savefile))                
          
        #
        """
        <:Testing Zone:>
        """
        self.retranslateUi(RecipeCard)
        QtCore.QMetaObject.connectSlotsByName(RecipeCard)
    def createCat(self):
        dir = os.getcwd()
        if not str(dir).endswith("Recipes"):
            try:
                os.chdir("Recipes")
            except:
                os.chdir(os.pardir)
                
                
        try:
            print("NewCat?")
            '''
            msg = QtGui.QMessageBox()
            msg.setText("Sorry, Not Yet Implemented...")
            msg.setWindowTitle("CookBook")
            msg.exec_()
            '''
             
            self.Form2 = QtGui.QWidget()
            self.ui2 = NewCat.Ui_Dialog()
            self.ui2.setupUi(self.Form2)
            self.Form2.show()
            
            
            
            
        except Exception as e:
            print("TraceStack?:\n"+str(e.with_traceback))
            print("\n\n"+str(e.args)+"\n\n")
            print(e)
                      
        
    def retranslateUi(self, RecipeCard):
            RecipeCard.setWindowTitle("CookBook - RecipeCard")
            #RecipeCard.setWindowTitle(_translate("RecipeCard", "PyCookBook - RecipeCard", None))
            self.comboBox.setItemText(0, _translate("RecipeCard", "Appitizers", None))
            self.comboBox.setItemText(1, _translate("RecipeCard", "Breads", None))
            self.comboBox.setItemText(2, _translate("RecipeCard", "Cake", None))
            self.comboBox.setItemText(3, _translate("RecipeCard", "Candy", None))
            self.comboBox.setItemText(4, _translate("RecipeCard", "Cookies", None))
            self.comboBox.setItemText(5, _translate("RecipeCard", "Desserts", None))
            self.comboBox.setItemText(6, _translate("RecipeCard", "Fish & SeaFood", None))
            self.comboBox.setItemText(7, _translate("RecipeCard", "Meat", None))
            self.comboBox.setItemText(8, _translate("RecipeCard", "Misc", None))
            self.comboBox.setItemText(9, _translate("RecipeCard", "Pies", None))
            self.comboBox.setItemText(10, _translate("RecipeCard", "Soups And Stews", None))
            self.comboBox.setItemText(11, _translate("RecipeCard", "Vegetables", None))
            self.label.setText(_translate("RecipeCard", "Recipe Name:", None))
            self.label_2.setText(_translate("RecipeCard", "Ingredients:", None))
            self.textEdit.setHtml(_translate("RecipeCard", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
    "p, li { white-space: pre-wrap; }\n"
    "</style></head><body style=\" font-family:\'Source Sans Pro\'; font-size:13pt; font-weight:200; font-style:normal;\">\n"
    "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
            self.label_3.setText(_translate("RecipeCard", "Directions:", None))






if __name__ == "__main__":
    import sys
    dir = "."
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_RecipeCard()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())