from matplotlib import pyplot as plt
from tkinter import filedialog
from PIL import Image


class ImageCoordScanner:
    def __init__(self, file, printer):
        """display an image and send x,y,xx,yy data when you click on it"""
        plt.title("Image à scanner")
        plt.xlabel("X pixel scaling")
        plt.ylabel("Y pixels scaling")

        self.callback = printer.new_record
        self.x = 0
        self.y = 0

        ax = plt.gca()
        fig = plt.gcf()

        cid = fig.canvas.mpl_connect('button_press_event', self.onclick)

        image = Image.open(file)
        ax.imshow(image)

        fig = plt.gcf()
        cid = fig.canvas.mpl_connect('button_press_event', self.onclick)
        fig.canvas.mpl_connect('button_release_event', self.onrelease)

        plt.show()
        printer.finish()


    def onclick(self, event):
        self.x = event.xdata
        self.y = event.ydata

    def onrelease(self, event):
        self.callback(self.x, self.y, event.xdata-self.x, event.ydata-self.y)
