import tkinter as tk


large_font_style=("Arial",40)
small_font_style=("Arial",16)
light_gray="#F5F5f5"
label_color="#25265E"
digit_font_style=("Arial",25,"bold")
light_blue="#CCEDFF"
default_font_styles=("Arial",20)
off_white="#F8FAFF"
white="#FFFFFF"


class calculator:
    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("calculator")
        
        self.total_expression =""
        self.current_expression=""

#creating frames
        self.display_frame =self.create_display_frame()
       
        

        self.buttons_frame=self.create_buttons_frame()
        self.digits={
            7:(1,1),8:(1,2),9:(1,3),
            4:(2,1),5:(2,2),6:(2,3),
            1:(3,1),2:(3,2),3:(3,3),
            0:(4,2),'.':(4,1)
        }
        self.create_digit_buttons()

        #..........code to make buttons fit into full screen ......... 
        self.buttons_frame.rowconfigure(0,weight=1)
        for x in range(1,5):
            self.buttons_frame.rowconfigure(x,weight=1)
            self.buttons_frame.columnconfigure(x,weight=1)


        self.operators={"/": "\u00f7","*":"\u00D7","-":"-","+":"+" }
        self.create_operators_buttons()
        self.special_buttons()

#creating labels
        self.total_lables,self.lables =self.create_display_labels()

       


  



   

    #......calling clear and equal buttons....................
    def special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_square_root_button()
        self.bind_keys()


    def bind_keys(self):
        self.window.bind("<Return>",lambda event:self.evaluate())
        for key in self.digits:
            self.window.bind(str(key),lambda event,digit=key: self.add_to_expression(digit))
        for key in self.operators:
            self.window.bind(key, lambda event,operator=key: self.append_operators(operator))
    #..........LABLES...............
    def create_display_labels(self):
        total_labels=tk.Label(self.display_frame,text=self.total_expression,anchor=tk.E,bg=light_gray,fg=label_color,padx=24,font=small_font_style)
        total_labels.pack(expand=True,fill="both")
       

        labels=tk.Label(self.display_frame,text=self.current_expression,anchor=tk.E,bg=light_gray,fg=label_color,padx=24,font=large_font_style)
        labels.pack(expand=True,fill="both")

        return total_labels,labels
    
    
    #.............FRAMES..............
    def create_display_frame(self):
        frame=tk.Frame(self.window,height=221,bg=light_gray)
        frame.pack(expand=True,fill="both")
        return frame

    def create_buttons_frame(self):
        frame=tk.Frame(self.window)
        frame.pack(expand=True,fill="both")
        return frame
    
    
    #.........adding current_expression to total expression..............

    def add_to_expression(self,value):
        self.current_expression+=str(value)
        self.update_lablel()

    #.........creating digit buttons...........
    def create_digit_buttons(self):
        for digit,grid_value in self.digits.items():
            button=tk.Button(self.buttons_frame,text=str(digit),bg=white,fg=label_color,font=digit_font_style,borderwidth=0,command=lambda x=digit:self.add_to_expression(x))
            button.grid(row=grid_value[0],column=grid_value[1],sticky=tk.NSEW)




    def append_operators(self,operater):
        self.current_expression += operater
        self.total_expression += self.current_expression
        self.current_expression = ""
        self.update_total_label()
        self.update_lablel()

    #........creating operators buttons.............
    def create_operators_buttons(self):
        i=0
        for operater,symbol in self.operators.items():
            button=tk.Button(self.buttons_frame,text=symbol,bg=off_white,fg=label_color,font=default_font_styles,borderwidth=0,command= lambda x=operater:self.append_operators(x))
            button.grid(row=i,column=4,sticky=tk.NSEW)
            i+=1

    #..........function of clear button.............
    def clear(self):
        self.total_expression=""
        self.current_expression=""
        self.update_total_label()
        self.update_lablel()
    
    #............creating clear button..............
    def create_clear_button(self):
        button=tk.Button(self.buttons_frame,text="CE",bg=off_white,fg=label_color,font=default_font_styles,borderwidth=0,command=self.clear)
        button.grid(row=0,column=1,sticky=tk.NSEW)
    
    #..........function of square button............
    def square(self):
        self.current_expression=str(eval(f"{self.current_expression}**2"))
        self.update_lablel()
    def create_square_button(self):
        button=tk.Button(self.buttons_frame,text="x\u00b2",bg=off_white,fg=label_color,font=default_font_styles,borderwidth=0,command=self.square)
        button.grid(row=0,column=2,sticky=tk.NSEW)

    #..........function of square root button............
    def sqrt(self):
        self.current_expression=str(eval(f"{self.current_expression}**0.5"))
        self.update_lablel()

    def create_square_root_button(self):
        button=tk.Button(self.buttons_frame,text="\u221ax",bg=off_white,fg=label_color,font=default_font_styles,borderwidth=0,command=self.sqrt)
        button.grid(row=0,column=3,sticky=tk.NSEW)

    

    #.......function of equals button..............
    def evaluate(self):
        self.total_expression+=self.current_expression
        self.update_total_label()
        try:
            self.current_expression=str(eval(self.total_expression))

            self.total_expression=""
        except Exception as e:
           self.current_expression="Error"
        finally:
           self.update_lablel()
    #.............creating  equal button................   
    def create_equals_button(self):
        button=tk.Button(self.buttons_frame,text="=",bg=light_blue,fg=label_color,font=default_font_styles,borderwidth=0,command=self.evaluate)
        button.grid(row=4,column=3,columnspan=2,sticky=tk.NSEW)




    #.......upadating total and current expressions lables.............

    def update_total_label(self):
        #changing symbols of operators
        expression=self.total_expression
        for operator,symbol in self.operators.items():
            expression=expression.replace(operator,f'{symbol}')
        self.total_lables.config(text=expression)
    
    def update_lablel(self):
        self.lables.config(text=self.current_expression[:11])

    def run(self):
        self.window.mainloop()


if __name__=="__main__":
    calc=calculator()
    calc.run()