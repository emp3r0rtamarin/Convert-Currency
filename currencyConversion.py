import tkinter as tk
import tkinter.messagebox
import requests

def makeRequest(url):
    url = str(url)
    response = requests.get(url)
    content = response.json()
    return content

class currencyConversion:

    def createWindow(self,title,window_size):
        self.root_window = tk.Tk()
        self.root_window.geometry(window_size)
        self.root_window.title(title)

        # radiobuttons
        self.rad_btn_var = tk.IntVar()
        
        rad_btn_usd = tk.Radiobutton(self.root_window, text = "USD to TRY",
        variable=self.rad_btn_var, value = 1)
        rad_btn_usd.pack()

        rad_btn_try = tk.Radiobutton(self.root_window, text = "TRY to USD",
        variable=self.rad_btn_var, value = 2)
        rad_btn_try.pack()
        #---

        # entry
        self.entry_value = tk.StringVar()

        entry = tk.Entry(self.root_window,textvariable = self.entry_value) 
        entry.pack()
        convert_button = tk.Button(self.root_window, text="Convert",
        command = self.download)
        convert_button.pack()

   

    def download(self):
        try:
            requested_value = int(self.entry_value.get())
            print(requested_value)
        except ValueError :
            tk.messagebox.showerror(title="Error",message="Error : Please Enter an Integer Value.")

        try:
            if self.rad_btn_var.get() == 1:
                url = "https://api.exchangeratesapi.io/latest?base=USD&symbols=USD,TRY"
                content = makeRequest(url)               
                one_dollar = content['rates']['TRY']
                final_value = requested_value * one_dollar
                final_value = "{:.2f}".format(final_value)
                tk.messagebox.showinfo(title="Result",message="{}$ is {}TL ".format(requested_value,final_value))

            elif self.rad_btn_var.get() == 2:
                url = "https://api.exchangeratesapi.io/latest?base=TRY&symbols=TRY,USD"
                content = makeRequest(url)
                one_try = content['rates']['USD']
                final_value = requested_value * one_try
                final_value = "{:.2f}".format(final_value)
                tk.messagebox.showinfo(title="Result",message="{}TL is {}$ ".format(requested_value,final_value))

            else:
                tk.messagebox.showerror(title="Error",message="Error : Please Select One Of The Radiobuttons.")
            
        except requests.exceptions.RequestException:
            tk.messagebox.showerror(title="Error",message="Error : Connection Failed.")
        

    def initialize(self):
        self.root_window.mainloop()
        


        