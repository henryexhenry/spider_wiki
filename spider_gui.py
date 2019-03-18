import tkinter as tk
import requests
from bs4 import BeautifulSoup

class Application:
    def __init__(self, master = None):

        HEIGHT = 500
        WIDTH = 600
        var = 'BFS'

        canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
        canvas.pack()

        #background_image = tk.PhotoImage(file='landscape.png')
        #background_label = tk.Label(root, image=background_image)
        #background_label.place(relwidth=1, relheight=1)

        frame = tk.Frame(root, bd=5)
        frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

        label = tk.Label(frame, font=40)
        label.place(relwidth=0.2, relheight=1)
        label['text'] = "Url: "
        entry = tk.Entry(frame, font=40)
        entry.place(relx = 0.2, relwidth=0.8, relheight=1)

        frame1 = tk.Frame(root, bd=5)
        frame1.place(relx=0.5, rely=0.2, relwidth=0.5, relheight=0.1, anchor='n')
        button = tk.Button(frame1, text="Get links", font=40, command=lambda: self.spider(entry.get(), var))
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
    def spider(self, L, var):

        req = requests.get(L)
        soup = BeautifulSoup(req.text, "html.parser")
            
        if var == 'BFS':

            count = 0
            for i in soup.body.find_all('a', {'class':'CategoryTreeLabelCategory'}):
                try:
                    self.text.insert(tk.END, i['href'] + '\n')
                    count += 1
                except(KeyError):
                    print('KeyError')
            self.label1['text'] += str(count)

        # elif var == 'DFS':
'''#TODO

    # Crawl the page and populate the queue with newly found URLs
    def crawl(L):

        if len(queue) > 999 :
            return

        if L in visited:
            continue
        else:
            visited[url] = 1

            req = requests.get(L)
            soup = BeautifulSoup(req.text, "html.parser")
            urls = soup.findAll("a", {'class':'CategoryTreeLabelCategory'})
        for i in urls:
            flag = 0
            # Complete relative URLs and strip trailing slash
            complete_url = urljoin(url, i["href"]).rstrip('/')

            # Check if the URL already exists in the queue
            for j in queue:
                if j == complete_url:
                    flag = 1
                    break

            # If not found in queue
            if flag == 0:
                if len(queue) > 99:
                    return
                if (visited_list.count(complete_url)) == 0:
                    queue.append(complete_url)

        # Pop one URL from the queue from the left side so that it can be crawled
        current = queue.popleft()
        # Recursive call to crawl until the queue is populated with 100 URLs
        crawl(current)
'''

root = tk.Tk()

app = Application(master = root)
root.mainloop()