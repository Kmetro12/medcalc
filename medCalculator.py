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
from kivy.uix.textinput import TextInput
from kivy.core.window import Window #setting the window size in kivy 
from kivy.uix.checkbox import CheckBox
from kivy.uix.dropdown import DropDown
from kivy.config import Config # allows usage of custom made icons 
from kivy.uix.behaviors.focus import FocusBehavior
from kivy.uix.behaviors import ButtonBehavior

#Window.clearcolor =(0,0,0,0)#setting the color of the window
Window.size=(360,600) # setting the window size 

class medCalcDayApp(App): #running the day application 
    def build(self):
        return medCalcDay()
class medCalcBigApp(App): #running the class for the big application 
    def build(self):
        return medCalcBig()

class medCalcNight(RelativeLayout):#the medcalc nightmode class 
     
    def __init__(self,**kwargs):#creating the constructor 
        super(medCalcNight, self).__init__(**kwargs)
        Window.clearcolor=(0.157,0.157,0.157,1)# setting the background window color 
        layoutHome = RelativeLayout() #creating the innerlayout
        lblDisclaimer = (Label(text="This application is intended to check the \nprovides math. If any discrepancies\n" +
                            "arise refer to providers hand-written math, \nand re-check ALL calculations. \nDo you agree to these terms of serive?",pos_hint={'center_x':0.5, 'center_y':0.8} )
                              )#
        layoutHome.add_widget(lblDisclaimer)
        
        #creating and adding buttons to disclaimer Window
        btnYes = Button(text="Accept", size_hint=(0.5,0.2), pos_hint={'center_x':0.5, 'center_y':0.3},
                        color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))#Place button bottom center can also use {'center_x': 0, 'center_y':0} 
        layoutHome.add_widget(btnYes) #adding button to screen 
        btnNo = Button(text="Decline", size_hint=(0.5,0.2),pos_hint={'center_x':0.5, 'center_y':0.5},
                       color=(.9,.9,.9,1),background_color=(.8,.8,.8,1)) #place button on top of accept button 
        layoutHome.add_widget(btnNo)
        #-----Functions for Disclaimer-----
        def pressYes(self):
            layoutHome.clear_widgets()#clears all widgets from the frame 
            createHomePage(self)  
        def pressNo(self):
            medCalc().stop() #exiting the program 
        #-----Misc Functions---------------
        def clearScreen():
            layoutHome.clear_widgets()     
        #---------------------------------- 
        #Creating the Homepage 
        #----------------------------------         
        def createHomePage(self):
            Window.clearcolor=(0.157,0.157,0.157,1)# setting the background window color 
            lblHomePageTest = Label(text="Please Select Problem Type: ",size_hint=(0.3,0.1), pos_hint={'x':0.362, 'y':0.88},color=(.9,.9,.9,1)) #color = how to change label text color 
            layoutHome.add_widget(lblHomePageTest)
            
            #adding buttons to problem types 
            btnSupply = Button(text="Supply per 1mL",size_hint=(0.4,0.1), pos_hint={'x':0.32, 'y':0.78},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
            btnSupply.bind(on_press=Supply)#binding the button to a function, RGBA decimals divide by 255 
            layoutHome.add_widget(btnSupply)
            
            btnIvp = Button(text="IV Push",size_hint=(0.4,0.1), pos_hint={'x':0.32, 'y':0.68},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
            btnIvp.bind(on_press=IvPush)
            layoutHome.add_widget(btnIvp)
            
            btnIvd = Button(text="IV Drip Problem",size_hint=(0.4,0.1), pos_hint={'x':0.32, 'y':0.58},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
            btnIvd.bind(on_press=IvDrip)
            layoutHome.add_widget(btnIvd)
            
            btnDopa = Button(text="Dopamine Problem",size_hint=(0.4,0.1), pos_hint={'x':0.32, 'y':0.48},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
            btnDopa.bind(on_press=Dopamine)
            layoutHome.add_widget(btnDopa)
            
            btnivInfusion = Button(text="Infusion Problem",size_hint=(0.4,0.1),pos_hint={'x':0.32,'y':0.38},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
            btnivInfusion.bind(on_press=ivInfusion)
            layoutHome.add_widget(btnivInfusion)
            
            btnConvert = Button(text="Conversion",size_hint=(0.4,0.1), pos_hint={'x':0.32, 'y':0.28},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
            btnConvert.bind(on_press=Conversion)
            layoutHome.add_widget(btnConvert)
            
            btnFormulas = Button(text="Formulas/O2/Burn",size_hint=(0.4,0.1),pos_hint={'x':0.32,'y':0.18},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
            btnFormulas.bind(on_press=formulasPage)
            layoutHome.add_widget(btnFormulas)
            
            btnSettings = Button(text="Settings",size_hint=(0.4,0.1),pos_hint={'x':0.32, 'y':0.08},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
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
            
            lblSupply = Label(text="Find supply per 1mL",size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblSupply)
            
            #creating buttons for supply 
            lblMgs = Label(text="Enter milligrams\n                (MG): ",size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.8},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblMgs)
            entrMgs = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.82}, multiline=False, cursor_color=(0,0,0,1), unfocus_on_touch=False)
            layoutHome.add_widget(entrMgs)
            
            lblMls = Label(text="Enter milliliters\n                 (mL): ",size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.74},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblMls)
            entrMls = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.76}, multiline=False, cursor_color=(0,0,0,1), unfocus_on_touch=False)
            layoutHome.add_widget(entrMls)
            
            lblMgspMl = Label(text="      Milligrams \n         per 1 mL: ",size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.68},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblMgspMl)
            
            txtAnswerSupp = TextInput(size_hint=(0.3,0.058), pos_hint={'x':0.48, 'y':0.7}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.91,0.91,0.031,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=20)#setbackground disabled to white first to avoid grey tint 
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
                    txtAnswerSupp.text = str((answer))#converting the answer back to a string and placing into text input box 
                except:
                    answer = "ERROR" #if exception is thrown then give error for answer 
                    txtAnswerSupp.text = answer
            
            #creating the button number function,   
            def buttonText(instance): #creating an output to print the button text 
                if entrMgs.focus == True:  #partially working, need to figure out how to get focus on textinput
                    entrMgs.text += instance.text
                if entrMls.focus == True: 
                    entrMls.text += instance.text

            def clearAll(self): #clearing all the text off the screen 
                entrMgs.text = ''
                entrMls.text = ''
                txtAnswerSupp.text = '' 
            def backSpace(instance):
                if entrMgs.focus == True:  #partially working, need to figure out how to get focus on textinput
                    previousNumber = entrMgs.text
                    previousNumber = previousNumber[:-1]#subtracting or slicing the string by -1 
                    entrMgs.text = previousNumber #showing the updated previous number 
                if entrMls.focus == True: 
                    previousNumber = entrMls.text
                    previousNumber = previousNumber[:-1]
                    entrMls.text = previousNumber #showing the updated previous number 
              
            buttonsNums = [7,8,9,4,5,6,1,2,3,0] #creating an empty list for the buttons 
            
            y = 0.35 #setting the initial value for y 
            x = 0.2 # setting the initial value for x 
            i=1 #creating a counter for i to newline after every 3rd button 
            #creating a for loop to create the buttons 
            for num in buttonsNums:
                btnCalc = Button(text=str(num),size_hint=(0.2,0.1), pos_hint={'x':x, 'y':y},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
                btnCalc.bind(on_press=buttonText)#binding the button to then set to its text
                layoutHome.add_widget(btnCalc) 
                x+=0.19
                
                if i%3 == 0:#if 1 divided by 3 has 0 remainder new row
                    y-=0.10
                    x=0.2 
                i+=1
                
            btnDecimal = Button(text=".",size_hint=(0.39,0.1), pos_hint={'x':0.39, 'y':0.05},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
            btnDecimal.bind(on_release=buttonText)
            layoutHome.add_widget(btnDecimal)
                
            btnBackspace = Button(text="<--",size_hint=(0.2,0.1), pos_hint={'x':0.2, 'y':0.45},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
            btnBackspace.bind(on_release=backSpace)
            layoutHome.add_widget(btnBackspace) #THIS BUTTON CURRENT STILL NEEDS WORK 
                
            btnClearAll = Button(text="Clear All",size_hint=(0.39,0.1), pos_hint={'x':0.39, 'y':0.45},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),
                                 background_down=('black'))#background_down to change on press background color 
            btnClearAll.bind(on_release=clearAll)
            layoutHome.add_widget(btnClearAll)
 
            btnReturnHome = Button(text="Return to Home",size_hint=(0.35,0.1), pos_hint={'x':0.18, 'y':0.59},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
            
            btnCalculate = Button(text="Calculate",size_hint=(0.3,0.1), pos_hint={'x':0.53, 'y':0.59},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
            btnCalculate.bind(on_press=supplyCalc)
            layoutHome.add_widget(btnCalculate)  
        
        #---------------------------------- 
        #End Supply Fx  
        #----------------------------------
        def IvPush(self):
            
            clearScreen()
            lblIvPush = Label(text="IV Push Problem", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblIvPush)
            
            lblDoseMg = Label(text="Enter Dose (Mg): ", size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.8},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblDoseMg) 
            entrMG = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.82}, multiline=False, cursor_color=(0,0,0,1))
            layoutHome.add_widget(entrMG)
            
            lblSuppml = Label(text="Supply per \n1mL(Mg/1mL): ", size_hint=(0.3,0.1), pos_hint={'x':0.13, 'y':0.74},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblSuppml)
            entrML = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.76}, multiline=False, cursor_color=(0,0,0,1))
            layoutHome.add_widget(entrML)
            
            lblMlstoDraw = Label(text="mLs to Draw: ", size_hint=(0.3,0.1), pos_hint={'x':0.13, 'y':0.68},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblMlstoDraw) 
            entrAnswer = TextInput(size_hint=(0.3,0.058), pos_hint={'x':0.48, 'y':0.7}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.91,0.91,0.031,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=20)#setbackground disabled to white first to avoid grey tint
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
                    
            def clearAll(self): #clearing all the text off the screen 
                entrMG.text = ''
                entrML.text = ''
                entrAnswer.text = ''     
                    
            btnClearAll = Button(text="Clear All",size_hint=(0.65,0.1), pos_hint={'x':0.18, 'y':0.49},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),
                                 background_down=('black'))#background_down to change on press background color 
            btnClearAll.bind(on_release=clearAll)
            layoutHome.add_widget(btnClearAll)               
            
            btnReturnHome = Button(text="Return to Home",size_hint=(0.35,0.1), pos_hint={'x':0.18, 'y':0.59},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
            
            btnCalculate = Button(text="Calculate",size_hint=(0.3,0.1), pos_hint={'x':0.53, 'y':0.59},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
            btnCalculate.bind(on_press=ivpCalc)
            layoutHome.add_widget(btnCalculate)

        def IvDrip(self):
            
            clearScreen()
            lblIvDrip = Label(text="Iv Drip Problem", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblIvDrip)
            
            lblMgTotal = Label(text="Total Amt to \nGive(Mg/min): ", size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.8},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblMgTotal)
            entrMgTotal = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.82}, multiline=False, cursor_color=(0,0,0,1))
            layoutHome.add_widget(entrMgTotal)
            
            lblDropset = Label(text="Enter Dropset: ", size_hint=(0.3,0.1), pos_hint={'x':0.13, 'y':0.74},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblDropset)
            entrDropset = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.76}, multiline=False, cursor_color=(0,0,0,1))
            layoutHome.add_widget(entrDropset)
            
            lblConcml = Label(text="Concentration\n(Mg/1mL): ", size_hint=(0.3,0.1), pos_hint={'x':0.13, 'y':0.68},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblConcml)
            entrConc = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.7}, multiline=False, cursor_color=(0,0,0,1))
            layoutHome.add_widget(entrConc)
            
            lblDripRate = Label(text="Drops per Minute\n(gtts/min): ", size_hint=(0.3,0.1), pos_hint={'x':0.13, 'y':0.62},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblDripRate)
            entrDripRate = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.64}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.91,0.91,0.031,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=20)#setbackground disabled to white first to avoid grey tint
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
                    
            def clearAll(self): #clearing all the text off the screen 
                entrMgTotal.text = ''
                entrDropset.text = ''
                entrConc.text = ''
                entrDripRate.text = ''  
                          
            btnClearAll = Button(text="Clear All",size_hint=(0.65,0.1), pos_hint={'x':0.18, 'y':0.4},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),
                                 background_down=('black'))#background_down to change on press background color 
            btnClearAll.bind(on_release=clearAll)
            layoutHome.add_widget(btnClearAll)
                
            btnReturnHome = Button(text="Return to Home",size_hint=(0.35,0.1), pos_hint={'x':0.18, 'y':0.5},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
            
            btnCalculate = Button(text="Calculate",size_hint=(0.3,0.1), pos_hint={'x':0.53, 'y':0.5},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
            btnCalculate.bind(on_press=ivDripCalc)
            layoutHome.add_widget(btnCalculate)
            
        def Dopamine(self):
            
            clearScreen() 
            lblDopamine = Label(text="Dopamine Problem", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblDopamine)
            
            lblMcgDose = Label(text="Dose (mcg/min): ", size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.8},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblMcgDose)
            entrMcgDose = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.82}, multiline=False, cursor_color=(0,0,0,1))
            layoutHome.add_widget(entrMcgDose)
            
            lblKgwt = Label(text="Weight in Kg: ", size_hint=(0.3,0.1), pos_hint={'x':0.2, 'y':0.74},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblKgwt)
            entrKgwt = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.76}, multiline=False, cursor_color=(0,0,0,1))
            layoutHome.add_widget(entrKgwt)
            
            lblDropset = Label(text="Dropset: ", size_hint=(0.3,0.1), pos_hint={'x':0.22, 'y':0.68},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblDropset)
            entrDropset = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.7}, multiline=False, disabled=True)
            entrDropset.text = str(60)#adding the 60 dropset in for user to see 
            layoutHome.add_widget(entrDropset)
            
            lblConcMcg = Label(text="Concentration \n      (mcg/mL): ", size_hint=(0.3,0.1), pos_hint={'x':0.18, 'y':0.62},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblConcMcg)
            entrConcMcg = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.64}, multiline=False, cursor_color=(0,0,0,1))
            layoutHome.add_widget(entrConcMcg)
            
            lblDopaAns = Label(text="Drops per Minute \n          (gtts/min): ", size_hint=(0.3,0.1), pos_hint={'x':0.15,'y':0.56},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblDopaAns)
            entrDopaAns = TextInput(size_hint=(0.3,0.058), pos_hint={'x':0.48, 'y':0.58}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.91,0.91,0.031,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=20)#setbackground disabled to white first to avoid grey tint
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
                    
            def clearAll(self): #clearing all the text off the screen 
                entrMcgDose.text = ''
                entrConcMcg.text = ''
                entrKgwt.text = ''
                entrDopaAns.text = ''  
                    
            btnClearAll = Button(text="Clear All",size_hint=(0.65,0.1), pos_hint={'x':0.18, 'y':0.34},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),
                                 background_down=('black'))#background_down to change on press background color 
            btnClearAll.bind(on_release=clearAll)
            layoutHome.add_widget(btnClearAll)
                
            btnReturnHome = Button(text="Return to Home",size_hint=(0.35,0.1), pos_hint={'x':0.18, 'y':0.44},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
            
            btnCalculate = Button(text="Calculate",size_hint=(0.3,0.1), pos_hint={'x':0.53, 'y':0.44},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
            btnCalculate.bind(on_press=DopamineCalc)
            layoutHome.add_widget(btnCalculate)

        def Conversion(self):
            
            clearScreen()
            lblConversion = Label(text="Conversions", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblConversion)
            
            lblNumberOne = Label(text="Enter Unit Amt ", size_hint=(0.3,0.1), pos_hint={'x':0.08, 'y':0.8},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblNumberOne)
            entrNumberOne = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.38, 'y':0.82}, multiline=False, cursor_color=(0,0,0,1))
            layoutHome.add_widget(entrNumberOne)
            
            #creating the dropdown list for number1  
            numOneDrop = DropDown()
            numOneUnits = ["mg",'g','mcg', 'ibs', 'kg']
          
            #looping through the units           
            for i in numOneUnits:
                btnNumOneUnits = Button(text= i,size_hint_y=None, height=44,color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))#creating the buttons with parameters, can also for '%r' for text
                btnNumOneUnits.bind(on_release=lambda btnNumOneUnits: numOneDrop.select(btnNumOneUnits.text))#binding the button to then set to its text 
                numOneDrop.add_widget(btnNumOneUnits)#adding the buttons the the screen
 
            lblConvertTo = Label(text="Convert to", size_hint=(0.3,0.1), pos_hint={'x':0.08, 'y':0.74},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblConvertTo)
            
            #creating the dropdown list for convert to
            unitsDrop = DropDown()
            unitsList = ["mg",'g','mcg', 'ibs', 'kg']
            
            #looping through the units           
            for i in unitsList:
                btnUnits = Button(text=i,size_hint_y=None, height=44,color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))#creating the buttons with parameters
                btnUnits.bind(on_release=lambda btnUnits: unitsDrop.select(btnUnits.text))#binding the button to then set to its text 
                unitsDrop.add_widget(btnUnits)#adding the buttons the the screen 
                
            #creating the main button for Convert to
            btnSelect = Button(text='Select Units',size_hint=(0.3,0.08), pos_hint={'x':0.38, 'y':0.75},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
            btnSelect.bind(on_release=unitsDrop.open)
            layoutHome.add_widget(btnSelect)
            unitsDrop.bind(on_select=lambda instance, x: setattr(btnSelect, 'text',x))
            
            #creating the main button for Num1 Convert units 
            btnSelectOne = Button(text='Select Units',size_hint=(0.3,0.07), pos_hint={'x':0.68, 'y':0.81},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
            btnSelectOne.bind(on_release=numOneDrop.open)
            layoutHome.add_widget(btnSelectOne)
            numOneDrop.bind(on_select=lambda instance, x: setattr(btnSelectOne, 'text',x))
            
            lblConvertAns = Label(text="Answer", size_hint=(0.3,0.1), pos_hint={'x':0.08,'y':0.68},color=(.9,.9,.9,1))#answer for the conversion output and label 
            layoutHome.add_widget(lblConvertAns)
            entrConvertAns = TextInput(size_hint=(0.3,0.058), pos_hint={'x':0.38, 'y':0.7}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.91,0.91,0.031,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=20)#setbackground disabled to white first to avoid grey tint
            layoutHome.add_widget(entrConvertAns)
            #------------------------------------------------------------
            #adding buttons to return to homescreen and calculate problem 
            def returnHome(self):
                clearScreen()
                createHomePage(self)
            def conversionCalc(self):  
                try:
                    unitOne = float(entrNumberOne.text)
                    
                    #error checking for ibs and kilograms
                    if btnSelectOne.text == "ibs" or btnSelectOne == "kg" and btnSelect.text != "ibs" or btnSelect.text != "kg":
                        answer = "ERROR CHK UNITS"
                        entrConvertAns.text = str(answer)
                    if btnSelectOne.text != "ibs" or btnSelectOne != "kg" and btnSelect.text == "ibs" or btnSelect.text == "kg":
                        answer = "ERROR CHK UNITS"
                        entrConvertAns.text = str(answer)
                    #start calculations 
                    if btnSelectOne.text == "mcg" and btnSelect.text == "mg": #converts micrograms to milligrams 
                        mcgsTomgs = round(unitOne*0.001,5)
                        entrConvertAns.text = str(mcgsTomgs)
                    if btnSelectOne.text == "mcg" and btnSelect.text == "g": #converts micrograms to grams
                        mcgsTogs = round(unitOne/1000000,5)
                        
                        entrConvertAns.text=str(mcgsTogs)
                    if btnSelectOne.text == "mg" and btnSelect.text == "mcg": #converts milligrams to micrograms 
                        mgsTomcgs = round(unitOne*1000,5)
                        entrConvertAns.text = str(mgsTomcgs)
                    if btnSelectOne.text == "mg" and btnSelect.text == "g": #converts milligrams to grams
                        mgsTogs = round(unitOne/1000,5)
                        entrConvertAns.text=str(mgsTogs)
                    
                    if btnSelectOne.text == "g" and btnSelect.text == "mcg": #converts grams to micrograms 
                        gsTomcgs = round(unitOne*1000000,5) 
                        entrConvertAns.text = str(gsTomcgs)
                    if btnSelectOne.text == "g" and btnSelect.text == "mg": #converts grams to milligrams
                        gsTomg = round(unitOne*1000,5)
                        entrConvertAns.text=str(gsTomg)
                
                    if btnSelectOne.text == "ibs" and btnSelect.text == "kg": #convert pounds to kilograms 
                        ibsTokg = round(unitOne/2.2046226218,5)
                        entrConvertAns.text = str(ibsTokg)
                    if btnSelectOne.text == "kg" and btnSelect.text == "ibs": #convert kilograms to pounds 
                        kgToibs = round(unitOne*2.2046,5)
                        entrConvertAns.text = str(kgToibs)
                    
                    if btnSelectOne.text == "ibs" and btnSelect.text == "ibs": #pounds to pounds
                        entrConvertAns.text = str(unitOne)
                    if btnSelectOne.text == "kg" and btnSelect.text == "kg": #kilograms to Kilograms 
                        entrConvertAns.text = str(unitOne)
                except: 
                    answer = "ERROR"
                    entrConvertAns.text = str(answer) 
                    
            def clearAll(self): #clearing all the text off the screen 
                entrNumberOne.text = ''
                entrConvertAns.text = ''
                    
            btnClearAll = Button(text="Clear All",size_hint=(0.65,0.1), pos_hint={'x':0.18, 'y':0.48},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),
                                 background_down=('black'))#background_down to change on press background color 
            btnClearAll.bind(on_release=clearAll)
            layoutHome.add_widget(btnClearAll)

            btnCalculate = Button(text="Convert",size_hint=(0.3,0.1), pos_hint={'x':0.53, 'y':0.58},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
            btnCalculate.bind(on_press=conversionCalc)
            layoutHome.add_widget(btnCalculate)
                
            btnReturnHome = Button(text="Return to Home",size_hint=(0.35,0.1), pos_hint={'x':0.18, 'y':0.58},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
         
        def Settings(self):
            
            clearScreen()
            lblSettings = Label(text="Settings", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblSettings)
            
            lblDayMode = Label(text="Day Mode:", size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.8},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblDayMode)
            chkDayMode = CheckBox(group=1, size_hint=(0.3,0.1), pos_hint={'x':0.3, 'y':0.8})
            layoutHome.add_widget(chkDayMode)
                  
            lblNightMode = Label(text="Night Mode:", size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.74},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblNightMode)
            chkNightMode = CheckBox(group=1, size_hint=(0.3,0.1), pos_hint={'x':0.3, 'y':0.74})#setting active to true for night mode so app does not switch modes 
            layoutHome.add_widget(chkNightMode)
            
            lblBig = Label(text="Big Mode:", size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.68},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblBig)
            chkBig = CheckBox(group=1, size_hint=(0.3,0.1), pos_hint={'x':0.3, 'y':0.68})#group groups the checkboxes together to make them radio buttons 
            layoutHome.add_widget(chkBig)
               
            def switchModes(self):
                if chkNightMode.active == True:#stay same
                    pass
                if chkDayMode.active == True:#activate day mode    
                    clearScreen()#clears the screen
                    medCalc().stop() #stops Night Mode
                    if __name__ == "__main__": #runs day mode 
                        medCalcDayApp().run()
                if chkBig.active == True: #activate big mode 
                    clearScreen()#clears the screen
                    medCalc().stop() #stops Night Mode
                    if __name__ == "__main__": #runs day mode 
                        medCalcBigApp().run()

            #adding buttons to return to homescreen and calculate problem 
            def returnHome(self):
                clearScreen()
                createHomePage(self)
                
            btnReturnHome = Button(text="Return to Home",size_hint=(0.35,0.1), pos_hint={'x':0.18, 'y':0.44},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
            
            btnCalculate = Button(text="Switch Modes",size_hint=(0.3,0.1), pos_hint={'x':0.53, 'y':0.44},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
            btnCalculate.bind(on_press=switchModes)
            layoutHome.add_widget(btnCalculate)
            #grouping check boxes for selection buttons to get effect of a radio button 
            
        def ivInfusion(self):
            
            clearScreen()
            lblInfusion = Label(text="Infusion/Fluid Problem", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblInfusion)
            
            lblVol = Label(text="Volume to be \ninfused in (mL)", size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.8},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblVol)
            entrVol = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.82}, multiline=False, cursor_color=(0,0,0,1))
            layoutHome.add_widget(entrVol)
            
            lblDropFact = Label(text="Dropset: ", size_hint=(0.3,0.1), pos_hint={'x':0.2, 'y':0.74},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblDropFact)
            entrDropFact = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.76}, multiline=False, cursor_color=(0,0,0,1))
            layoutHome.add_widget(entrDropFact)
            
            lblDuration = Label(text="Duration in Minutes ", size_hint=(0.3,0.1), pos_hint={'x':0.13, 'y':0.68},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblDuration)
            entrDuration = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.7}, multiline=False, cursor_color=(0,0,0,1))
            layoutHome.add_widget(entrDuration)
            
            lblInfans = Label(text="gtts/min: ", size_hint=(0.3,0.1), pos_hint={'x':0.2, 'y':0.62},color=(.9,.9,.9,1))
            layoutHome.add_widget(lblInfans)
            entrInfans = TextInput(size_hint=(0.3,0.058), pos_hint={'x':0.48, 'y':0.64}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.91,0.91,0.031,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=20)#setbackground disabled to white first to avoid grey tint
            layoutHome.add_widget(entrInfans)
            
            #adding buttons to return to homescreen and calculate problem 
            def returnHome(self):
                clearScreen()
                createHomePage(self)
                
            def infusionCalc(self):
                try:
                    vol = float(entrVol.text)
                    drop = float(entrDropFact.text)
                    dur = float(entrDuration.text)
                    gtt = round(vol*drop/dur,5)#finding the drops per minute 
                    entrInfans.text = str(gtt)
                except:
                    answer = "ERROR"
                    entrInfans.text = str(answer)
                    
            def clearAll(self): #clearing all the text off the screen 
                entrVol.text = ''
                entrDropFact.text = ''
                entrDuration.text = '' 
                entrInfans.text = ''
                    
            btnClearAll = Button(text="Clear All",size_hint=(0.65,0.1), pos_hint={'x':0.18, 'y':0.4},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),
                                 background_down=('black'))#background_down to change on press background color 
            btnClearAll.bind(on_release=clearAll)
            layoutHome.add_widget(btnClearAll)
                    
            btnReturnHome = Button(text="Return to Home",size_hint=(0.35,0.1), pos_hint={'x':0.18, 'y':0.5},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
            
            btnCalculate = Button(text="Calculate",size_hint=(0.3,0.1), pos_hint={'x':0.53, 'y':0.5},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
            btnCalculate.bind(on_press=infusionCalc)
            layoutHome.add_widget(btnCalculate)
            
        def formulasPage(self):
            
            clearScreen()
            lblFormulas = Label(text="Formulas", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9})
            layoutHome.add_widget(lblFormulas)
            
            lblSupply = Label(text="Supply:\n mg / ml= mg per 1mL\n"+
                              "-------------------------------------", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.8})
            layoutHome.add_widget(lblSupply)
            
            lblIvPush = Label(text="Iv Push:\n dose / supply per 1mL = mLs to Draw\n"+
                              "-------------------------------------", size_hint=(0.3,0.1), pos_hint={'x':0.25, 'y':0.7})
            layoutHome.add_widget(lblIvPush)
            
            lblIvDrip = Label(text="Iv Drip:\n (dose*gtts)/Concentration per 1mL = gtts/min\n"+
                              "-------------------------------------", size_hint=(0.3,0.1), pos_hint={'x':0.33, 'y':0.6})
            layoutHome.add_widget(lblIvDrip)
            
            lblDopa = Label(text="Dopamine:\n Dose(mcg)*kg*dropset) / Concen = gtts/min\n"+
                              "-------------------------------------", size_hint=(0.3,0.1), pos_hint={'x':0.32, 'y':0.5})
            layoutHome.add_widget(lblDopa)
            
            lblInf = Label(text="Infusion/Fluid:\n(Volume*DropFactor)/ Minutes = gtts/min\n"+
                              "-------------------------------------", size_hint=(0.3,0.1), pos_hint={'x':0.30, 'y':0.4})
            layoutHome.add_widget(lblInf)
            lblInf2 = Label(text="ml/hr to gtts/min\n(Volume*DropFactor)/ Minutes = gtts/min\n"+
                              "-------------------------------------", size_hint=(0.3,0.1), pos_hint={'x':0.30, 'y':0.3})
            layoutHome.add_widget(lblInf2)
            
            def o2Tank(self):
                
                clearScreen()
                lblO2 = Label(text="O2 Tank Remaining Calculation", size_hint=(0.3,0.1), pos_hint={'x':0.2, 'y':0.9},color=(.9,.9,.9,1))
                layoutHome.add_widget(lblO2)
                
                lblCyl = Label(text="Cylinder Factor", size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.8},color=(.9,.9,.9,1))
                layoutHome.add_widget(lblCyl)
                
                lblCurrpsi = Label(text="Current PSI in Tank", size_hint=(0.3,0.1), pos_hint={'x':0.14, 'y':0.74},color=(.9,.9,.9,1))
                layoutHome.add_widget(lblCurrpsi)
                entrCurrpsi = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.76}, multiline=False, cursor_color=(0,0,0,1))
                layoutHome.add_widget(entrCurrpsi)
            
                lbl02LPM = Label(text="liters per Minute(LPM) ", size_hint=(0.3,0.1), pos_hint={'x':0.10, 'y':0.68},color=(.9,.9,.9,1))
                layoutHome.add_widget(lbl02LPM)
                entr02LPM = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.7}, multiline=False, cursor_color=(0,0,0,1))
                layoutHome.add_widget(entr02LPM)
     
                lbl02ans = Label(text="Minutes remaining ", size_hint=(0.3,0.1), pos_hint={'x':0.13, 'y':0.62},color=(.9,.9,.9,1))
                layoutHome.add_widget(lbl02ans)
                entr02ans = TextInput(size_hint=(0.3,0.058), pos_hint={'x':0.48, 'y':0.64}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.91,0.91,0.031,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=20)#setbackground disabled to white first to avoid grey tint
                layoutHome.add_widget(entr02ans)
                
                lblres = Label(text="*Calculated with Safe residual\n pressure of 200PSI ", size_hint=(0.3,0.1), pos_hint={'x':0.3, 'y':0.55},color=(.9,.9,.9,1))
                layoutHome.add_widget(lblres)
                
                #creating the dropdown list for convert to
                unitsDrop02 = DropDown()
                unitsList02 = ["D Cylinder",'Jumbo D','E Cylinder', 'M Cylinder', 'H Cylinder']
            
                #looping through the units           
                for i in unitsList02:
                    btnUnits02 = Button(text=i,size_hint_y=None, height=44,color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))#creating the buttons with parameters
                    btnUnits02.bind(on_release=lambda btnUnits02: unitsDrop02.select(btnUnits02.text))#binding the button to then set to its text 
                    unitsDrop02.add_widget(btnUnits02)#adding the buttons the the screen 
                    
                #creating the main button for 02 cylinder 
                btnSelect = Button(text='Tank Type',size_hint=(0.3,0.09), pos_hint={'x':0.48, 'y':0.82},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
                btnSelect.bind(on_release=unitsDrop02.open)
                layoutHome.add_widget(btnSelect)
                unitsDrop02.bind(on_select=lambda instance, x: setattr(btnSelect, 'text',x))
                def o2Calc(self):
                    try:
                        lpm = float(entr02LPM.text)
                        psi = float(entrCurrpsi.text)
                            
                        dCylfact = 0.16 #D cylinder factor
                        jumboDnECylfact = 0.28 #jumboD and E cylinder factor
                        mCylfact = 1.56 #M cylinder factor
                        hCylfact = 3.14 #H cylinder factor 
                        saferes = 200 #safe residual pressure 
                        
                        if btnSelect.text == "Tank Type":
                            answer = "ERR CHK TANK"
                            entr02ans.text = str(answer)
                        if btnSelect.text == "Jumbo D" or btnSelect.text == "E Cylinder":
                            oxygenLeftTime = round(((psi-saferes)*jumboDnECylfact)/lpm,5)
                            entr02ans.text = str(oxygenLeftTime) 
                        if btnSelect.text == "D Cylinder":
                            oxygenTimeleft = round(((psi-saferes)*dCylfact)/lpm,5)
                            entr02ans.text = str(oxygenTimeleft)  
                        if btnSelect.text == "M Cylinder":
                            o2Time = round(((psi-saferes)*mCylfact)/lpm,5)
                            entr02ans.text = str(o2Time)
                        if btnSelect.text == "H Cylinder":
                            o2Timeh = round(((psi-saferes)*hCylfact)/lpm,5)
                            entr02ans.text = str(o2Timeh)
                    except:
                        answer = "ERROR"
                        entr02ans.text = str(answer)
                        
                def clearAll(self): #clearing all the text off the screen 
                    entrCurrpsi.text = ''
                    entr02LPM.text = ''
                    entr02ans.text =''
                 
                def returnHome(self):
                    clearScreen()
                    createHomePage(self)
                    
                btnClearAll = Button(text="Clear All",size_hint=(0.65,0.1), pos_hint={'x':0.18, 'y':0.35},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),
                                 background_down=('black'))#background_down to change on press background color 
                btnClearAll.bind(on_release=clearAll)
                layoutHome.add_widget(btnClearAll)
                    
                btnReturnHome = Button(text="Return to Home",size_hint=(0.35,0.1), pos_hint={'x':0.18, 'y':0.45},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
                btnReturnHome.bind(on_press=returnHome)
                layoutHome.add_widget(btnReturnHome)
            
                btnCalculate = Button(text="Calculate",size_hint=(0.3,0.1), pos_hint={'x':0.53, 'y':0.45},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
                btnCalculate.bind(on_press=o2Calc)#binding the button to 02 calc function 
                layoutHome.add_widget(btnCalculate)
                
            def burnFormula(self):
                
                clearScreen()
                lblBurnFormula = Label(text="Parkland Formula", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9},color=(.9,.9,.9,1))
                layoutHome.add_widget(lblBurnFormula)
                
                lblml = Label(text="ML: ", size_hint=(0.3,0.1), pos_hint={'x':0.25, 'y':0.8},color=(.9,.9,.9,1))
                layoutHome.add_widget(lblml)
                entrml = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.82}, multiline=False, disabled=True)
                entrml.text = str(4)#setting the default value for 4 for the parkland burn formula
                layoutHome.add_widget(entrml)
            
                lblTBSA = Label(text="TBSA(%) ", size_hint=(0.3,0.1), pos_hint={'x':0.23, 'y':0.74},color=(.9,.9,.9,1))
                layoutHome.add_widget(lblTBSA)
                entrTBSA = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.76}, multiline=False, cursor_color=(0,0,0,1))
                layoutHome.add_widget(entrTBSA)
            
                lblkg = Label(text="KG: ", size_hint=(0.3,0.1), pos_hint={'x':0.25, 'y':0.68},color=(.9,.9,.9,1))
                layoutHome.add_widget(lblkg)
                entrkg = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.7}, multiline=False, cursor_color=(0,0,0,1))
                layoutHome.add_widget(entrkg)
                
                lblDropFactor = Label(text="Drop Factor:", size_hint=(0.25,0.1), pos_hint={'x':0.22, 'y':0.62},color=(.9,.9,.9,1))
                layoutHome.add_widget(lblDropFactor)
                entrDropFact = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.64}, multiline=False, cursor_color=(0,0,0,1))
                layoutHome.add_widget(entrDropFact)
                
                lblburnAns = Label(text="(FIRST 8 HRS) gtts/min ", size_hint=(0.25,0.1), pos_hint={'x':0.13, 'y':0.56},color=(.9,.9,.9,1))
                layoutHome.add_widget(lblburnAns)
                entrburnAns = TextInput(size_hint=(0.3,0.058), pos_hint={'x':0.48, 'y':0.58}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.91,0.91,0.031,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=20)#setbackground disabled to white first to avoid grey tint
                layoutHome.add_widget(entrburnAns)
                
                lblburnAns2 = Label(text="(NEXT 16 HRS) gtts/min ", size_hint=(0.25,0.1), pos_hint={'x':0.13, 'y':0.50},color=(.9,.9,.9,1))
                layoutHome.add_widget(lblburnAns2)
                entrburnAns2 = TextInput(size_hint=(0.3,0.058), pos_hint={'x':0.48, 'y':0.52}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.91,0.91,0.031,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=20)#setbackground disabled to white first to avoid grey tint
                layoutHome.add_widget(entrburnAns2)
                
                lblburnTotal = Label(text="Total mL ovr 24HRS ", size_hint=(0.25,0.1), pos_hint={'x':0.13, 'y':0.44},color=(.9,.9,.9,1))
                layoutHome.add_widget(lblburnTotal)
                entrburnTotal = TextInput(size_hint=(0.3,0.058), pos_hint={'x':0.48, 'y':0.46}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.91,0.91,0.031,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=20)#setbackground disabled to white first to avoid grey tint
                layoutHome.add_widget(entrburnTotal)
                
                #adding buttons to return to homescreen and calculate problem 
                def returnHome(self):
                    clearScreen()
                    createHomePage(self)
                def burnCalc(self):
                    try: 
                        burnml = 4.0
                        burnBSA= float(entrTBSA.text)
                        wt = float(entrkg.text)
                        fluidvol = burnml*burnBSA*wt
                        dropFactor = float(entrDropFact.text)
                         
                        first8 = (burnml*burnBSA*wt) #The first half of NS or LR is given over first 8 hours 
                        gttsFirst = round(first8*dropFactor/480,5)#480 is the amount of minutes in 8 hours for infusion problem 
                        entrburnAns.text = str(gttsFirst)
                        
                        gttsSecond = round(first8*dropFactor/960)#960 is the amount of minutes in 2nd 16 hours 
                        entrburnAns2.text = str(gttsSecond)
                         
                        total = burnml*burnBSA*wt
                        entrburnTotal.text = str(total)
                    except:
                        answer = "ERROR"
                        entrburnTotal.text = str(answer)
                        entrburnAns.text = str(answer)
                        entrburnAns2.text = str(answer)
                        
                def clearAll(self): #clearing all the text off the screen 
                    entrTBSA.text = '' 
                    entrkg.text = ''
                    entrburnAns.text = '' 
                    entrburnAns2.text = ''
                    entrburnTotal.text = '' 
                    entrDropFact.text = ''
                    
                        
                btnClearAll = Button(text="Clear All",size_hint=(0.65,0.1), pos_hint={'x':0.18, 'y':0.25},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),
                                 background_down=('black'))#background_down to change on press background color 
                btnClearAll.bind(on_release=clearAll)
                layoutHome.add_widget(btnClearAll)
                        
                btnCalculate = Button(text="Calculate",size_hint=(0.3,0.1), pos_hint={'x':0.53, 'y':0.35},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
                btnCalculate.bind(on_press=burnCalc)
                layoutHome.add_widget(btnCalculate)
                
                btnReturnHome = Button(text="Return to Home",size_hint=(0.35,0.1), pos_hint={'x':0.18, 'y':0.35},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
                btnReturnHome.bind(on_press=returnHome)
                layoutHome.add_widget(btnReturnHome)
                
            #-----------------END BURN FORMULA---------------------------------------------------------------
            #adding buttons to return to homescreen and calculate problem 
            def returnHome(self):
                clearScreen()
                createHomePage(self)
            
            btnReturnHome = Button(text="Return to Home",size_hint=(0.35,0.1), pos_hint={'x':0.07, 'y':0.1},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
            
            btnO2Tank = Button (text="O2 Time Calc", size_hint=(0.35,0.1),pos_hint={'x':0.07, 'y':0.2},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
            btnO2Tank.bind(on_press=o2Tank)
            layoutHome.add_widget(btnO2Tank)
            
            btnO2Tank = Button (text="Burn Formula", size_hint=(0.35,0.1),pos_hint={'x':0.42, 'y':0.2},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))
            btnO2Tank.bind(on_press=burnFormula)
            layoutHome.add_widget(btnO2Tank)
            #----------------------------END FORMULAS FUNCTION 
#-------------------------------END FUNCTIONS-------------------------------------------------------------
        #adding actions to the buttons for disclaimer 
        btnYes.bind(on_press=pressYes)
        btnNo.bind(on_press=pressNo)        
        self.add_widget(layoutHome)#adding the innerlayout to the root 
#----------------------END NIGHT MODE----------------------------------------------
#----------------------------------------------------------------------------------
#----------------------Begin Day Mode----------------------------------------------        
class medCalcDay(RelativeLayout):#the medcalc daymode class 
    def __init__(self,**kwargs):#creating the constructor 
        super(medCalcDay, self).__init__(**kwargs)
        
        layoutHome = RelativeLayout() #creating the innerlayout
        Window.clearcolor=(1,1,1,1) #setting window color to white 
        lblDisclaimer = (Label(text="This application is intended to check the \nprovides math. If any discrepancies\n" +
                            "arise refer to providers hand-written math, \nand re-check ALL calculations. \nDo you agree to these terms of serive?",pos_hint={'center_x':0.5, 'center_y':0.8},
                             color = (0,0,0,1)))#
        layoutHome.add_widget(lblDisclaimer)
        #creating and adding buttons to disclaimer Window
        btnYes = Button(text="Accept", size_hint=(0.5,0.2), pos_hint={'center_x':0.5, 'center_y':0.3},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))#Place button bottom center can also use {'center_x': 0, 'center_y':0} 
        layoutHome.add_widget(btnYes) #adding button to screen 
        btnNo = Button(text="Decline", size_hint=(0.5,0.2),pos_hint={'center_x':0.5, 'center_y':0.52},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1)) #place button on top of accept button 
        layoutHome.add_widget(btnNo)
        #-----Functions for Disclaimer-----
        def pressYes(self):
            layoutHome.clear_widgets()#clears all widgets from the frame 
            createHomePage(self)  
        def pressNo(self):
            medCalc().stop() #exiting the program 
        #-----Misc Functions---------------
        def clearScreen():
            layoutHome.clear_widgets()     
        #---------------------------------- 
        #Creating the Homepage 
        #----------------------------------         
        def createHomePage(self):
            Window.clearcolor=(0.99,0.99,0.99,1)# setting the background window color 
            lblHomePageTest = Label(text="Please Select Problem Type: ",size_hint=(0.3,0.1), pos_hint={'x':0.362, 'y':0.88},color=(0,0,0,1)) #color = how to change label text color 
            layoutHome.add_widget(lblHomePageTest)
            
            #adding buttons to problem types 
            btnSupply = Button(text="Supply per 1mL",size_hint=(0.4,0.1), pos_hint={'x':0.32, 'y':0.8},background_normal='',background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))#0.737,0.737,0.737,1
            btnSupply.bind(on_press=Supply)#binding the button to a function, RGBA decimals divide by 255 
            layoutHome.add_widget(btnSupply)
            
            btnIvp = Button(text="IV Push",size_hint=(0.4,0.1), pos_hint={'x':0.32, 'y':0.69},
                            background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
            btnIvp.bind(on_press=IvPush)
            layoutHome.add_widget(btnIvp)
            
            btnIvd = Button(text="IV Drip Problem",size_hint=(0.4,0.1), pos_hint={'x':0.32, 'y':0.58},
                            background_normal='',background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
            btnIvd.bind(on_press=IvDrip)
            layoutHome.add_widget(btnIvd)
            
            btnDopa = Button(text="Dopamine Problem",size_hint=(0.4,0.1), pos_hint={'x':0.32, 'y':0.47},
                             background_normal='',background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
            btnDopa.bind(on_press=Dopamine)
            layoutHome.add_widget(btnDopa)
            
            btnivInfusion = Button(text="Infusion Problem",size_hint=(0.4,0.1),pos_hint={'x':0.32,'y':0.36},
                                   background_normal='',background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
            btnivInfusion.bind(on_press=ivInfusion)
            layoutHome.add_widget(btnivInfusion)
            
            btnConvert = Button(text="Conversion",size_hint=(0.4,0.1), pos_hint={'x':0.32, 'y':0.25},
                                background_normal='',background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
            btnConvert.bind(on_press=Conversion)
            layoutHome.add_widget(btnConvert)
            
            btnFormulas = Button(text="Formulas/O2/Burn",size_hint=(0.4,0.1),pos_hint={'x':0.32,'y':0.14},
                                 background_normal='',background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
            btnFormulas.bind(on_press=formulasPage)
            layoutHome.add_widget(btnFormulas)
            
            btnSettings = Button(text="Settings",size_hint=(0.4,0.1),pos_hint={'x':0.32, 'y':0.03},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
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
            
            lblSupply = Label(text="Find supply per 1mL",size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9},color=(0,0,0,1))
            layoutHome.add_widget(lblSupply)
            
            #creating buttons for supply 
            lblMgs = Label(text="Enter milligrams\n                (MG): ",size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.8},color=(0,0,0,1))
            layoutHome.add_widget(lblMgs)
            entrMgs = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.82}, multiline=False, cursor_color=(0,0,0,1), unfocus_on_touch=False)
            layoutHome.add_widget(entrMgs)
            
            lblMls = Label(text="Enter milliliters\n                 (mL): ",size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.74},color=(0,0,0,1))
            layoutHome.add_widget(lblMls)
            entrMls = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.76}, multiline=False, cursor_color=(0,0,0,1), unfocus_on_touch=False)
            layoutHome.add_widget(entrMls)
            
            lblMgspMl = Label(text="      Milligrams \n         per 1 mL: ",size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.68},color=(0,0,0,1))
            layoutHome.add_widget(lblMgspMl)
            
            txtAnswerSupp = TextInput(size_hint=(0.3,0.058), pos_hint={'x':0.48, 'y':0.7}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.4,0.78,0.831,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=20)#setbackground disabled to white first to avoid grey tint 
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
                    txtAnswerSupp.text = str((answer))#converting the answer back to a string and placing into text input box 
                except:
                    answer = "ERROR" #if exception is thrown then give error for answer 
                    txtAnswerSupp.text = answer
            
            #creating the button number function,   
            def buttonText(instance): #creating an output to print the button text 
                if entrMgs.focus == True:  #partially working, need to figure out how to get focus on textinput
                    entrMgs.text += instance.text
                if entrMls.focus == True: 
                    entrMls.text += instance.text

            def clearAll(self): #clearing all the text off the screen 
                entrMgs.text = ''
                entrMls.text = ''
                txtAnswerSupp.text = '' 
            def backSpace(instance):
                if entrMgs.focus == True:  #partially working, need to figure out how to get focus on textinput
                    previousNumber = entrMgs.text
                    previousNumber = previousNumber[:-1]#subtracting or slicing the string by -1 
                    entrMgs.text = previousNumber #showing the updated previous number 
                if entrMls.focus == True: 
                    previousNumber = entrMls.text
                    previousNumber = previousNumber[:-1]
                    entrMls.text = previousNumber #showing the updated previous number 
              
            buttonsNums = [7,8,9,4,5,6,1,2,3,0] #creating an empty list for the buttons 
            
            y = 0.35 #setting the initial value for y 
            x = 0.2 # setting the initial value for x 
            i=1 #creating a counter for i to newline after every 3rd button 
            #creating a for loop to create the buttons 
            for num in buttonsNums:
                btnCalc = Button(text=str(num),size_hint=(0.2,0.1), pos_hint={'x':x, 'y':y},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1),border=(20,20,20,20))
                btnCalc.bind(on_press=buttonText)#binding the button to then set to its text
                layoutHome.add_widget(btnCalc) 
                x+=0.19
                
                if i%3 == 0:#if 1 divided by 3 has 0 remainder new row
                    y-=0.10
                    x=0.2 
                i+=1
                
            btnDecimal = Button(text=".",size_hint=(0.39,0.1), pos_hint={'x':0.39, 'y':0.05},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
            btnDecimal.bind(on_release=buttonText)
            layoutHome.add_widget(btnDecimal)
                
            btnBackspace = Button(text="<--",size_hint=(0.2,0.1), pos_hint={'x':0.2, 'y':0.45},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
            btnBackspace.bind(on_release=backSpace)
            layoutHome.add_widget(btnBackspace) #THIS BUTTON CURRENT STILL NEEDS WORK 
                
            btnClearAll = Button(text="Clear All",size_hint=(0.39,0.1), pos_hint={'x':0.39, 'y':0.45},color=(0,0,0,1),
                                 background_normal='', background_color=(0.737,0.737,0.737,1),
                                 background_down=('black'))#background_down to change on press background color 
            btnClearAll.bind(on_release=clearAll)
            layoutHome.add_widget(btnClearAll)
 
            btnReturnHome = Button(text="Return to Home",size_hint=(0.35,0.1), pos_hint={'x':0.18, 'y':0.59},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
            
            btnCalculate = Button(text="Calculate",size_hint=(0.3,0.1), pos_hint={'x':0.53, 'y':0.59},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
            btnCalculate.bind(on_press=supplyCalc)
            layoutHome.add_widget(btnCalculate)  
        
        #---------------------------------- 
        #End Supply Fx  
        #----------------------------------
        def IvPush(self):
            
            clearScreen()
            lblIvPush = Label(text="IV Push Problem", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9},color=(0,0,0,1))
            layoutHome.add_widget(lblIvPush)
            
            lblDoseMg = Label(text="Enter Dose (Mg): ", size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.8},color=(0,0,0,1))
            layoutHome.add_widget(lblDoseMg) 
            entrMG = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.82}, multiline=False, cursor_color=(0,0,0,1))
            layoutHome.add_widget(entrMG)
            
            lblSuppml = Label(text="Supply per \n1mL(Mg/1mL): ", size_hint=(0.3,0.1), pos_hint={'x':0.13, 'y':0.74},color=(0,0,0,1))
            layoutHome.add_widget(lblSuppml)
            entrML = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.76}, multiline=False, cursor_color=(0,0,0,1))
            layoutHome.add_widget(entrML)
            
            lblMlstoDraw = Label(text="mLs to Draw: ", size_hint=(0.3,0.1), pos_hint={'x':0.13, 'y':0.68},color=(0,0,0,1))
            layoutHome.add_widget(lblMlstoDraw) 
            entrAnswer = TextInput(size_hint=(0.3,0.058), pos_hint={'x':0.48, 'y':0.7}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.4,0.78,0.831,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=20)#setbackground disabled to white first to avoid grey tint
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
                    
            def clearAll(self): #clearing all the text off the screen 
                entrMG.text = ''
                entrML.text = ''
                entrAnswer.text = ''     
                    
            btnClearAll = Button(text="Clear All",size_hint=(0.65,0.1), pos_hint={'x':0.18, 'y':0.49},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1),
                                 background_down=('black'))#background_down to change on press background color 
            btnClearAll.bind(on_release=clearAll)
            layoutHome.add_widget(btnClearAll)               
            
            btnReturnHome = Button(text="Return to Home",size_hint=(0.35,0.1), pos_hint={'x':0.18, 'y':0.59},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
            
            btnCalculate = Button(text="Calculate",size_hint=(0.3,0.1), pos_hint={'x':0.53, 'y':0.59},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
            btnCalculate.bind(on_press=ivpCalc)
            layoutHome.add_widget(btnCalculate)

        def IvDrip(self):
            
            clearScreen()
            lblIvDrip = Label(text="Iv Drip Problem", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9},color=(0,0,0,1))
            layoutHome.add_widget(lblIvDrip)
            
            lblMgTotal = Label(text="Total Amt to \nGive(Mg/min): ", size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.8},color=(0,0,0,1))
            layoutHome.add_widget(lblMgTotal)
            entrMgTotal = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.82}, multiline=False, cursor_color=(0,0,0,1))
            layoutHome.add_widget(entrMgTotal)
            
            lblDropset = Label(text="Enter Dropset: ", size_hint=(0.3,0.1), pos_hint={'x':0.13, 'y':0.74},color=(0,0,0,1))
            layoutHome.add_widget(lblDropset)
            entrDropset = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.76}, multiline=False, cursor_color=(0,0,0,1))
            layoutHome.add_widget(entrDropset)
            
            lblConcml = Label(text="Concentration\n(Mg/1mL): ", size_hint=(0.3,0.1), pos_hint={'x':0.13, 'y':0.68},color=(0,0,0,1))
            layoutHome.add_widget(lblConcml)
            entrConc = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.7}, multiline=False, cursor_color=(0,0,0,1))
            layoutHome.add_widget(entrConc)
            
            lblDripRate = Label(text="Drops per Minute\n(gtts/min): ", size_hint=(0.3,0.1), pos_hint={'x':0.13, 'y':0.62},color=(0,0,0,1))
            layoutHome.add_widget(lblDripRate)
            entrDripRate = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.64}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.4,0.78,0.831,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=20)#setbackground disabled to white first to avoid grey tint
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
                    
            def clearAll(self): #clearing all the text off the screen 
                entrMgTotal.text = ''
                entrDropset.text = ''
                entrConc.text = ''
                entrDripRate.text = ''  
                          
            btnClearAll = Button(text="Clear All",size_hint=(0.65,0.1), pos_hint={'x':0.18, 'y':0.4},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1),
                                 background_down=('black'))#background_down to change on press background color 
            btnClearAll.bind(on_release=clearAll)
            layoutHome.add_widget(btnClearAll)
                
            btnReturnHome = Button(text="Return to Home",size_hint=(0.35,0.1), pos_hint={'x':0.18, 'y':0.5},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
            
            btnCalculate = Button(text="Calculate",size_hint=(0.3,0.1), pos_hint={'x':0.53, 'y':0.5},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
            btnCalculate.bind(on_press=ivDripCalc)
            layoutHome.add_widget(btnCalculate)
            
        def Dopamine(self):
            
            clearScreen() 
            lblDopamine = Label(text="Dopamine Problem", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9},color=(0,0,0,1))
            layoutHome.add_widget(lblDopamine)
            
            lblMcgDose = Label(text="Dose (mcg/min): ", size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.8},color=(0,0,0,1))
            layoutHome.add_widget(lblMcgDose)
            entrMcgDose = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.82}, multiline=False, cursor_color=(0,0,0,1))
            layoutHome.add_widget(entrMcgDose)
            
            lblKgwt = Label(text="Weight in Kg: ", size_hint=(0.3,0.1), pos_hint={'x':0.2, 'y':0.74},color=(0,0,0,1))
            layoutHome.add_widget(lblKgwt)
            entrKgwt = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.76}, multiline=False, cursor_color=(0,0,0,1))
            layoutHome.add_widget(entrKgwt)
            
            lblDropset = Label(text="Dropset: ", size_hint=(0.3,0.1), pos_hint={'x':0.22, 'y':0.68},color=(0,0,0,1))
            layoutHome.add_widget(lblDropset)
            entrDropset = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.7}, multiline=False, disabled=True)
            entrDropset.text = str(60)#adding the 60 dropset in for user to see 
            layoutHome.add_widget(entrDropset)
            
            lblConcMcg = Label(text="Concentration \n      (mcg/mL): ", size_hint=(0.3,0.1), pos_hint={'x':0.18, 'y':0.62},color=(0,0,0,1))
            layoutHome.add_widget(lblConcMcg)
            entrConcMcg = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.64}, multiline=False, cursor_color=(0,0,0,1))
            layoutHome.add_widget(entrConcMcg)
            
            lblDopaAns = Label(text="Drops per Minute \n          (gtts/min): ", size_hint=(0.3,0.1), pos_hint={'x':0.15,'y':0.56},color=(0,0,0,1))
            layoutHome.add_widget(lblDopaAns)
            entrDopaAns = TextInput(size_hint=(0.3,0.058), pos_hint={'x':0.48, 'y':0.58}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.4,0.78,0.831,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=20)#setbackground disabled to white first to avoid grey tint
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
                    
            def clearAll(self): #clearing all the text off the screen 
                entrMcgDose.text = ''
                entrConcMcg.text = ''
                entrKgwt.text = ''
                entrDopaAns.text = ''  
                    
            btnClearAll = Button(text="Clear All",size_hint=(0.65,0.1), pos_hint={'x':0.18, 'y':0.34},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1),
                                 background_down=('black'))#background_down to change on press background color 
            btnClearAll.bind(on_release=clearAll)
            layoutHome.add_widget(btnClearAll)
                
            btnReturnHome = Button(text="Return to Home",size_hint=(0.35,0.1), pos_hint={'x':0.18, 'y':0.44},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
            
            btnCalculate = Button(text="Calculate",size_hint=(0.3,0.1), pos_hint={'x':0.53, 'y':0.44},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
            btnCalculate.bind(on_press=DopamineCalc)
            layoutHome.add_widget(btnCalculate)

        def Conversion(self):
            
            clearScreen()
            lblConversion = Label(text="Conversions", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9},color=(0,0,0,1))
            layoutHome.add_widget(lblConversion)
            
            lblNumberOne = Label(text="Enter Unit Amt ", size_hint=(0.3,0.1), pos_hint={'x':0.08, 'y':0.8},color=(0,0,0,1))
            layoutHome.add_widget(lblNumberOne)
            entrNumberOne = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.38, 'y':0.82}, multiline=False, cursor_color=(0,0,0,1))
            layoutHome.add_widget(entrNumberOne)
            
            #creating the dropdown list for number1  
            numOneDrop = DropDown()
            numOneUnits = ["mg",'g','mcg', 'ibs', 'kg']
          
            #looping through the units           
            for i in numOneUnits:
                btnNumOneUnits = Button(text= i,size_hint_y=None, height=44,
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))#creating the buttons with parameters, can also for '%r' for text
                btnNumOneUnits.bind(on_release=lambda btnNumOneUnits: numOneDrop.select(btnNumOneUnits.text))#binding the button to then set to its text 
                numOneDrop.add_widget(btnNumOneUnits)#adding the buttons the the screen
 
            lblConvertTo = Label(text="Convert to", size_hint=(0.3,0.1), pos_hint={'x':0.08, 'y':0.74},color=(0,0,0,1))
            layoutHome.add_widget(lblConvertTo)
            
            #creating the dropdown list for convert to
            unitsDrop = DropDown()
            unitsList = ["mg",'g','mcg', 'ibs', 'kg']
            
            #looping through the units           
            for i in unitsList:
                btnUnits = Button(text=i,size_hint_y=None, height=44,
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))#creating the buttons with parameters
                btnUnits.bind(on_release=lambda btnUnits: unitsDrop.select(btnUnits.text))#binding the button to then set to its text 
                unitsDrop.add_widget(btnUnits)#adding the buttons the the screen 
                
            #creating the main button for Convert to
            btnSelect = Button(text='Select Units',size_hint=(0.3,0.08), pos_hint={'x':0.38, 'y':0.75},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
            btnSelect.bind(on_release=unitsDrop.open)
            layoutHome.add_widget(btnSelect)
            unitsDrop.bind(on_select=lambda instance, x: setattr(btnSelect, 'text',x))
            
            #creating the main button for Num1 Convert units 
            btnSelectOne = Button(text='Select Units',size_hint=(0.3,0.07), pos_hint={'x':0.68, 'y':0.81},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
            btnSelectOne.bind(on_release=numOneDrop.open)
            layoutHome.add_widget(btnSelectOne)
            numOneDrop.bind(on_select=lambda instance, x: setattr(btnSelectOne, 'text',x))
            
            lblConvertAns = Label(text="Answer", size_hint=(0.3,0.1), pos_hint={'x':0.08,'y':0.68},color=(0,0,0,1))#answer for the conversion output and label 
            layoutHome.add_widget(lblConvertAns)
            entrConvertAns = TextInput(size_hint=(0.3,0.058), pos_hint={'x':0.38, 'y':0.7}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.4,0.78,0.831,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=20)#setbackground disabled to white first to avoid grey tint
            layoutHome.add_widget(entrConvertAns)
            #------------------------------------------------------------
            #adding buttons to return to homescreen and calculate problem 
            def returnHome(self):
                clearScreen()
                createHomePage(self)
            def conversionCalc(self):  
                try:
                    unitOne = float(entrNumberOne.text)
                    
                    #error checking for ibs and kilograms
                    if btnSelectOne.text == "ibs" or btnSelectOne == "kg" and btnSelect.text != "ibs" or btnSelect.text != "kg":
                        answer = "ERROR CHK UNITS"
                        entrConvertAns.text = str(answer)
                    if btnSelectOne.text != "ibs" or btnSelectOne != "kg" and btnSelect.text == "ibs" or btnSelect.text == "kg":
                        answer = "ERROR CHK UNITS"
                        entrConvertAns.text = str(answer)
                    #start calculations 
                    if btnSelectOne.text == "mcg" and btnSelect.text == "mg": #converts micrograms to milligrams 
                        mcgsTomgs = round(unitOne*0.001,5)
                        entrConvertAns.text = str(mcgsTomgs)
                    if btnSelectOne.text == "mcg" and btnSelect.text == "g": #converts micrograms to grams
                        mcgsTogs = round(unitOne/1000000,5)
                        
                        entrConvertAns.text=str(mcgsTogs)
                    if btnSelectOne.text == "mg" and btnSelect.text == "mcg": #converts milligrams to micrograms 
                        mgsTomcgs = round(unitOne*1000,5)
                        entrConvertAns.text = str(mgsTomcgs)
                    if btnSelectOne.text == "mg" and btnSelect.text == "g": #converts milligrams to grams
                        mgsTogs = round(unitOne/1000,5)
                        entrConvertAns.text=str(mgsTogs)
                    
                    if btnSelectOne.text == "g" and btnSelect.text == "mcg": #converts grams to micrograms 
                        gsTomcgs = round(unitOne*1000000,5) 
                        entrConvertAns.text = str(gsTomcgs)
                    if btnSelectOne.text == "g" and btnSelect.text == "mg": #converts grams to milligrams
                        gsTomg = round(unitOne*1000,5)
                        entrConvertAns.text=str(gsTomg)
                
                    if btnSelectOne.text == "ibs" and btnSelect.text == "kg": #convert pounds to kilograms 
                        ibsTokg = round(unitOne/2.2046226218,5)
                        entrConvertAns.text = str(ibsTokg)
                    if btnSelectOne.text == "kg" and btnSelect.text == "ibs": #convert kilograms to pounds 
                        kgToibs = round(unitOne*2.2046,5)
                        entrConvertAns.text = str(kgToibs)
                    
                    if btnSelectOne.text == "ibs" and btnSelect.text == "ibs": #pounds to pounds
                        entrConvertAns.text = str(unitOne)
                    if btnSelectOne.text == "kg" and btnSelect.text == "kg": #kilograms to Kilograms 
                        entrConvertAns.text = str(unitOne)
                except: 
                    answer = "ERROR"
                    entrConvertAns.text = str(answer) 
                    
            def clearAll(self): #clearing all the text off the screen 
                entrNumberOne.text = ''
                entrConvertAns.text = ''
                    
            btnClearAll = Button(text="Clear All",size_hint=(0.65,0.1), pos_hint={'x':0.18, 'y':0.48},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1), 
                                 background_down=('black'))#background_down to change on press background color 
            btnClearAll.bind(on_release=clearAll)
            layoutHome.add_widget(btnClearAll)

            btnCalculate = Button(text="Convert",size_hint=(0.3,0.1), pos_hint={'x':0.53, 'y':0.58},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
            btnCalculate.bind(on_press=conversionCalc)
            layoutHome.add_widget(btnCalculate)
                
            btnReturnHome = Button(text="Return to Home",size_hint=(0.35,0.1), pos_hint={'x':0.18, 'y':0.58},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
         
        def Settings(self):
            
            clearScreen()
            lblSettings = Label(text="Settings", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9},color=(0,0,0,1))
            layoutHome.add_widget(lblSettings)
            
            lblDayMode = Label(text="Day Mode:", size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.8},color=(0,0,0,1))
            layoutHome.add_widget(lblDayMode)
            chkDayMode = CheckBox(group=1, size_hint=(0.3,0.1), pos_hint={'x':0.3, 'y':0.8},color=(0,0,0,1))
            layoutHome.add_widget(chkDayMode)
                  
            lblNightMode = Label(text="Night Mode:", size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.74},color=(0,0,0,1))
            layoutHome.add_widget(lblNightMode)
            chkNightMode = CheckBox(group=1, size_hint=(0.3,0.1), pos_hint={'x':0.3, 'y':0.74},color=(0,0,0,1))#setting active to true for night mode so app does not switch modes 
            layoutHome.add_widget(chkNightMode)
            
            lblBig = Label(text="Big Mode:", size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.68},color=(0,0,0,1))
            layoutHome.add_widget(lblBig)
            chkBig = CheckBox(group=1, size_hint=(0.3,0.1), pos_hint={'x':0.3, 'y':0.68},color=(0,0,0,1))#group groups the checkboxes together to make them radio buttons 
            layoutHome.add_widget(chkBig)
               
            def switchModes(self):
                if chkNightMode.active == True:#stay same
                    clearScreen()
                    medCalcDayApp().stop(self)
                    if __name__ == "__main__":
                        medCalc().run()
                if chkDayMode.active == True:#activate day mode    
                    pass
                if chkBig.active == True: #activate big mode 
                    clearScreen()#clears the screen
                    medCalcDayApp().stop() #stops Night Mode
                    if __name__ == "__main__": #runs day mode 
                        medCalcBigApp().run()

            #adding buttons to return to homescreen and calculate problem 
            def returnHome(self):
                clearScreen()
                createHomePage(self)
                
            btnReturnHome = Button(text="Return to Home",size_hint=(0.35,0.1), pos_hint={'x':0.18, 'y':0.44},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
            
            btnCalculate = Button(text="Switch Modes",size_hint=(0.3,0.1), pos_hint={'x':0.53, 'y':0.44},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
            btnCalculate.bind(on_press=switchModes)
            layoutHome.add_widget(btnCalculate)
            #grouping check boxes for selection buttons to get effect of a radio button 
            
        def ivInfusion(self):
            
            clearScreen()
            lblInfusion = Label(text="Infusion/Fluid Problem", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9},color=(0,0,0,1))
            layoutHome.add_widget(lblInfusion)
            
            lblVol = Label(text="Volume to be \ninfused in (mL)", size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.8},color=(0,0,0,1))
            layoutHome.add_widget(lblVol)
            entrVol = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.82}, multiline=False, cursor_color=(0,0,0,1))
            layoutHome.add_widget(entrVol)
            
            lblDropFact = Label(text="Dropset: ", size_hint=(0.3,0.1), pos_hint={'x':0.2, 'y':0.74},color=(0,0,0,1))
            layoutHome.add_widget(lblDropFact)
            entrDropFact = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.76}, multiline=False, cursor_color=(0,0,0,1))
            layoutHome.add_widget(entrDropFact)
            
            lblDuration = Label(text="Duration in Minutes ", size_hint=(0.3,0.1), pos_hint={'x':0.13, 'y':0.68},color=(0,0,0,1))
            layoutHome.add_widget(lblDuration)
            entrDuration = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.7}, multiline=False, cursor_color=(0,0,0,1))
            layoutHome.add_widget(entrDuration)
            
            lblInfans = Label(text="gtts/min: ", size_hint=(0.3,0.1), pos_hint={'x':0.2, 'y':0.62},color=(0,0,0,1))
            layoutHome.add_widget(lblInfans)
            entrInfans = TextInput(size_hint=(0.3,0.058), pos_hint={'x':0.48, 'y':0.64}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.4,0.78,0.831,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=20)#setbackground disabled to white first to avoid grey tint
            layoutHome.add_widget(entrInfans)
            
            #adding buttons to return to homescreen and calculate problem 
            def returnHome(self):
                clearScreen()
                createHomePage(self)
                
            def infusionCalc(self):
                try:
                    vol = float(entrVol.text)
                    drop = float(entrDropFact.text)
                    dur = float(entrDuration.text)
                    gtt = round(vol*drop/dur,5)#finding the drops per minute 
                    entrInfans.text = str(gtt)
                except:
                    answer = "ERROR"
                    entrInfans.text = str(answer)
                    
            def clearAll(self): #clearing all the text off the screen 
                entrVol.text = ''
                entrDropFact.text = ''
                entrDuration.text = '' 
                entrInfans.text = ''
                    
            btnClearAll = Button(text="Clear All",size_hint=(0.65,0.1), pos_hint={'x':0.18, 'y':0.4},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1),
                                 background_down=('black'))#background_down to change on press background color 
            btnClearAll.bind(on_release=clearAll)
            layoutHome.add_widget(btnClearAll)
                    
            btnReturnHome = Button(text="Return to Home",size_hint=(0.35,0.1), pos_hint={'x':0.18, 'y':0.5},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
            
            btnCalculate = Button(text="Calculate",size_hint=(0.3,0.1), pos_hint={'x':0.53, 'y':0.5},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
            btnCalculate.bind(on_press=infusionCalc)
            layoutHome.add_widget(btnCalculate)
            
        def formulasPage(self):
            
            clearScreen()
            lblFormulas = Label(text="Formulas", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9},color=(0,0,0,1))
            layoutHome.add_widget(lblFormulas)
            
            lblSupply = Label(text="Supply:\n mg / ml= mg per 1mL\n"+
                              "-------------------------------------", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.8},color=(0,0,0,1))
            layoutHome.add_widget(lblSupply)
            
            lblIvPush = Label(text="Iv Push:\n dose / supply per 1mL = mLs to Draw\n"+
                              "-------------------------------------", size_hint=(0.3,0.1), pos_hint={'x':0.25, 'y':0.7},color=(0,0,0,1))
            layoutHome.add_widget(lblIvPush)
            
            lblIvDrip = Label(text="Iv Drip:\n (dose*gtts)/Concentration per 1mL = gtts/min\n"+
                              "-------------------------------------", size_hint=(0.3,0.1), pos_hint={'x':0.33, 'y':0.6},color=(0,0,0,1))
            layoutHome.add_widget(lblIvDrip)
            
            lblDopa = Label(text="Dopamine:\n Dose(mcg)*kg*dropset) / Concen = gtts/min\n"+
                              "-------------------------------------", size_hint=(0.3,0.1), pos_hint={'x':0.32, 'y':0.5},color=(0,0,0,1))
            layoutHome.add_widget(lblDopa)
            
            lblInf = Label(text="Infusion/Fluid:\n(Volume*DropFactor)/ Minutes = gtts/min\n"+
                              "-------------------------------------", size_hint=(0.3,0.1), pos_hint={'x':0.30, 'y':0.4},color=(0,0,0,1))
            layoutHome.add_widget(lblInf)
            lblInf2 = Label(text="ml/hr to gtts/min\n(Volume*DropFactor)/ Minutes = gtts/min\n"+
                              "-------------------------------------", size_hint=(0.3,0.1), pos_hint={'x':0.30, 'y':0.3},color=(0,0,0,1))
            layoutHome.add_widget(lblInf2)
            
            def o2Tank(self):
                
                clearScreen()
                lblO2 = Label(text="O2 Tank Remaining Calculation", size_hint=(0.3,0.1), pos_hint={'x':0.2, 'y':0.9},color=(0,0,0,1))
                layoutHome.add_widget(lblO2)
                
                lblCyl = Label(text="Cylinder Factor", size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.8},color=(0,0,0,1))
                layoutHome.add_widget(lblCyl)
                
                lblCurrpsi = Label(text="Current PSI in Tank", size_hint=(0.3,0.1), pos_hint={'x':0.14, 'y':0.74},color=(0,0,0,1))
                layoutHome.add_widget(lblCurrpsi)
                entrCurrpsi = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.76}, multiline=False, cursor_color=(0,0,0,1))
                layoutHome.add_widget(entrCurrpsi)
            
                lbl02LPM = Label(text="liters per Minute(LPM) ", size_hint=(0.3,0.1), pos_hint={'x':0.10, 'y':0.68},color=(0,0,0,1))
                layoutHome.add_widget(lbl02LPM)
                entr02LPM = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.7}, multiline=False, cursor_color=(0,0,0,1))
                layoutHome.add_widget(entr02LPM)
     
                lbl02ans = Label(text="Minutes remaining ", size_hint=(0.3,0.1), pos_hint={'x':0.13, 'y':0.62},color=(0,0,0,1))
                layoutHome.add_widget(lbl02ans)
                entr02ans = TextInput(size_hint=(0.3,0.058), pos_hint={'x':0.48, 'y':0.64}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.4,0.78,0.831,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=20)#setbackground disabled to white first to avoid grey tint
                layoutHome.add_widget(entr02ans)
                
                lblres = Label(text="*Calculated with Safe residual\n pressure of 200PSI ", size_hint=(0.3,0.1), pos_hint={'x':0.3, 'y':0.55},color=(0,0,0,1))
                layoutHome.add_widget(lblres)
                
                #creating the dropdown list for convert to
                unitsDrop02 = DropDown()
                unitsList02 = ["D Cylinder",'Jumbo D','E Cylinder', 'M Cylinder', 'H Cylinder']
            
                #looping through the units           
                for i in unitsList02:
                    btnUnits02 = Button(text=i,size_hint_y=None, height=44,
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))#creating the buttons with parameters
                    btnUnits02.bind(on_release=lambda btnUnits02: unitsDrop02.select(btnUnits02.text))#binding the button to then set to its text 
                    unitsDrop02.add_widget(btnUnits02)#adding the buttons the the screen 
                    
                #creating the main button for 02 cylinder 
                btnSelect = Button(text='Tank Type',size_hint=(0.3,0.09), pos_hint={'x':0.48, 'y':0.82},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
                btnSelect.bind(on_release=unitsDrop02.open)
                layoutHome.add_widget(btnSelect)
                unitsDrop02.bind(on_select=lambda instance, x: setattr(btnSelect, 'text',x))
                def o2Calc(self):
                    try:
                        lpm = float(entr02LPM.text)
                        psi = float(entrCurrpsi.text)
                            
                        dCylfact = 0.16 #D cylinder factor
                        jumboDnECylfact = 0.28 #jumboD and E cylinder factor
                        mCylfact = 1.56 #M cylinder factor
                        hCylfact = 3.14 #H cylinder factor 
                        saferes = 200 #safe residual pressure 
                        
                        if btnSelect.text == "Tank Type":
                            answer = "ERR CHK TANK"
                            entr02ans.text = str(answer)
                        if btnSelect.text == "Jumbo D" or btnSelect.text == "E Cylinder":
                            oxygenLeftTime = round(((psi-saferes)*jumboDnECylfact)/lpm,5)
                            entr02ans.text = str(oxygenLeftTime) 
                        if btnSelect.text == "D Cylinder":
                            oxygenTimeleft = round(((psi-saferes)*dCylfact)/lpm,5)
                            entr02ans.text = str(oxygenTimeleft)  
                        if btnSelect.text == "M Cylinder":
                            o2Time = round(((psi-saferes)*mCylfact)/lpm,5)
                            entr02ans.text = str(o2Time)
                        if btnSelect.text == "H Cylinder":
                            o2Timeh = round(((psi-saferes)*hCylfact)/lpm,5)
                            entr02ans.text = str(o2Timeh)
                    except:
                        answer = "ERROR"
                        entr02ans.text = str(answer)
                        
                def clearAll(self): #clearing all the text off the screen 
                    entrCurrpsi.text = ''
                    entr02LPM.text = ''
                    entr02ans.text =''
                 
                def returnHome(self):
                    clearScreen()
                    createHomePage(self)
                    
                btnClearAll = Button(text="Clear All",size_hint=(0.65,0.1), pos_hint={'x':0.18, 'y':0.35},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1),
                                 background_down=('black'))#background_down to change on press background color 
                btnClearAll.bind(on_release=clearAll)
                layoutHome.add_widget(btnClearAll)
                    
                btnReturnHome = Button(text="Return to Home",size_hint=(0.35,0.1), pos_hint={'x':0.18, 'y':0.45},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
                btnReturnHome.bind(on_press=returnHome)
                layoutHome.add_widget(btnReturnHome)
            
                btnCalculate = Button(text="Calculate",size_hint=(0.3,0.1), pos_hint={'x':0.53, 'y':0.45},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
                btnCalculate.bind(on_press=o2Calc)#binding the button to 02 calc function 
                layoutHome.add_widget(btnCalculate)
                
            def burnFormula(self):
                
                clearScreen()
                lblBurnFormula = Label(text="Parkland Formula", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9},color=(0,0,0,1))
                layoutHome.add_widget(lblBurnFormula)
                
                lblml = Label(text="ML: ", size_hint=(0.3,0.1), pos_hint={'x':0.25, 'y':0.8},color=(0,0,0,1))
                layoutHome.add_widget(lblml)
                entrml = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.82}, multiline=False, disabled=True)
                entrml.text = str(4)#setting the default value for 4 for the parkland burn formula
                layoutHome.add_widget(entrml)
            
                lblTBSA = Label(text="TBSA(%) ", size_hint=(0.3,0.1), pos_hint={'x':0.23, 'y':0.74},color=(0,0,0,1))
                layoutHome.add_widget(lblTBSA)
                entrTBSA = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.76}, multiline=False, cursor_color=(0,0,0,1))
                layoutHome.add_widget(entrTBSA)
            
                lblkg = Label(text="KG: ", size_hint=(0.3,0.1), pos_hint={'x':0.25, 'y':0.68},color=(0,0,0,1))
                layoutHome.add_widget(lblkg)
                entrkg = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.7}, multiline=False, cursor_color=(0,0,0,1))
                layoutHome.add_widget(entrkg)
                
                lblDropFactor = Label(text="Drop Factor:", size_hint=(0.25,0.1), pos_hint={'x':0.22, 'y':0.62},color=(0,0,0,1))
                layoutHome.add_widget(lblDropFactor)
                entrDropFact = TextInput(size_hint=(0.3,0.06), pos_hint={'x':0.48, 'y':0.64}, multiline=False, cursor_color=(0,0,0,1))
                layoutHome.add_widget(entrDropFact)
                
                lblburnAns = Label(text="(FIRST 8 HRS) gtts/min ", size_hint=(0.25,0.1), pos_hint={'x':0.13, 'y':0.56},color=(0,0,0,1))
                layoutHome.add_widget(lblburnAns)
                entrburnAns = TextInput(size_hint=(0.3,0.058), pos_hint={'x':0.48, 'y':0.58}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.4,0.78,0.831,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=20)#setbackground disabled to white first to avoid grey tint
                layoutHome.add_widget(entrburnAns)
                
                lblburnAns2 = Label(text="(NEXT 16 HRS) gtts/min ", size_hint=(0.25,0.1), pos_hint={'x':0.13, 'y':0.50},color=(0,0,0,1))
                layoutHome.add_widget(lblburnAns2)
                entrburnAns2 = TextInput(size_hint=(0.3,0.058), pos_hint={'x':0.48, 'y':0.52}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.4,0.78,0.831,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=20)#setbackground disabled to white first to avoid grey tint
                layoutHome.add_widget(entrburnAns2)
                
                lblburnTotal = Label(text="Total mL ovr 24HRS ", size_hint=(0.25,0.1), pos_hint={'x':0.13, 'y':0.44},color=(0,0,0,1))
                layoutHome.add_widget(lblburnTotal)
                entrburnTotal = TextInput(size_hint=(0.3,0.058), pos_hint={'x':0.48, 'y':0.46}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.4,0.78,0.831,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=20)#setbackground disabled to white first to avoid grey tint
                layoutHome.add_widget(entrburnTotal)
                
                #adding buttons to return to homescreen and calculate problem 
                def returnHome(self):
                    clearScreen()
                    createHomePage(self)
                def burnCalc(self):
                    try: 
                        burnml = 4.0
                        burnBSA= float(entrTBSA.text)
                        wt = float(entrkg.text)
                        fluidvol = burnml*burnBSA*wt
                        dropFactor = float(entrDropFact.text)
                         
                        first8 = (burnml*burnBSA*wt) #The first half of NS or LR is given over first 8 hours 
                        gttsFirst = round(first8*dropFactor/480,5)#480 is the amount of minutes in 8 hours for infusion problem 
                        entrburnAns.text = str(gttsFirst)
                        
                        gttsSecond = round(first8*dropFactor/960)#960 is the amount of minutes in 2nd 16 hours 
                        entrburnAns2.text = str(gttsSecond)
                         
                        total = burnml*burnBSA*wt
                        entrburnTotal.text = str(total)
                    except:
                        answer = "ERROR"
                        entrburnTotal.text = str(answer)
                        entrburnAns.text = str(answer)
                        entrburnAns2.text = str(answer)
                        
                def clearAll(self): #clearing all the text off the screen 
                    entrTBSA.text = '' 
                    entrkg.text = ''
                    entrburnAns.text = '' 
                    entrburnAns2.text = ''
                    entrburnTotal.text = '' 
                    entrDropFact.text = ''
                    
                        
                btnClearAll = Button(text="Clear All",size_hint=(0.65,0.1), pos_hint={'x':0.18, 'y':0.25},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1),
                                 background_down=('black'))#background_down to change on press background color 
                btnClearAll.bind(on_release=clearAll)
                layoutHome.add_widget(btnClearAll)
                        
                btnCalculate = Button(text="Calculate",size_hint=(0.3,0.1), pos_hint={'x':0.53, 'y':0.35},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
                btnCalculate.bind(on_press=burnCalc)
                layoutHome.add_widget(btnCalculate)
                
                btnReturnHome = Button(text="Return to Home",size_hint=(0.35,0.1), pos_hint={'x':0.18, 'y':0.35},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
                btnReturnHome.bind(on_press=returnHome)
                layoutHome.add_widget(btnReturnHome)
                
            #-----------------END BURN FORMULA---------------------------------------------------------------
            #adding buttons to return to homescreen and calculate problem 
            def returnHome(self):
                clearScreen()
                createHomePage(self)
            
            btnReturnHome = Button(text="Return to Home",size_hint=(0.35,0.1), pos_hint={'x':0.07, 'y':0.1},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
            
            btnO2Tank = Button (text="O2 Time Calc", size_hint=(0.35,0.1),pos_hint={'x':0.07, 'y':0.2},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
            btnO2Tank.bind(on_press=o2Tank)
            layoutHome.add_widget(btnO2Tank)
            
            btnO2Tank = Button (text="Burn Formula", size_hint=(0.35,0.1),pos_hint={'x':0.42, 'y':0.2},
                                 background_normal='', background_color=(0.737,0.737,0.737,1),color=(0,0,0,1))
            btnO2Tank.bind(on_press=burnFormula)
            layoutHome.add_widget(btnO2Tank)
            #----------------------------END FORMULAS FUNCTION 
#-------------------------------END FUNCTIONS-------------------------------------------------------------
        #adding actions to the buttons for disclaimer 
        btnYes.bind(on_press=pressYes)
        btnNo.bind(on_press=pressNo)        
        self.add_widget(layoutHome)#adding the innerlayout to the root
   
#------------END DAY MODE------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------
#------------Begin Big Mode----------------------------------------------------------------------
class medCalcBig(RelativeLayout):
    def __init__(self,**kwargs):#creating the constructor 
        super(medCalcBig, self).__init__(**kwargs)
        
        layoutHome = RelativeLayout() #creating the innerlayout
        Window.clearcolor=(0.157,0.157,0.157,1)# setting the background window color 
        lblDisclaimer = (Label(text="This application is intended to check the \nprovides math. If any discrepancies\n" +
                            "arise refer to providers hand-written math, \nand re-check ALL calculations. \nDo you agree to these terms of serive?",pos_hint={'center_x':0.5, 'center_y':0.8},font_size=16 )
                              )#
        layoutHome.add_widget(lblDisclaimer)
        #creating and adding buttons to disclaimer Window
        btnYes = Button(text="Accept", size_hint=(0.5,0.2), pos_hint={'center_x':0.5, 'center_y':0.3},
                        color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),font_size=20)#Place button bottom center can also use {'center_x': 0, 'center_y':0} 
        layoutHome.add_widget(btnYes) #adding button to screen 
        btnNo = Button(text="Decline", size_hint=(0.5,0.2),pos_hint={'center_x':0.5, 'center_y':0.5},
                       color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),font_size=20) #place button on top of accept button 
        layoutHome.add_widget(btnNo)
        #-----Functions for Disclaimer-----
        def pressYes(self):
            layoutHome.clear_widgets()#clears all widgets from the frame 
            createHomePage(self)  
        def pressNo(self):
            medCalc().stop() #exiting the program 
        #-----Misc Functions---------------
        def clearScreen():
            layoutHome.clear_widgets()     
        #---------------------------------- 
        #Creating the Homepage 
        #----------------------------------         
        def createHomePage(self):
            Window.clearcolor=(0.157,0.157,0.157,1)# setting the background window color 
            lblHomePageTest = Label(text="Please Select Problem Type: ",size_hint=(0.3,0.1), pos_hint={'x':0.362, 'y':0.88},color=(.9,.9,.9,1), font_size=(20)) #color = how to change label text color 
            layoutHome.add_widget(lblHomePageTest)
            
            #adding buttons to problem types 
            btnSupply = Button(text="Supply per 1mL",size_hint=(0.6,0.1), pos_hint={'center_x':0.5, 'y':0.78},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1), font_size=(20))
            btnSupply.bind(on_press=Supply)#binding the button to a function, RGBA decimals divide by 255 
            layoutHome.add_widget(btnSupply)
            
            btnIvp = Button(text="IV Push",size_hint=(0.6,0.1), pos_hint={'center_x':0.5, 'y':0.68},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1), font_size=(20))
            btnIvp.bind(on_press=IvPush)
            layoutHome.add_widget(btnIvp)
            
            btnIvd = Button(text="IV Drip Problem",size_hint=(0.6,0.1), pos_hint={'center_x':0.5, 'y':0.58},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1), font_size=(20))
            btnIvd.bind(on_press=IvDrip)
            layoutHome.add_widget(btnIvd)
            
            btnDopa = Button(text="Dopamine Problem",size_hint=(0.6,0.1), pos_hint={'center_x':0.5, 'y':0.48},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1), font_size=(20))
            btnDopa.bind(on_press=Dopamine)
            layoutHome.add_widget(btnDopa)
            
            btnivInfusion = Button(text="Infusion Problem",size_hint=(0.6,0.1), pos_hint={'center_x':0.5,'y':0.38},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1), font_size=(20))
            btnivInfusion.bind(on_press=ivInfusion)
            layoutHome.add_widget(btnivInfusion)
            
            btnConvert = Button(text="Conversion",size_hint=(0.6,0.1), pos_hint={'center_x':0.5, 'y':0.28},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1), font_size=(20))
            btnConvert.bind(on_press=Conversion)
            layoutHome.add_widget(btnConvert)
            
            btnFormulas = Button(text="Formulas/O2/Burn",size_hint=(0.6,0.1), pos_hint={'center_x':0.5,'y':0.18},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1), font_size=(20))
            btnFormulas.bind(on_press=formulasPage)
            layoutHome.add_widget(btnFormulas)
            
            btnSettings = Button(text="Settings",size_hint=(0.6,0.1), pos_hint={'center_x':0.5, 'y':0.08},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1), font_size=(20))
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
            
            lblSupply = Label(text="Find supply per 1mL",size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblSupply)
            
            #creating buttons for supply 
            lblMgs = Label(text="Enter milligrams\n                   (MG): ",size_hint=(0.3,0.1), pos_hint={'x':0.14, 'y':0.82},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblMgs)
            entrMgs = TextInput(size_hint=(0.4,0.09), pos_hint={'x':0.48, 'y':0.82}, multiline=False, cursor_color=(0,0,0,1), unfocus_on_touch=False,font_size=20)
            layoutHome.add_widget(entrMgs)
            
            lblMls = Label(text="Enter milliliters\n                 (mL): ",size_hint=(0.3,0.1), pos_hint={'x':0.14, 'y':0.72},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblMls)
            entrMls = TextInput(size_hint=(0.4,0.09), pos_hint={'x':0.48, 'y':0.72}, multiline=False, cursor_color=(0,0,0,1), unfocus_on_touch=False,font_size=20)
            layoutHome.add_widget(entrMls)
            
            lblMgspMl = Label(text="      Milligrams \n         per 1 mL: ",size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.62},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblMgspMl)
            
            txtAnswerSupp = TextInput(size_hint=(0.4,0.088), pos_hint={'x':0.48, 'y':0.62}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.91,0.91,0.031,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=24)#setbackground disabled to white first to avoid grey tint 
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
                    txtAnswerSupp.text = str((answer))#converting the answer back to a string and placing into text input box 
                except:
                    answer = "ERROR" #if exception is thrown then give error for answer 
                    txtAnswerSupp.text = answer

            def clearAll(self): #clearing all the text off the screen 
                entrMgs.text = ''
                entrMls.text = ''
                txtAnswerSupp.text = '' 
                
            btnClearAll = Button(text="Clear All",size_hint=(0.77,0.15), pos_hint={'x':0.13, 'y':0.35},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),
                                 background_down=('black'),font_size=18)#background_down to change on press background color 
            btnClearAll.bind(on_release=clearAll)
            layoutHome.add_widget(btnClearAll)
 
            btnReturnHome = Button(text="Return Home",size_hint=(0.4,0.1), pos_hint={'x':0.13, 'y':0.50},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),font_size=18)
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
            
            btnCalculate = Button(text="Calculate",size_hint=(0.4,0.1), pos_hint={'x':0.5, 'y':0.50},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),font_size=18)
            btnCalculate.bind(on_press=supplyCalc)
            layoutHome.add_widget(btnCalculate)  
        
        #---------------------------------- 
        #End Supply Fx  
        #----------------------------------
        def IvPush(self):
            
            clearScreen()
            lblIvPush = Label(text="IV Push Problem", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblIvPush)
            
            lblDoseMg = Label(text="Enter Dose (Mg): ", size_hint=(0.3,0.1), pos_hint={'x':0.14, 'y':0.82},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblDoseMg) 
            entrMG = TextInput(size_hint=(0.4,0.09), pos_hint={'x':0.48, 'y':0.82}, multiline=False, cursor_color=(0,0,0,1),font_size=20)
            layoutHome.add_widget(entrMG)
            
            lblSuppml = Label(text="Supply per \n1mL(Mg/1mL): ", size_hint=(0.3,0.1), pos_hint={'x':0.13, 'y':0.72},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblSuppml)
            entrML = TextInput(size_hint=(0.4,0.09), pos_hint={'x':0.48, 'y':0.72}, multiline=False, cursor_color=(0,0,0,1),font_size=20)
            layoutHome.add_widget(entrML)
            
            lblMlstoDraw = Label(text="mLs to Draw: ", size_hint=(0.3,0.1), pos_hint={'x':0.13, 'y':0.62},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblMlstoDraw) 
            entrAnswer = TextInput(size_hint=(0.4,0.088), pos_hint={'x':0.48, 'y':0.62}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.91,0.91,0.031,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=24)#setbackground disabled to white first to avoid grey tint
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
                    
            def clearAll(self): #clearing all the text off the screen 
                entrMG.text = ''
                entrML.text = ''
                entrAnswer.text = ''     
                    
            btnClearAll = Button(text="Clear All",size_hint=(0.77,0.15), pos_hint={'x':0.13, 'y':0.35},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),
                                 background_down=('black'),font_size=18)#background_down to change on press background color 
            btnClearAll.bind(on_release=clearAll)
            layoutHome.add_widget(btnClearAll)               
            
            btnReturnHome = Button(text="Return Home",size_hint=(0.4,0.1), pos_hint={'x':0.13, 'y':0.5},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),font_size=18)
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
            
            btnCalculate = Button(text="Calculate",size_hint=(0.4,0.1), pos_hint={'x':0.50, 'y':0.5},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),font_size=18)
            btnCalculate.bind(on_press=ivpCalc)
            layoutHome.add_widget(btnCalculate)

        def IvDrip(self):
            
            clearScreen()
            lblIvDrip = Label(text="Iv Drip Problem", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblIvDrip)
            
            lblMgTotal = Label(text="Total Amt to \nGive(Mg/min): ", size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.82},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblMgTotal)
            entrMgTotal = TextInput(size_hint=(0.4,0.09), pos_hint={'x':0.48, 'y':0.82}, multiline=False, cursor_color=(0,0,0,1),font_size=20)
            layoutHome.add_widget(entrMgTotal)
            
            lblDropset = Label(text="Enter Dropset: ", size_hint=(0.3,0.1), pos_hint={'x':0.13, 'y':0.72},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblDropset)
            entrDropset = TextInput(size_hint=(0.4,0.09), pos_hint={'x':0.48, 'y':0.72}, multiline=False, cursor_color=(0,0,0,1),font_size=20)
            layoutHome.add_widget(entrDropset)
            
            lblConcml = Label(text="    Concentration\n            (Mg/1mL): ", size_hint=(0.3,0.1), pos_hint={'x':0.13, 'y':0.62},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblConcml)
            entrConc = TextInput(size_hint=(0.4,0.09), pos_hint={'x':0.48, 'y':0.62}, multiline=False, cursor_color=(0,0,0,1),font_size=20)
            layoutHome.add_widget(entrConc)
            
            lblDripRate = Label(text="Drops per Minute\n            (gtts/min): ", size_hint=(0.3,0.1), pos_hint={'x':0.13, 'y':0.52},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblDripRate)
            entrDripRate = TextInput(size_hint=(0.4,0.09), pos_hint={'x':0.48, 'y':0.52}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.91,0.91,0.031,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=24)#setbackground disabled to white first to avoid grey tint
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
                    
            def clearAll(self): #clearing all the text off the screen 
                entrMgTotal.text = ''
                entrDropset.text = ''
                entrConc.text = ''
                entrDripRate.text = ''  
                          
            btnClearAll = Button(text="Clear All",size_hint=(0.8,0.15), pos_hint={'x':0.13, 'y':0.25},color=(.9,.9,.9,2),background_color=(.8,.8,.8,1),
                                 background_down=('black'),font_size=18)#background_down to change on press background color 
            btnClearAll.bind(on_release=clearAll)
            layoutHome.add_widget(btnClearAll)
                
            btnReturnHome = Button(text="Return Home",size_hint=(0.4,0.1), pos_hint={'x':0.13, 'y':0.4},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),font_size=18)
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
            
            btnCalculate = Button(text="Calculate",size_hint=(0.4,0.1), pos_hint={'x':0.53, 'y':0.4},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),font_size=18)
            btnCalculate.bind(on_press=ivDripCalc)
            layoutHome.add_widget(btnCalculate)
            
        def Dopamine(self):
            
            clearScreen() 
            lblDopamine = Label(text="Dopamine Problem", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblDopamine)
            
            lblMcgDose = Label(text="Dose (mcg/min): ", size_hint=(0.3,0.1), pos_hint={'x':0.14, 'y':0.82},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblMcgDose)
            entrMcgDose = TextInput(size_hint=(0.4,0.09), pos_hint={'x':0.48, 'y':0.82}, multiline=False, cursor_color=(0,0,0,1),font_size=20)
            layoutHome.add_widget(entrMcgDose)
            
            lblKgwt = Label(text="Weight in Kg: ", size_hint=(0.3,0.1), pos_hint={'x':0.18, 'y':0.72},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblKgwt)
            entrKgwt = TextInput(size_hint=(0.4,0.09), pos_hint={'x':0.48, 'y':0.72}, multiline=False, cursor_color=(0,0,0,1),font_size=20)
            layoutHome.add_widget(entrKgwt)
            
            lblDropset = Label(text="Dropset: ", size_hint=(0.3,0.1), pos_hint={'x':0.22, 'y':0.62},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblDropset)
            entrDropset = TextInput(size_hint=(0.4,0.09), pos_hint={'x':0.48, 'y':0.62}, multiline=False,font_size=20,disabled=True)
            entrDropset.text = str(60)#adding the 60 dropset in for user to see 
            layoutHome.add_widget(entrDropset)
            
            lblConcMcg = Label(text="Concentration \n      (mcg/mL): ", size_hint=(0.3,0.1), pos_hint={'x':0.16, 'y':0.52},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblConcMcg)
            entrConcMcg = TextInput(size_hint=(0.4,0.09), pos_hint={'x':0.48, 'y':0.52}, multiline=False, cursor_color=(0,0,0,1),font_size=20)
            layoutHome.add_widget(entrConcMcg)
            
            lblDopaAns = Label(text="Drops per Minute \n          (gtts/min): ", size_hint=(0.3,0.1), pos_hint={'x':0.13,'y':0.42},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblDopaAns)
            entrDopaAns = TextInput(size_hint=(0.4,0.088), pos_hint={'x':0.48, 'y':0.42}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.91,0.91,0.031,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=24)#setbackground disabled to white first to avoid grey tint
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
                    
            def clearAll(self): #clearing all the text off the screen 
                entrMcgDose.text = ''
                entrConcMcg.text = ''
                entrKgwt.text = ''
                entrDopaAns.text = ''  
                    
            btnClearAll = Button(text="Clear All",size_hint=(0.8,0.15), pos_hint={'x':0.13, 'y':0.13},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),
                                 background_down=('black'),font_size=18)#background_down to change on press background color 
            btnClearAll.bind(on_release=clearAll)
            layoutHome.add_widget(btnClearAll)
                
            btnReturnHome = Button(text="Return Home",size_hint=(0.4,0.1), pos_hint={'x':0.13, 'y':0.28},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),font_size=18)
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
            
            btnCalculate = Button(text="Calculate",size_hint=(0.4,0.1), pos_hint={'x':0.53, 'y':0.28},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),font_size=18)
            btnCalculate.bind(on_press=DopamineCalc)
            layoutHome.add_widget(btnCalculate)

        def Conversion(self):
            
            clearScreen()
            lblConversion = Label(text="Conversions", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblConversion)
            
            lblNumberOne = Label(text="Unit Amt ", size_hint=(0.3,0.1), pos_hint={'x':0.06, 'y':0.82},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblNumberOne)
            entrNumberOne = TextInput(size_hint=(0.3,0.09), pos_hint={'x':0.36, 'y':0.82}, multiline=False, cursor_color=(0,0,0,1),font_size=20)
            layoutHome.add_widget(entrNumberOne)
            
            #creating the dropdown list for number1  
            numOneDrop = DropDown()
            numOneUnits = ["mg",'g','mcg', 'ibs', 'kg']
          
            #looping through the units           
            for i in numOneUnits:
                btnNumOneUnits = Button(text= i,size_hint_y=None, height=44,color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),font_size=16)#creating the buttons with parameters, can also for '%r' for text
                btnNumOneUnits.bind(on_release=lambda btnNumOneUnits: numOneDrop.select(btnNumOneUnits.text))#binding the button to then set to its text 
                numOneDrop.add_widget(btnNumOneUnits)#adding the buttons the the screen
 
            lblConvertTo = Label(text="Convert to", size_hint=(0.3,0.1), pos_hint={'x':0.08, 'y':0.74},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblConvertTo)
            
            #creating the dropdown list for convert to
            unitsDrop = DropDown()
            unitsList = ["mg",'g','mcg', 'ibs', 'kg']
            
            #looping through the units           
            for i in unitsList:
                btnUnits = Button(text=i,size_hint_y=None, height=44,color=(.9,.9,.9,1),background_color=(.8,.8,.8,1))#creating the buttons with parameters
                btnUnits.bind(on_release=lambda btnUnits: unitsDrop.select(btnUnits.text))#binding the button to then set to its text 
                unitsDrop.add_widget(btnUnits)#adding the buttons the the screen 
                
            #creating the main button for Convert to
            btnSelect = Button(text='Select Units',size_hint=(0.4,0.08), pos_hint={'x':0.36, 'y':0.74},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),font_size=18)
            btnSelect.bind(on_release=unitsDrop.open)
            layoutHome.add_widget(btnSelect)
            unitsDrop.bind(on_select=lambda instance, x: setattr(btnSelect, 'text',x))
            
            #creating the main button for Num1 Convert units 
            btnSelectOne = Button(text='Select Units',size_hint=(0.3,0.08), pos_hint={'x':0.66, 'y':0.83},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),font_size=18)
            btnSelectOne.bind(on_release=numOneDrop.open)
            layoutHome.add_widget(btnSelectOne)
            numOneDrop.bind(on_select=lambda instance, x: setattr(btnSelectOne, 'text',x))
            
            lblConvertAns = Label(text="Answer", size_hint=(0.3,0.1), pos_hint={'x':0.06,'y':0.65},color=(.9,.9,.9,1),font_size=18)#answer for the conversion output and label 
            layoutHome.add_widget(lblConvertAns)
            entrConvertAns = TextInput(size_hint=(0.4,0.088), pos_hint={'x':0.36, 'y':0.65}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.91,0.91,0.031,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=20)#setbackground disabled to white first to avoid grey tint
            layoutHome.add_widget(entrConvertAns)
            #------------------------------------------------------------
            #adding buttons to return to homescreen and calculate problem 
            def returnHome(self):
                clearScreen()
                createHomePage(self)
            def conversionCalc(self):  
                try:
                    unitOne = float(entrNumberOne.text)
                    
                    #error checking for ibs and kilograms
                    if btnSelectOne.text == "ibs" or btnSelectOne == "kg" and btnSelect.text != "ibs" or btnSelect.text != "kg":
                        answer = "ERROR CHK UNITS"
                        entrConvertAns.text = str(answer)
                    if btnSelectOne.text != "ibs" or btnSelectOne != "kg" and btnSelect.text == "ibs" or btnSelect.text == "kg":
                        answer = "ERROR CHK UNITS"
                        entrConvertAns.text = str(answer)
                    #start calculations 
                    if btnSelectOne.text == "mcg" and btnSelect.text == "mg": #converts micrograms to milligrams 
                        mcgsTomgs = round(unitOne*0.001,5)
                        entrConvertAns.text = str(mcgsTomgs)
                    if btnSelectOne.text == "mcg" and btnSelect.text == "g": #converts micrograms to grams
                        mcgsTogs = round(unitOne/1000000,5)
                        
                        entrConvertAns.text=str(mcgsTogs)
                    if btnSelectOne.text == "mg" and btnSelect.text == "mcg": #converts milligrams to micrograms 
                        mgsTomcgs = round(unitOne*1000,5)
                        entrConvertAns.text = str(mgsTomcgs)
                    if btnSelectOne.text == "mg" and btnSelect.text == "g": #converts milligrams to grams
                        mgsTogs = round(unitOne/1000,5)
                        entrConvertAns.text=str(mgsTogs)
                    
                    if btnSelectOne.text == "g" and btnSelect.text == "mcg": #converts grams to micrograms 
                        gsTomcgs = round(unitOne*1000000,5) 
                        entrConvertAns.text = str(gsTomcgs)
                    if btnSelectOne.text == "g" and btnSelect.text == "mg": #converts grams to milligrams
                        gsTomg = round(unitOne*1000,5)
                        entrConvertAns.text=str(gsTomg)
                
                    if btnSelectOne.text == "ibs" and btnSelect.text == "kg": #convert pounds to kilograms 
                        ibsTokg = round(unitOne/2.2046226218,5)
                        entrConvertAns.text = str(ibsTokg)
                    if btnSelectOne.text == "kg" and btnSelect.text == "ibs": #convert kilograms to pounds 
                        kgToibs = round(unitOne*2.2046,5)
                        entrConvertAns.text = str(kgToibs)
                    
                    if btnSelectOne.text == "ibs" and btnSelect.text == "ibs": #pounds to pounds
                        entrConvertAns.text = str(unitOne)
                    if btnSelectOne.text == "kg" and btnSelect.text == "kg": #kilograms to Kilograms 
                        entrConvertAns.text = str(unitOne)
                except: 
                    answer = "ERROR"
                    entrConvertAns.text = str(answer) 
                    
            def clearAll(self): #clearing all the text off the screen 
                entrNumberOne.text = ''
                entrConvertAns.text = ''
                    
            btnClearAll = Button(text="Clear All",size_hint=(0.8,0.15), pos_hint={'x':0.13, 'y':0.38},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),
                                 background_down=('black'),font_size=18)#background_down to change on press background color 
            btnClearAll.bind(on_release=clearAll)
            layoutHome.add_widget(btnClearAll)

            btnCalculate = Button(text="Convert",size_hint=(0.4,0.1), pos_hint={'x':0.53, 'y':0.53},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),font_size=18)
            btnCalculate.bind(on_press=conversionCalc)
            layoutHome.add_widget(btnCalculate)
                
            btnReturnHome = Button(text="Return Home",size_hint=(0.4,0.1), pos_hint={'x':0.13, 'y':0.53},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),font_size=18)
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
         
        def Settings(self):
            
            clearScreen()
            lblSettings = Label(text="Settings", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblSettings)
            
            lblDayMode = Label(text="Day Mode:", size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.8},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblDayMode)
            chkDayMode = CheckBox(group=1, size_hint=(0.3,0.1), pos_hint={'x':0.3, 'y':0.8})
            layoutHome.add_widget(chkDayMode)
                  
            lblNightMode = Label(text="Night Mode:", size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.74},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblNightMode)
            chkNightMode = CheckBox(group=1, size_hint=(0.3,0.1), pos_hint={'x':0.3, 'y':0.74})#setting active to true for night mode so app does not switch modes 
            layoutHome.add_widget(chkNightMode)
            
            lblBig = Label(text="Big Mode:", size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.68},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblBig)
            chkBig = CheckBox(group=1, size_hint=(0.3,0.1), pos_hint={'x':0.3, 'y':0.68})#group groups the checkboxes together to make them radio buttons 
            layoutHome.add_widget(chkBig)
               
            def switchModes(self):
                if chkNightMode.active == True:#stay same
                    clearScreen()#clears the screen
                    medCalcBigApp().stop(self) #stops Night Mode
                    if __name__ == "__main__": #runs day mode 
                        medCalc().run()
                if chkDayMode.active == True:#activate day mode    
                    clearScreen()#clears the screen
                    medCalcBigApp().stop() #stops Night Mode
                    if __name__ == "__main__": #runs day mode 
                        medCalcDayApp().run()
                if chkBig.active == True: #activate big mode 
                    pass

            #adding buttons to return to homescreen and calculate problem 
            def returnHome(self):
                clearScreen()
                createHomePage(self)
                
            btnReturnHome = Button(text="Return to Home",size_hint=(0.4,0.1), pos_hint={'x':0.13, 'y':0.44},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),font_size=18)
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
            
            btnCalculate = Button(text="Switch Modes",size_hint=(0.4,0.1), pos_hint={'x':0.53, 'y':0.44},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),font_size=18)
            btnCalculate.bind(on_press=switchModes)
            layoutHome.add_widget(btnCalculate)
            #grouping check boxes for selection buttons to get effect of a radio button 
            
        def ivInfusion(self):
            
            clearScreen()
            lblInfusion = Label(text="     Infusion/Fluid Problem", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblInfusion)
            
            lblVol = Label(text="Volume to be \ninfused in (mL)", size_hint=(0.3,0.1), pos_hint={'x':0.15, 'y':0.82},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblVol)
            entrVol = TextInput(size_hint=(0.4,0.09), pos_hint={'x':0.48, 'y':0.82}, multiline=False, cursor_color=(0,0,0,1),font_size=20)
            layoutHome.add_widget(entrVol)
            
            lblDropFact = Label(text="Dropset: ", size_hint=(0.3,0.1), pos_hint={'x':0.2, 'y':0.72},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblDropFact)
            entrDropFact = TextInput(size_hint=(0.4,0.09), pos_hint={'x':0.48, 'y':0.72}, multiline=False, cursor_color=(0,0,0,1),font_size=20)
            layoutHome.add_widget(entrDropFact)
            
            lblDuration = Label(text="          Duration in \n               Minutes ", size_hint=(0.3,0.1), pos_hint={'x':0.13, 'y':0.62},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblDuration)
            entrDuration = TextInput(size_hint=(0.4,0.09), pos_hint={'x':0.48, 'y':0.62}, multiline=False, cursor_color=(0,0,0,1),font_size=20)
            layoutHome.add_widget(entrDuration)
            
            lblInfans = Label(text="gtts/min: ", size_hint=(0.3,0.1), pos_hint={'x':0.2, 'y':0.52},color=(.9,.9,.9,1),font_size=18)
            layoutHome.add_widget(lblInfans)
            entrInfans = TextInput(size_hint=(0.4,0.088), pos_hint={'x':0.48, 'y':0.52}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.91,0.91,0.031,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=24)#setbackground disabled to white first to avoid grey tint
            layoutHome.add_widget(entrInfans)
            
            #adding buttons to return to homescreen and calculate problem 
            def returnHome(self):
                clearScreen()
                createHomePage(self)
                
            def infusionCalc(self):
                try:
                    vol = float(entrVol.text)
                    drop = float(entrDropFact.text)
                    dur = float(entrDuration.text)
                    gtt = round(vol*drop/dur,5)#finding the drops per minute 
                    entrInfans.text = str(gtt)
                except:
                    answer = "ERROR"
                    entrInfans.text = str(answer)
                    
            def clearAll(self): #clearing all the text off the screen 
                entrVol.text = ''
                entrDropFact.text = ''
                entrDuration.text = '' 
                entrInfans.text = ''
                    
            btnClearAll = Button(text="Clear All",size_hint=(0.79,0.15), pos_hint={'x':0.13, 'y':0.25},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),
                                 background_down=('black'),font_size=18)#background_down to change on press background color 
            btnClearAll.bind(on_release=clearAll)
            layoutHome.add_widget(btnClearAll)
                    
            btnReturnHome = Button(text="Return Home",size_hint=(0.4,0.1), pos_hint={'x':0.13, 'y':0.4},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),font_size=18)
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
            
            btnCalculate = Button(text="Calculate",size_hint=(0.4,0.1), pos_hint={'x':0.53, 'y':0.4},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),font_size=18)
            btnCalculate.bind(on_press=infusionCalc)
            layoutHome.add_widget(btnCalculate)
            
        def formulasPage(self):
            
            clearScreen()
            lblFormulas = Label(text="Formulas", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9})
            layoutHome.add_widget(lblFormulas)
            
            lblSupply = Label(text="Supply:\n mg / ml= mg per 1mL\n"+
                              "-------------------------------------", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.8})
            layoutHome.add_widget(lblSupply)
            
            lblIvPush = Label(text="Iv Push:\n dose / supply per 1mL = mLs to Draw\n"+
                              "-------------------------------------", size_hint=(0.3,0.1), pos_hint={'x':0.25, 'y':0.7})
            layoutHome.add_widget(lblIvPush)
            
            lblIvDrip = Label(text="Iv Drip:\n (dose*gtts)/Concentration per 1mL = gtts/min\n"+
                              "-------------------------------------", size_hint=(0.3,0.1), pos_hint={'x':0.33, 'y':0.6})
            layoutHome.add_widget(lblIvDrip)
            
            lblDopa = Label(text="Dopamine:\n Dose(mcg)*kg*dropset) / Concen = gtts/min\n"+
                              "-------------------------------------", size_hint=(0.3,0.1), pos_hint={'x':0.32, 'y':0.5})
            layoutHome.add_widget(lblDopa)
            
            lblInf = Label(text="Infusion/Fluid:\n(Volume*DropFactor)/ Minutes = gtts/min\n"+
                              "-------------------------------------", size_hint=(0.3,0.1), pos_hint={'x':0.30, 'y':0.4})
            layoutHome.add_widget(lblInf)
            lblInf2 = Label(text="ml/hr to gtts/min\n(Volume*DropFactor)/ Minutes = gtts/min\n"+
                              "-------------------------------------", size_hint=(0.3,0.1), pos_hint={'x':0.30, 'y':0.3})
            layoutHome.add_widget(lblInf2)
            
            def o2Tank(self):
                
                clearScreen()
                lblO2 = Label(text="O2 Tank Remaining Calculation", size_hint=(0.3,0.1), pos_hint={'x':0.3, 'y':0.9},color=(.9,.9,.9,1),font_size=18)
                layoutHome.add_widget(lblO2)
                
                lblCyl = Label(text="Cylinder \nFactor", size_hint=(0.3,0.1), pos_hint={'x':0.18, 'y':0.82},color=(.9,.9,.9,1),font_size=18)
                layoutHome.add_widget(lblCyl)
                
                lblCurrpsi = Label(text="Current PSI \n      in Tank", size_hint=(0.3,0.1), pos_hint={'x':0.18, 'y':0.72},color=(.9,.9,.9,1),font_size=18)
                layoutHome.add_widget(lblCurrpsi)
                entrCurrpsi = TextInput(size_hint=(0.4,0.09), pos_hint={'x':0.48, 'y':0.72}, multiline=False, cursor_color=(0,0,0,1),font_size=20)
                layoutHome.add_widget(entrCurrpsi)
            
                lbl02LPM = Label(text="liters per \nMinute(LPM) ", size_hint=(0.3,0.1), pos_hint={'x':0.18, 'y':0.62},color=(.9,.9,.9,1),font_size=18)
                layoutHome.add_widget(lbl02LPM)
                entr02LPM = TextInput(size_hint=(0.4,0.09), pos_hint={'x':0.48, 'y':0.62}, multiline=False, cursor_color=(0,0,0,1),font_size=20)
                layoutHome.add_widget(entr02LPM)
     
                lbl02ans = Label(text="Minutes \nremaining ", size_hint=(0.3,0.1), pos_hint={'x':0.18, 'y':0.52},color=(.9,.9,.9,1),font_size=18)
                layoutHome.add_widget(lbl02ans)
                entr02ans = TextInput(size_hint=(0.4,0.088), pos_hint={'x':0.48, 'y':0.52}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.91,0.91,0.031,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=24)#setbackground disabled to white first to avoid grey tint
                layoutHome.add_widget(entr02ans)
                
                lblres = Label(text="*Calculated with Safe residual\n pressure of 200PSI ", size_hint=(0.3,0.1), pos_hint={'x':0.3, 'y':0.42},color=(.9,.9,.9,1),font_size=18)
                layoutHome.add_widget(lblres)
                
                #creating the dropdown list for convert to
                unitsDrop02 = DropDown()
                unitsList02 = ["D Cylinder",'Jumbo D','E Cylinder', 'M Cylinder', 'H Cylinder']
            
                #looping through the units           
                for i in unitsList02:
                    btnUnits02 = Button(text=i,size_hint_y=None, height=44,color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),font_size=18)#creating the buttons with parameters
                    btnUnits02.bind(on_release=lambda btnUnits02: unitsDrop02.select(btnUnits02.text))#binding the button to then set to its text 
                    unitsDrop02.add_widget(btnUnits02)#adding the buttons the the screen 
                    
                #creating the main button for 02 cylinder 
                btnSelect = Button(text='Tank Type',size_hint=(0.4,0.09), pos_hint={'x':0.48, 'y':0.82},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),font_size=18)
                btnSelect.bind(on_release=unitsDrop02.open)
                layoutHome.add_widget(btnSelect)
                unitsDrop02.bind(on_select=lambda instance, x: setattr(btnSelect, 'text',x))
                def o2Calc(self):
                    try:
                        lpm = float(entr02LPM.text)
                        psi = float(entrCurrpsi.text)
                            
                        dCylfact = 0.16 #D cylinder factor
                        jumboDnECylfact = 0.28 #jumboD and E cylinder factor
                        mCylfact = 1.56 #M cylinder factor
                        hCylfact = 3.14 #H cylinder factor 
                        saferes = 200 #safe residual pressure 
                        
                        if btnSelect.text == "Tank Type":
                            answer = "ERR CHK TANK"
                            entr02ans.text = str(answer)
                        if btnSelect.text == "Jumbo D" or btnSelect.text == "E Cylinder":
                            oxygenLeftTime = round(((psi-saferes)*jumboDnECylfact)/lpm,5)
                            entr02ans.text = str(oxygenLeftTime) 
                        if btnSelect.text == "D Cylinder":
                            oxygenTimeleft = round(((psi-saferes)*dCylfact)/lpm,5)
                            entr02ans.text = str(oxygenTimeleft)  
                        if btnSelect.text == "M Cylinder":
                            o2Time = round(((psi-saferes)*mCylfact)/lpm,5)
                            entr02ans.text = str(o2Time)
                        if btnSelect.text == "H Cylinder":
                            o2Timeh = round(((psi-saferes)*hCylfact)/lpm,5)
                            entr02ans.text = str(o2Timeh)
                    except:
                        answer = "ERROR"
                        entr02ans.text = str(answer)
                        
                def clearAll(self): #clearing all the text off the screen 
                    entrCurrpsi.text = ''
                    entr02LPM.text = ''
                    entr02ans.text =''
                 
                def returnHome(self):
                    clearScreen()
                    createHomePage(self)
                    
                btnClearAll = Button(text="Clear All",size_hint=(0.8,0.15), pos_hint={'x':0.13, 'y':0.17},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),
                                 background_down=('black'),font_size=18)#background_down to change on press background color 
                btnClearAll.bind(on_release=clearAll)
                layoutHome.add_widget(btnClearAll)
                    
                btnReturnHome = Button(text="Return to Home",size_hint=(0.4,0.1), pos_hint={'x':0.13, 'y':0.32},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),font_size=18)
                btnReturnHome.bind(on_press=returnHome)
                layoutHome.add_widget(btnReturnHome)
            
                btnCalculate = Button(text="Calculate",size_hint=(0.4,0.1), pos_hint={'x':0.53, 'y':0.32},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),font_size=18)
                btnCalculate.bind(on_press=o2Calc)#binding the button to 02 calc function 
                layoutHome.add_widget(btnCalculate)
                
            def burnFormula(self):
                
                clearScreen()
                lblBurnFormula = Label(text="Parkland Formula", size_hint=(0.3,0.1), pos_hint={'x':0.12, 'y':0.9},color=(.9,.9,.9,1),font_size=18)
                layoutHome.add_widget(lblBurnFormula)
                
                lblml = Label(text="ML: ", size_hint=(0.3,0.1), pos_hint={'x':0.25, 'y':0.82},color=(.9,.9,.9,1),font_size=18)
                layoutHome.add_widget(lblml)
                entrml = TextInput(size_hint=(0.4,0.09), pos_hint={'x':0.48, 'y':0.82}, multiline=False, disabled=True,font_size=20)
                entrml.text = str(4)#setting the default value for 4 for the parkland burn formula
                layoutHome.add_widget(entrml)
            
                lblTBSA = Label(text="TBSA(%) ", size_hint=(0.3,0.1), pos_hint={'x':0.23, 'y':0.75},color=(.9,.9,.9,1),font_size=18)
                layoutHome.add_widget(lblTBSA)
                entrTBSA = TextInput(size_hint=(0.4,0.09), pos_hint={'x':0.48, 'y':0.75}, multiline=False, cursor_color=(0,0,0,1),font_size=20)
                layoutHome.add_widget(entrTBSA)
            
                lblkg = Label(text="KG: ", size_hint=(0.3,0.1), pos_hint={'x':0.25, 'y':0.66},color=(.9,.9,.9,1),font_size=18)
                layoutHome.add_widget(lblkg)
                entrkg = TextInput(size_hint=(0.4,0.09), pos_hint={'x':0.48, 'y':0.66}, multiline=False, cursor_color=(0,0,0,1),font_size=20)
                layoutHome.add_widget(entrkg)
                
                lblDropFactor = Label(text="Drop Factor:", size_hint=(0.25,0.1), pos_hint={'x':0.22, 'y':0.57},color=(.9,.9,.9,1),font_size=18)
                layoutHome.add_widget(lblDropFactor)
                entrDropFact = TextInput(size_hint=(0.4,0.09), pos_hint={'x':0.48, 'y':0.57}, multiline=False, cursor_color=(0,0,0,1),font_size=20)
                layoutHome.add_widget(entrDropFact)
                
                lblburnAns = Label(text="(FIRST 8 HRS) \n        gtts/min ", size_hint=(0.25,0.1), pos_hint={'x':0.13, 'y':0.46},color=(.9,.9,.9,1),font_size=18)
                layoutHome.add_widget(lblburnAns)
                entrburnAns = TextInput(size_hint=(0.4,0.088), pos_hint={'x':0.48, 'y':0.48}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.91,0.91,0.031,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=24)#setbackground disabled to white first to avoid grey tint
                layoutHome.add_widget(entrburnAns)
                
                lblburnAns2 = Label(text="(NEXT 16 HRS) \n        gtts/min ", size_hint=(0.25,0.1), pos_hint={'x':0.13, 'y':0.38},color=(.9,.9,.9,1),font_size=18)
                layoutHome.add_widget(lblburnAns2)
                entrburnAns2 = TextInput(size_hint=(0.4,0.088), pos_hint={'x':0.48, 'y':0.39}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.91,0.91,0.031,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=20)#setbackground disabled to white first to avoid grey tint
                layoutHome.add_widget(entrburnAns2)
                
                lblburnTotal = Label(text="mL ovr 24HRS ", size_hint=(0.25,0.1), pos_hint={'x':0.13, 'y':0.30},color=(.9,.9,.9,1),font_size=18)
                layoutHome.add_widget(lblburnTotal)
                entrburnTotal = TextInput(size_hint=(0.4,0.088), pos_hint={'x':0.48, 'y':0.30}, multiline=False, disabled=True,#disabled sets text input to read only 
                                    background_disabled_normal='', background_color=(0.91,0.91,0.031,0.9),disabled_foreground_color=(0,0,0,1),
                                    font_size=20)#setbackground disabled to white first to avoid grey tint
                layoutHome.add_widget(entrburnTotal)
                
                #adding buttons to return to homescreen and calculate problem 
                def returnHome(self):
                    clearScreen()
                    createHomePage(self)
                def burnCalc(self):
                    try: 
                        burnml = 4.0
                        burnBSA= float(entrTBSA.text)
                        wt = float(entrkg.text)
                        fluidvol = burnml*burnBSA*wt
                        dropFactor = float(entrDropFact.text)
                         
                        first8 = (burnml*burnBSA*wt) #The first half of NS or LR is given over first 8 hours 
                        gttsFirst = round(first8*dropFactor/480,5)#480 is the amount of minutes in 8 hours for infusion problem 
                        entrburnAns.text = str(gttsFirst)
                        
                        gttsSecond = round(first8*dropFactor/960)#960 is the amount of minutes in 2nd 16 hours 
                        entrburnAns2.text = str(gttsSecond)
                         
                        total = burnml*burnBSA*wt
                        entrburnTotal.text = str(total)
                    except:
                        answer = "ERROR"
                        entrburnTotal.text = str(answer)
                        entrburnAns.text = str(answer)
                        entrburnAns2.text = str(answer)
                        
                def clearAll(self): #clearing all the text off the screen 
                    entrTBSA.text = '' 
                    entrkg.text = ''
                    entrburnAns.text = '' 
                    entrburnAns2.text = ''
                    entrburnTotal.text = '' 
                    entrDropFact.text = ''
                    
                        
                btnClearAll = Button(text="Clear All",size_hint=(0.8,0.125), pos_hint={'x':0.13, 'y':0.065},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),
                                 background_down=('black'),font_size=18)#background_down to change on press background color 
                btnClearAll.bind(on_release=clearAll)
                layoutHome.add_widget(btnClearAll)
                        
                btnCalculate = Button(text="Calculate",size_hint=(0.4,0.1), pos_hint={'x':0.53, 'y':0.19},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),font_size=18)
                btnCalculate.bind(on_press=burnCalc)
                layoutHome.add_widget(btnCalculate)
                
                btnReturnHome = Button(text="Return to Home",size_hint=(0.4,0.1), pos_hint={'x':0.13, 'y':0.19},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),font_size=18)
                btnReturnHome.bind(on_press=returnHome)
                layoutHome.add_widget(btnReturnHome)
                
            #-----------------END BURN FORMULA---------------------------------------------------------------
            #adding buttons to return to homescreen and calculate problem 
            def returnHome(self):
                clearScreen()
                createHomePage(self)
            
            btnReturnHome = Button(text="Return to Home",size_hint=(0.79,0.1), pos_hint={'x':0.07, 'y':0.1},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),font_size=18)
            btnReturnHome.bind(on_press=returnHome)
            layoutHome.add_widget(btnReturnHome)
            
            btnO2Tank = Button (text="O2 Time Calc", size_hint=(0.4,0.1),pos_hint={'x':0.07, 'y':0.2},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),font_size=18)
            btnO2Tank.bind(on_press=o2Tank)
            layoutHome.add_widget(btnO2Tank)
            
            btnO2Tank = Button (text="Burn Formula", size_hint=(0.4,0.1),pos_hint={'x':0.46, 'y':0.2},color=(.9,.9,.9,1),background_color=(.8,.8,.8,1),font_size=18)
            btnO2Tank.bind(on_press=burnFormula)
            layoutHome.add_widget(btnO2Tank)
            #----------------------------END FORMULAS FUNCTION 
#-------------------------------END FUNCTIONS-------------------------------------------------------------
        #adding actions to the buttons for disclaimer 
        btnYes.bind(on_press=pressYes)
        btnNo.bind(on_press=pressNo)        
        self.add_widget(layoutHome)#adding the innerlayout to the root
#------------END Big MODE------------------------------------------------------------------------
class medCalc(App): #building the application (night mode, default)
    def build(self):
        self.icon='D:\Python\pyImages\medCalcxiconnorm.ico' #adding the icon file 
        return medCalcNight()    
if __name__ == "__main__": #running the application 
    medCalc().run()
