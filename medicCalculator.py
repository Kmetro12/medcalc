'''
Created on Jun 29, 2021

@author: Silvermoon
'''
import kivy #importing kivy and various tools needed 
from kivymd.app import App
from kivy.uix.label import Label 
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.button import Button


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
            createHomePage() 
            #disclaimerWindow.dismiss()#closing the popup window  
            pass
        def pressNo(self):
            medCalc().stop() #exiting the program 
        #---------------------------------- 
        #Creating the Homepage 
        #---------------------------------- 
        
        def createHomePage():
            lblHomePageTest = Label(text="TesthingLabel")
            layoutHome.add_widget(lblHomePageTest)
        #adding actions to the buttons 
        btnYes.bind(on_press=pressYes)
        btnNo.bind(on_press=pressNo)
        
        self.add_widget(layoutHome)#adding the innerlayout to the root 
        
        #disclaimerPop()
class medCalc(App): #building the application 
    def build(self):
        return medCalcNight() 

if __name__ == "__main__": #running the application 
    medCalc().run()
