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
#from matplotlib.backend_bases import button_press_handler
from kivy.uix.textinput import TextInput
from kivy.core.window import Window #setting the window size in kivy 
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown

#Window.clearcolor =(0,0,0,0)#setting the color of the window
#Window.size=(360,600) # setting the window size 
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
        
        lblDisclaimer = (Label(text="This application is intended to check the \nprovides math. If any discrepancies\n" +
                            "arise refer to providers hand-written math, \nand re-check ALL calculations. \nDo you agree to these terms of serive?",pos_hint={'center_x':0.5, 'center_y':0.8} )
                              )#
        layoutHome.add_widget(lblDisclaimer)
        
        #creating and adding buttons to disclaimer Window
        btnYes = Button(text="Accept", size_hint=(0.5,0.2), pos_hint={'center_x':0.5, 'center_y':0.3})#Place button bottom center can also use {'center_x': 0, 'center_y':0} 
        layoutHome.add_widget(btnYes)
        btnNo = Button(text="Decline", size_hint=(0.5,0.2),pos_hint={'center_x':0.5, 'center_y':0.5}) #place button on top of accept button 
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
            lblHomePageTest = Label(text="Please Select Problem Type: ",size_hint=(0.3,0.1), pos_hint={'x':0.362, 'y':0.85})
            layoutHome.add_widget(lblHomePageTest)
            
            #adding buttons to problem types 
            btnSupply = Button(text="Supply per 1mL",size_hint=(0.4,0.1), pos_hint={'x':0.32, 'y':0.75})
            btnSupply.bind(on_press=Supply)#binding the button to a function 
            layoutHome.add_widget(btnSupply)
            
            btnIvp = Button(text="IV Push",size_hint=(0.4,0.1), pos_hint={'x':0.32, 'y':0.65})
            btnIvp.bind(on_press=IvPush)
            layoutHome.add_widget(btnIvp)
            
            btnIvd = Button(text="IV Drip Problem",size_hint=(0.4,0.1), pos_hint={'x':0.32, 'y':0.55} )
            btnIvd.bind(on_press=IvDrip)
            layoutHome.add_widget(btnIvd)
            
            btnDopa = Button(text="Dopamine Problem",size_hint=(0.4,0.1), pos_hint={'x':0.32, 'y':0.45})
            btnDopa.bind(on_press=Dopamine)
            layoutHome.add_widget(btnDopa)
            
            btnConvert = Button(text="Conversion",size_hint=(0.4,0.1), pos_hint={'x':0.32, 'y':0.35})
            btnConvert.bind(on_press=Conversion)
            layoutHome.add_widget(btnConvert)
            
            btnSettings = Button(text="Settings",size_hint=(0.4,0.1),pos_hint={'x':0.32, 'y':0.25})
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
            
            lblSupply = Label(text="Find supply per 1mL",size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9})
            layoutHome.add_widget(lblSupply)
            
            #creating buttons for supply 
            lblMgs = Label(text="Enter milligrams\n                (MG): ",size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.8})
            layoutHome.add_widget(lblMgs)
            entrMgs = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.82}, multiline=False)
            layoutHome.add_widget(entrMgs)
            
            lblMls = Label(text="Enter milliliters\n                 (mL): ",size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.74})
            layoutHome.add_widget(lblMls)
            entrMls = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.76}, multiline=False)
            layoutHome.add_widget(entrMls)
            
            lblMgspMl = Label(text="      Milligrams \n         per 1 mL: ",size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.68})
            layoutHome.add_widget(lblMgspMl)
            
            txtAnswerSupp = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.7}, multiline=False, disabled=True) #disabled sets text input to read only 
            layoutHome.add_widget(txtAnswerSupp)
            
            #adding buttons to return to homescreen and calculate problem 
            def returnHome(self):
                clearScreen()
                createHomePage(self)
                
            def supplyCalc(self):
                
                try: #try catch loop for user errors 
                    MgsNum = float(entrMgs.text)#Converting TextInput to Float 
                    MlsNum = float(entrMls.text)
                    
                    answer = round(MgsNum/MlsNum,5) #rounding the answer to 5 decimal places
                    txtAnswerSupp.text = str(answer)#converting the answer back to a string and placing into text input box 
                except:
                    answer = "ERROR" #if exception is thrown then give error for answer 
                    txtAnswerSupp.text = answer
             
            btnReturnHome = Button(text="Return to Home",size_hint=(0.35,0.1), pos_hint={'x':0.18, 'y':0.59})
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
            
            btnCalculate = Button(text="Calculate",size_hint=(0.3,0.1), pos_hint={'x':0.53, 'y':0.59})
            btnCalculate.bind(on_press=supplyCalc)
            layoutHome.add_widget(btnCalculate)
            
        #---------------------------------- 
        #End Supply Fx  
        #----------------------------------
        
        def IvPush(self):
            clearScreen()
            
            lblIvPush = Label(text="IV Push Problem", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9})
            layoutHome.add_widget(lblIvPush)
            
            lblDoseMg = Label(text="Enter Dose (Mg): ", size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.8})
            layoutHome.add_widget(lblDoseMg) 
            entrMG = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.82}, multiline=False)
            layoutHome.add_widget(entrMG)
            
            lblSuppml = Label(text="Supply per \n1mL(Mg/1mL): ", size_hint=(0.3,0.1), pos_hint={'x':0.13, 'y':0.74})
            layoutHome.add_widget(lblSuppml)
            entrML = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.76}, multiline=False)
            layoutHome.add_widget(entrML)
            
            lblMlstoDraw = Label(text="mLs to Draw: ", size_hint=(0.3,0.1), pos_hint={'x':0.13, 'y':0.68})
            layoutHome.add_widget(lblMlstoDraw) 
            entrAnswer = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.7}, multiline=False, disabled=True)
            layoutHome.add_widget(entrAnswer)
            
            #adding buttons to return to homescreen and calculate problem 
            def returnHome(self):
                clearScreen()
                createHomePage(self)
            
            def ivpCalc(self):
                
                try:#error handling 
                    mgsNum = float(entrMG.text)#converting text input to float 
                    mlsNum = float(entrML.text)
                    
                    answer = round(mgsNum/mlsNum,5)
                    entrAnswer.text = str(answer)#converting the answer back to a string and placing into text input box 
                except:    
                    answer = "ERROR"
                    entrAnswer.text = answer                     
            
            btnReturnHome = Button(text="Return to Home",size_hint=(0.35,0.1), pos_hint={'x':0.18, 'y':0.59})
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
            
            btnCalculate = Button(text="Calculate",size_hint=(0.3,0.1), pos_hint={'x':0.53, 'y':0.59})
            btnCalculate.bind(on_press=ivpCalc)
            layoutHome.add_widget(btnCalculate)
            

            
        def IvDrip(self):
            
            clearScreen()
            
            lblIvDrip = Label(text="Iv Drip Problem", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9})
            layoutHome.add_widget(lblIvDrip)
            
            lblMgTotal = Label(text="Total Amt to \nGive(Mg/min): ", size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.8})
            layoutHome.add_widget(lblMgTotal)
            entrMgTotal = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.82}, multiline=False)
            layoutHome.add_widget(entrMgTotal)
            
            lblDropset = Label(text="Enter Dropset: ", size_hint=(0.3,0.1), pos_hint={'x':0.13, 'y':0.74})
            layoutHome.add_widget(lblDropset)
            entrDropset = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.76}, multiline=False)
            layoutHome.add_widget(entrDropset)
            
            lblConcml = Label(text="Concentration\n(Mg/1mL): ", size_hint=(0.3,0.1), pos_hint={'x':0.13, 'y':0.68})
            layoutHome.add_widget(lblConcml)
            entrConc = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.7}, multiline=False)
            layoutHome.add_widget(entrConc)
            
            lblDripRate = Label(text="Drops per Minute\n(gtts/min): ", size_hint=(0.3,0.1), pos_hint={'x':0.13, 'y':0.62})
            layoutHome.add_widget(lblDripRate)
            entrDripRate = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.64}, multiline=False, disabled=True)
            layoutHome.add_widget(entrDripRate)
            
            #adding buttons to return to homescreen and calculate problem 
            def returnHome(self):
                clearScreen()
                createHomePage(self)
                
            def ivDripCalc(self):
                try:
                    mgNum = float(entrMgTotal.text)
                    dropNum = float(entrDropset.text)
                    concNum = float(entrConc.text)
                    
                    answer = round(mgNum*dropNum/concNum,5)
                    entrDripRate.text = str(answer)
                except:
                    answer = "ERROR"
                    entrDripRate.text = answer
                
            btnReturnHome = Button(text="Return to Home",size_hint=(0.35,0.1), pos_hint={'x':0.18, 'y':0.5})
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
            
            btnCalculate = Button(text="Calculate",size_hint=(0.3,0.1), pos_hint={'x':0.53, 'y':0.5})
            btnCalculate.bind(on_press=ivDripCalc)
            layoutHome.add_widget(btnCalculate)
            
        def Dopamine(self):
            clearScreen()
            
            lblDopamine = Label(text="Dopamine Problem", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9})
            layoutHome.add_widget(lblDopamine)
            
            lblMcgDose = Label(text="Dose (mcg/min): ", size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.8})
            layoutHome.add_widget(lblMcgDose)
            entrMcgDose = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.82}, multiline=False)
            layoutHome.add_widget(entrMcgDose)
            
            lblKgwt = Label(text="Weight in Kg: ", size_hint=(0.3,0.1), pos_hint={'x':0.13, 'y':0.74})
            layoutHome.add_widget(lblKgwt)
            entrKgwt = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.76}, multiline=False)
            layoutHome.add_widget(entrKgwt)
            
            lblDropset = Label(text="Dropset: ", size_hint=(0.3,0.1), pos_hint={'x':0.13, 'y':0.68})
            layoutHome.add_widget(lblDropset)
            entrDropset = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.7}, multiline=False, disabled=True)
            entrDropset.text = str(60)#adding the 60 dropset in for user to see 
            layoutHome.add_widget(entrDropset)
            
            lblConcMcg = Label(text="Concentration \n      (mcg/mL): ", size_hint=(0.3,0.1), pos_hint={'x':0.13, 'y':0.62})
            layoutHome.add_widget(lblConcMcg)
            entrConcMcg = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.64}, multiline=False)
            layoutHome.add_widget(entrConcMcg)
            
            lblDopaAns = Label(text="Drops per Minute \n          (gtts/min): ", size_hint=(0.3,0.1), pos_hint={'x':0.13,'y':0.56})
            layoutHome.add_widget(lblDopaAns)
            entrDopaAns = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.58}, multiline=False, disabled=True)
            layoutHome.add_widget(entrDopaAns)
            
            #adding buttons to return to homescreen and calculate problem 
            def returnHome(self):
                clearScreen()
                createHomePage(self)
                
            def DopamineCalc(self):
                try:
                    mcgMinNum = float(entrMcgDose.text)
                    kgwtNum = float(entrKgwt.text)
                    DropsetNum = float(entrDropset.text) #adding the dropset number 60 for the calculation 
                    concDopaNum = float(entrConcMcg.text)
                    
                    answer = round(mcgMinNum*kgwtNum*DropsetNum/concDopaNum,5)
                    entrDopaAns.text= str(answer)
                    
                except: 
                    answer = "ERROR"
                    entrDopaAns.text = str(answer)
                
            btnReturnHome = Button(text="Return to Home",size_hint=(0.35,0.1), pos_hint={'x':0.18, 'y':0.44})
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
            
            btnCalculate = Button(text="Calculate",size_hint=(0.3,0.1), pos_hint={'x':0.53, 'y':0.44})
            btnCalculate.bind(on_press=DopamineCalc)
            layoutHome.add_widget(btnCalculate)

        
        
        def Conversion(self):
            
            clearScreen()
            
            lblConversion = Label(text="Conversions", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9})
            layoutHome.add_widget(lblConversion)
            
            lblNumberOne = Label(text="Number One ", size_hint=(0.3,0.1), pos_hint={'x':0.08, 'y':0.8})
            layoutHome.add_widget(lblNumberOne)
            entrNumberOne = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.38, 'y':0.82}, multiline=False)
            layoutHome.add_widget(entrNumberOne)
            
            #creating the dropdown list for number1 
            
            numOneDrop = DropDown()
            numOneUnits = ["mg",'g','mcg', 'ibs', 'kg']
          
            #looping through the units           
            for i in numOneUnits:
                btnNumOneUnits = Button(text= i,size_hint_y=None, height=44)#creating the buttons with parameters, can also for '%r' for text
                btnNumOneUnits.bind(on_release=lambda btnNumOneUnits: numOneDrop.select(btnNumOneUnits.text))#binding the button to then set to its text 
                numOneDrop.add_widget(btnNumOneUnits)#adding the buttons the the screen
           
            #--------------------------------------------------------------------------------------------------------
            
            lblConvertTo = Label(text="Convert to", size_hint=(0.3,0.1), pos_hint={'x':0.08, 'y':0.74})
            layoutHome.add_widget(lblConvertTo)
            
            #creating the dropdown list for convert to
            unitsDrop = DropDown()
            unitsList = ["mg",'g','mcg', 'ibs', 'kg']
            
            #looping through the units           
            for i in unitsList:
                btnUnits = Button(text=i,size_hint_y=None, height=44)#creating the buttons with parameters
                btnUnits.bind(on_release=lambda btnUnits: unitsDrop.select(btnUnits.text))#binding the button to then set to its text 
                unitsDrop.add_widget(btnUnits)#adding the buttons the the screen 
                
            #creating the main button for Convert to
            btnSelect = Button(text='Select Units',size_hint=(0.3,0.09), pos_hint={'x':0.38, 'y':0.74})
            btnSelect.bind(on_release=unitsDrop.open)
            layoutHome.add_widget(btnSelect)
            unitsDrop.bind(on_select=lambda instance, x: setattr(btnSelect, 'text',x))
            
            #creating the main button for Num1 Convert units 
            btnSelectOne = Button(text='Select Units',size_hint=(0.3,0.07), pos_hint={'x':0.68, 'y':0.81})
            btnSelectOne.bind(on_release=numOneDrop.open)
            layoutHome.add_widget(btnSelectOne)
            numOneDrop.bind(on_select=lambda instance, x: setattr(btnSelectOne, 'text',x))
            
            
            lblConvertAns = Label(text="Answer", size_hint=(0.3,0.1), pos_hint={'x':0.08,'y':0.68})#answer for the conversion output and label 
            layoutHome.add_widget(lblConvertAns)
            entrConvertAns = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.38, 'y':0.7}, multiline=False, disabled=True)
            layoutHome.add_widget(entrConvertAns)
            

            #------------------------------------------------------------
            #adding buttons to return to homescreen and calculate problem 
            def returnHome(self):
                clearScreen()
                createHomePage(self)
            def conversionCalc(self):
                

                try:
                    unitOne = float(entrNumberOne.text)
                    oneG = 1000 #one gream = 1000 milligrams 
                    
                except: 
                    answer = "ERROR"
                    entrConvertAns.text = str(answer) 
                    
                if btnSelectOne.text == "mcg" and btnSelect.text == "mg": #converts micrograms to milligrams 
                    mcgsTomgs = unitOne*0.001
                    round(mcgsTomgs,5)#using the round function to round the answer to 5 decimal places 
                    entrConvertAns.text = str(mcgsTomgs)
                if btnSelectOne.text == "mcg" and btnSelect.text == "mg": #converts micrograms to grams
                    mcgsTogs = unitOne/1000000
                    round(mcgsTogs,5)
                    entrConvertAns.text=str(mcgsTogs)
                
                if btnSelectOne.text == "mg" and btnSelect.text == "mcg": #converts milligrams to micrograms 
                    mgsTomcgs = unitOne*1000
                    round(mgsTomcgs,5)#using the round function to round the answer to 5 decimal places 
                    entrConvertAns.text = str(mgsTomcgs)
                if btnSelectOne.text == "mg" and btnSelect.text == "g": #converts milligrams to grams
                    mgsTogs = unitOne/1000
                    round(mgsTogs,5)
                    entrConvertAns.text=str(mgsTogs)
                    
                if btnSelectOne.text == "g" and btnSelect.text == "mcg": #converts grams to micrograms 
                    gsTomcgs = unitOne*1000000
                    round(gsTomcgs,5)#using the round function to round the answer to 5 decimal places 
                    entrConvertAns.text = str(gsTomcgs)
                if btnSelectOne.text == "g" and btnSelect.text == "mg": #converts grams to milligrams
                    gsTomg = unitOne*1000
                    round(gsTomg,5)
                    entrConvertAns.text=str(gsTomg)
                
                if btnSelectOne.text == "ibs" and btnSelect.text == "kg": #convert pounds to kilograms 
                    ibsTokg = unitOne/2.20462
                    round(ibsTokg,5)
                    entrConvertAns.text = str(ibsTokg)
                if btnSelectOne.text == "kg" and btnSelect.text == "ibs": #convert kilograms to pounds 
                    kgToibs = unitOne*2.2046
                    round(kgToibs,5)
                    entrConvertAns.text = str(kgToibs)
                    
                if btnSelectOne.text == "ibs" and btnSelect.text == "ibs": #pounds to pounds
                    entrConvertAns.text = str(unitOne)
                if btnSelectOne.text == "kg" and btnSelect.text == "kg": #kilograms to Kilograms 
                    entrConvertAns.text = str(unitOne)
               
            btnCalculate = Button(text="Convert",size_hint=(0.3,0.1), pos_hint={'x':0.53, 'y':0.44})
            btnCalculate.bind(on_press=conversionCalc)
            layoutHome.add_widget(btnCalculate)
                
            btnReturnHome = Button(text="Return to Home",size_hint=(0.35,0.1), pos_hint={'x':0.18, 'y':0.44})
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
         
        def Settings(self):
            
            clearScreen()
            
            lblSettings = Label(text="Settings", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9})
            layoutHome.add_widget(lblSettings)
            
            lblDayMode = Label(text="Day Mode:", size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.8})
            layoutHome.add_widget(lblDayMode)
            chkDayMode = CheckBox(group=1, size_hint=(0.3,0.1), pos_hint={'x':0.3, 'y':0.8})
            layoutHome.add_widget(chkDayMode)
                  
            lblNightMode = Label(text="Night Mode:", size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.74})
            layoutHome.add_widget(lblNightMode)
            chkNightMode = CheckBox(group=1, size_hint=(0.3,0.1), pos_hint={'x':0.3, 'y':0.74})#setting active to true for night mode so app does not switch modes 
            layoutHome.add_widget(chkNightMode)
            
            lblBig = Label(text="Big Mode:", size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.68})
            layoutHome.add_widget(lblBig)
            chkBig = CheckBox(group=1, size_hint=(0.3,0.1), pos_hint={'x':0.3, 'y':0.68})
            layoutHome.add_widget(chkBig)
            
            def switchModes(self):
                if chkNightMode.active == True:
                    print("Night Mode")
                if chkDayMode.active == True:
                    print("Day Mode")
                if chkBig.active == True:
                    print("Big")
            '''
            #creating the option list for the checkboxes 
            options = [
                ("Night Mode", "n"),
                ("Day Mode", "d"), 
                ("Big Mode", "b")
                ]
            
            selection = str("n")#setting variable selection to convert options to string, initialize value to mode, change in various classes  
            
            #looping the check boxes on the screen 
            r=0.8 #initializing r value for 0.8
            for text, mode in options:#for loop to create three radio buttons, DOES NOT CURRENTLY PRINT TEXT FROM OPTIONS  
                radioButtonss = CheckBox(group=1, pos_hint={'x':0.3, 'y':r}) #using this to place buttons on screen and not overlap 
                layoutHome.add_widget(radioButtonss)#variable=selection,value=mode,text=text, size_hint=(0.3,0.1),
                r-=0.06 #used for position the relative layout buttons 
            

            #switchModes function 
            def switchModes(self):
                selectedButton = selection.get() #gets the selected variable 
            
                if(selectedButton == "n"):
                    pass
                if (selectedButton =="d"):
                    print("hi")
                if(selectedButton =="b"):
                    print("bye")
            '''
            #adding buttons to return to homescreen and calculate problem 
            def returnHome(self):
                clearScreen()
                createHomePage(self)
                
            btnReturnHome = Button(text="Return to Home",size_hint=(0.35,0.1), pos_hint={'x':0.18, 'y':0.44})
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
            
            btnCalculate = Button(text="Switch Modes",size_hint=(0.3,0.1), pos_hint={'x':0.53, 'y':0.44})
            btnCalculate.bind(on_press=switchModes)
            layoutHome.add_widget(btnCalculate)
            #grouping check boxes for selection buttons to get effect of a radio button 
            
            '''
            #creating a check box function 
            def checkBoxActive(checkbox,value):
                if value:
                    print('The check box', checkbox, 'is active')
                else:
                    print('The check box', checkbox, 'IS NOT ACTIVE')
                    
            checkbox = CheckBox()
            checkbox.bind(active=checkBoxActive) 
            layoutHome.add_widget(checkbox)
             '''

        
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
