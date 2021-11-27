from tkinter import *
from tkinter import filedialog
from plota import *


'''if __name__=="__main__":
    root = Tk()
    root.title('Plota app')'''

class Window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("Plota App")
        self.pack(fill=BOTH,expand=1)

        getfilepath = Button(self,text='choose a dataset to plot',
                             command=self.getLocalFile)
        getfilepath.pack()

        csvread = Button(self,text='read csv',
                             command=self.readcsv)
        csvread.pack()
        
        plotgraph = Button(self,text='plot the graph',
                             command=self.plotcsv)
        plotgraph.pack()

    def getLocalFile(self):
        root = Tk()
        root.withdraw()

        global filepath
        filepath = filedialog.askopenfilename()

        print('A file path detected')
        return filepath

        if __name__ == '__main__':
            getLocalFile()
            
    def readcsv(self):
        try:
            x,y = np.loadtxt(filepath, unpack=True, delimiter=",")
            return x,y
            
            if __name__ == '__main__':
                readcsv()
        except Exception as e:
                print(e)
                print('''
                        ====================================
                        Check to see that your dataset is two
                        dimensional and is comma separated
                        ====================================
                        ''')

    def plotcsv(self):
        try:
            x,y = readcsv(filepath)
            corr = np.correlate(x,y)#finds the correlation between x and y

            print('The correlation between x and y is:', corr)
            
            plt.scatter(x,y) #plots the scatter plot of x and y
            plt.xlabel('x-axis')
            plt.ylabel('y-axis')
            plt.show()
        except Exception as e:
            print(e)

root = Tk()
app = Window(root)
root.mainloop()
