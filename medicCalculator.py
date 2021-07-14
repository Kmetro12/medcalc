'''
Created on Jun 29, 2021

@author: Silvermoon
'''
import kivy #importing kivy and various tools needed 
from kivy.app import App
from kivy.uix.label import Label 
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button
from kivy.graphics import * 
from matplotlib.backend_bases import button_press_handler
from kivy.uix.textinput import TextInput


'''
class widget(Widget): #A class to inherit widgets 
    pass

class pop(FloatLayout):#class for float layout for the disclaimer 
    pass

def disclaimerPop(): #disclaimer function for the application 
    layout = GridLayout(cols=1, padding=10) #creating the layout to place labels and buttons on 
    
    #creating the text for the layout and adding it to the screen  
    layout.add_widget(Label(text="This application is intended to check the provides math. \nIf any discrepancies" +
                            "arise refer to providers hand-written math, and re-check ALL calculations. \nDo you agree to these terms of serive? ", padding=[10,10],
                            size_hint=(0.9,0.9),text_size=(200,200), halign='left'))#textsize to scale label with popup window 
    
    #creating and adding buttons to disclaimer popup 
    btnYes = Button(text="Accept", size_hint=(0.4,0.4), pos_hint=(20,20))#changing the button size and other attributes 
    layout.add_widget(btnYes)
    btnNo = Button(text="No", size_hint=(0.4,0.4),pos_hint=(20,20))
    layout.add_widget(btnNo)
    
    disclaimerWindow = Popup(title="disclaimer", content=layout, size_hint=(0.9,0.9), size=(400,400),auto_dismiss=False) # pos_hint={'x': 10.0,'y':10.0},size hint changes size of popup
    disclaimerWindow.opacity = 1 #setting the opacity of the disclaimer window 
    disclaimerWindow.open() #opening and above creating the popup window 
    
    #define function for button actions
    def pressYes(self):
        disclaimerWindow.dismiss()#closing the popup window  

    def pressNo(self):
        medCalc().stop() #exiting the program 
        
    #adding actions to the buttons 
    btnYes.bind(on_press=pressYes)
    btnNo.bind(on_press=pressNo)
'''
def homeScreen():
    pass
    
 #calling the disclaimer function
    
class medCalcNight(RelativeLayout):#the medcalc nightmode class 
     
    def __init__(self,**kwargs):#creating the constructor 
        super(medCalcNight, self).__init__(**kwargs)
        self.cols = 1 #define number of colums   

        layoutHome = RelativeLayout() #creating the innerlayout
        
        lblDisclaimer = (Label(text="This application is intended to check the provides math. \nIf any discrepancies" +
                            "arise refer to providers hand-written \nmath, and re-check ALL calculations. \nDo you agree to these terms of serive?",pos_hint={'center_x':0.6, 'center_y':0.8} )
                              )#
        layoutHome.add_widget(lblDisclaimer)
        
        #creating and adding buttons to disclaimer Window
        btnYes = Button(text="Accept", size_hint=(0.5,0.2), pos_hint={'x':0.32, 'y':0.1})#Place button bottom center can also use {'center_x': 0, 'center_y':0} 
        layoutHome.add_widget(btnYes)
        btnNo = Button(text="Decline", size_hint=(0.5,0.2),pos_hint={'x':0.32, 'y':0.3}) #place button on top of accept button 
        layoutHome.add_widget(btnNo)
        
        #-----Functions for Disclaimer-----
        def pressYes(self):
            layoutHome.clear_widgets()#clears all widgets from the frame 
            createHomePage(self) 
            #disclaimerWindow.dismiss()#closing the popup window  
            pass
        def pressNo(self):
            medCalc().stop() #exiting the program 
            
        #-----Misc Functions---------------
        def clearScreen():
            layoutHome.clear_widgets() 
            
        #---------------------------------- 
        #Creating the Homepage 
        #----------------------------------         
        def createHomePage(self):
            lblHomePageTest = Label(text="Please Select Problem Type: ",size_hint=(0.3,0.1), pos_hint={'x':0.32, 'y':0.7})
            layoutHome.add_widget(lblHomePageTest)
            
            #adding buttons to problem types 
            btnSupply = Button(text="Supply per 1mL",size_hint=(0.3,0.1), pos_hint={'x':0.32, 'y':0.6})
            btnSupply.bind(on_press=Supply)#binding the button to a function 
            layoutHome.add_widget(btnSupply)
            
            btnIvp = Button(text="IV Push",size_hint=(0.3,0.1), pos_hint={'x':0.32, 'y':0.5})
            btnIvp.bind(on_press=IvPush)
            layoutHome.add_widget(btnIvp)
            
            btnIvd = Button(text="IV Drip Problem",size_hint=(0.3,0.1), pos_hint={'x':0.32, 'y':0.4} )
            btnIvd.bind(on_press=IvDrip)
            layoutHome.add_widget(btnIvd)
            
            btnDopa = Button(text="Dopamine Problem",size_hint=(0.3,0.1), pos_hint={'x':0.32, 'y':0.3})
            btnDopa.bind(on_press=Dopamine)
            layoutHome.add_widget(btnDopa)
            
            btnConvert = Button(text="Conversion",size_hint=(0.3,0.1), pos_hint={'x':0.32, 'y':0.2})
            btnConvert.bind(on_press=Conversion)
            layoutHome.add_widget(btnConvert)
            
            btnSettings = Button(text="Settings",size_hint=(0.3,0.1),pos_hint={'x':0.32, 'y':0.1})
            btnSettings.bind(on_press=Settings)
            layoutHome.add_widget(btnSettings)
        #---------------------------------- 
        #End Create Homepage  
        #----------------------------------
        #---------------------------------- 
        #Start Supply Fx
        #----------------------------------
        def Supply(self):
            
            clearScreen() #clearing the screen to place supply problem, and title label   
            result = str("") #creating a string variable so result can then be placed in text box 
            
            lblSupply = Label(text="Find supply per 1mL",size_hint=(0.3,0.1), pos_hint={'x':0.32, 'y':0.7})
            layoutHome.add_widget(lblSupply)
            
            #creating buttons for supply 
            lblMgs = Label(text="Enter milligrams (Mgs): ",size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.6})
            layoutHome.add_widget(lblMgs)
            txtMgs = TextInput(size_hint=(0.3,0.1), pos_hint={'x':0.42, 'y':0.6}, multiline=False)
            layoutHome.add_widget(txtMgs)
            
            lblMls = Label(text="Enter milliliters (Mls): ",size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.5})
            layoutHome.add_widget(lblMls)
            txtMls = TextInput(size_hint=(0.3,0.1), pos_hint={'x':0.42, 'y':0.5}, multiline=False)
            layoutHome.add_widget(txtMls)
            
            lblMgspMl = Label(text="Milligrams per 1 mL: ",size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.4})
            layoutHome.add_widget(lblMgspMl)
            
            txtAnswerSupp = TextInput(size_hint=(0.3,0.1), pos_hint={'x':0.42, 'y':0.4}, multiline=False, disabled=True) #disabled sets text input to read only 
            layoutHome.add_widget(txtAnswerSupp)
            
            #adding buttons to return to homescreen and calculate problem 
            def returnHome(self):
                clearScreen()
                createHomePage(self)
                
            def supplyCalc(self):
                
                try: #try catch loop for user errors 
                    MgsNum = float(txtMgs.text)#Converting TextInput to Float 
                    MlsNum = float(txtMls.text)
                    
                    answer = round(MgsNum/MlsNum,5) #rounding the answer to 5 decimal places
                    txtAnswerSupp.text = str(answer)#converting the answer back to a string and placing into text input box 
                except:
                    answer = "ERROR" #if exception is thrown then give error for answer 
                    txtAnswerSupp.text = answer
             
            btnReturnHome = Button(text="Return to Homescreen",size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.3})
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
            
            btnCalculate = Button(text="Calculate",size_hint=(0.3,0.1), pos_hint={'x':0.45, 'y':0.3})
            btnCalculate.bind(on_press=supplyCalc)
            layoutHome.add_widget(btnCalculate)
            
        #---------------------------------- 
        #End Supply Fx  
        #----------------------------------
        
        def IvPush(self):
            pass
        def IvDrip(self):
            pass
        def Dopamine(self):
            pass
        def Conversion(self):
            pass
        def Settings(self):
            pass

        
        #adding actions to the buttons for disclaimer 
        btnYes.bind(on_press=pressYes)
        btnNo.bind(on_press=pressNo)
        
 
        
        self.add_widget(layoutHome)#adding the innerlayout to the root 
        
        #disclaimerPop()
class medCalc(App): #building the application 
    def build(self):
        return medCalcNight() 

if __name__ == "__main__": #running the application 
    medCalc().run()
    