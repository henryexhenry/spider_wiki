import tkinter as tk
import requests
from lxml import etree
import time
import random

class Node(object):
    def __init__(self, cat_, layer_):
        self.cat = cat_
        self.layer = layer_
        self.supcats = []
        
    def __repr__(self):
        return "Node: %s" % self.supcats
    
    def add_supcat(self, node):
        self.supcats.append(node) 
    
    def get_supcats(self):
        return self.supcats

class Application:
    def __init__(self, master = None):

        baseURL = 'https://en.wikipedia.org/wiki/Category:'
        HEIGHT = 500
        WIDTH = 600

        canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
        canvas.pack()

        #background_image = tk.PhotoImage(file='landscape.png')
        #background_label = tk.Label(root, image=background_image)
        #background_label.place(relwidth=1, relheight=1)

        frame = tk.Frame(root, bd=5)
        frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

        label = tk.Label(frame, font=40)
        label.place(relwidth=0.2, relheight=1)
        label['text'] = "Category: "
        entry = tk.Entry(frame, font=40)
        entry.place(relx = 0.2, relwidth=0.8, relheight=1)

        frame1 = tk.Frame(root, bd=5)
        frame1.place(relx=0.5, rely=0.2, relwidth=0.5, relheight=0.1, anchor='n')
        button = tk.Button(frame1, text="Get links", font=40, command=lambda: self.DFS(entry.get()))
        button.place(relx=0.3, relheight=0.8, relwidth=0.4)

        lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
        lower_frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.55, anchor='n')

        lower_frame1 = tk.Frame(root)
        lower_frame1.place(relx=0.5, rely=0.85, relwidth=0.75, relheight=0.1, anchor='n')
        self.label1 = tk.Label(lower_frame1, text='Total: ')
        self.label1.place(relwidth=0.2, relheight=1)

        self.text = tk.Text(lower_frame)
        self.text.place(relwidth=1, relheight=1)
        '''#TODO
                frame2 = tk.Frame(root, bd=5)
                frame2.place(relx = 0, rely=0.2, relwidth=0.5, relheight=0.1, anchor='n')
                r1 = tk.Radiobutton(frame2, text='BFS', variable=var, value='BFS')
                r1.place(relwidth = 0.5, relheight = 1)
                r2 = tk.Radiobutton(frame2, text='DFS', variable=var, value='DFS')
                r2.place(relwidth = 0.5, relheight = 1)
        '''
    # crawls all subcategories of a category
    def spider___(self, cat, l, dict_): # -> [subcategoris]

        cur = Node(cat, l)

        bound_subcats = 3
        bound_layer = 3        # set boundary
        

        # *******************   connect wiki   *************************

        time.sleep(random.random()*2)

        print('Connecting.....................')
        req = requests.get('https://en.wikipedia.org/wiki/Category:' + cat)
        print('Connected......................')
        html = etree.HTML(req.text)

        # if element has more than one classes, use contains()
        print('crawling         ################')



        # *******************   Crawling content   *************************
        '''
        with open('data/'+cat+'.txt', 'w') as f:
            for i in html.xpath("//div[@id='content']//text()"):
                try:
                    f.write(i)
                except:
                    pass
        '''
        if l >= bound_layer:         # set boundary
            return cur


        # *******************   Crawling subcategories   *************************
        for j, i in enumerate(html.xpath("//a[contains(@class, 'CategoryTreeLabelCategory')]/text()")):
            
            if j < bound_subcats:
            
                if i not in dict_:          # check duplicate

                    dict_[i] = 1
                    cur.supcats.append(Node(i, l+1))

        print('crawled          #################')

        return cur




    def DFS(self, cat):
        print('DFSing..............................')
        self.text.insert(tk.END, cat + '\n')

        DICT = {}

        head = self.spider___(cat, 0, DICT)
        node = head
        stack = []
        count = 1

        while node.supcats or stack:
            while node.supcats:

                stack += node.supcats[1:][::-1]

                if node.supcats[0:1]:
                    print(node.supcats)

                    node = node.supcats[0]
                    self.text.insert(tk.END, (node.layer) * '  ' + node.cat + '\n')
                    count += 1
                    print('layer: ', node.layer)

                    node = self.spider___(node.cat, node.layer, DICT)

            s = stack.pop()
            self.text.insert(tk.END, (s.layer) * '  ' + s.cat + '\n')
            count += 1

            node = self.spider___(s.cat, s.layer, DICT)

            
        print('DFS end !')

        self.label1['text'] = 'Total: '
        self.label1['text'] += str(count)




root = tk.Tk()

app = Application(master = root)
root.mainloop()