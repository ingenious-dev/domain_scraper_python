from utility import creating_and_viewing_html_files

import requests
from bs4 import BeautifulSoup

from scrape_hostpinnacle import scrape_hostpinnacle_for_domains
from scrape_kenyawebexperts import scrape_kenyawebexperts_for_domains
from scrape_truehost import scrape_truehost_for_domains

selections = []
def build_ui():
    def print_selection():
        global selections
        selections = []

        text = ''
        if (var1.get() == 1):
            selections.append('hostpinnacle')
            text += 'Hostpinnacle, '

        if (var2.get() == 1):
            selections.append('kenyawebexperts')
            text += 'Kenya Web Experts, '

        if (var3.get() == 1):
            selections.append('truehost')
            text += 'Truehost '

        if text:
            l.config(text=f'Seach in {text}')
        else:
            l.config(text='No selection')

    def run():
        # window.destroy() # *3
        b.destroy()

        import threading

        x = threading.Thread(target=run_search, args=(l,))
        x.start()
    
    import tkinter as tk
 
    window = tk.Tk()
    window.title('Domain Scraper')
    window.geometry('300x200')
    
    l = tk.Label(window,
        bg='white',
        # width=20,
        text='No selection'
    )
    l.pack()
    
    var1 = tk.IntVar()
    var2 = tk.IntVar()
    var3 = tk.IntVar()
    c1 = tk.Checkbutton(window, text='Hostpinnacle',variable=var1, onvalue=1, offvalue=0, command=print_selection)
    c1.pack()
    c2 = tk.Checkbutton(window, text='Kenya Web Experts',variable=var2, onvalue=1, offvalue=0, command=print_selection)
    c2.pack()
    c3 = tk.Checkbutton(window, text='Truehost',variable=var3, onvalue=1, offvalue=0, command=print_selection)
    c3.pack()

    b = tk.Button(window, text='Submit', width=20, bg='brown', fg='white', command=run ) # *1, *2
    b.pack()
    
    window.mainloop()

def run_search(label):
    if not selections:
        print('No Selection Made')
        return
    
    import time
    
    import xlwt

    book = xlwt.Workbook()

    # lookup_domains = ['test.com']
    label.config(text='Checking domains.txt')
    print('Checking domains.txt')
    domains_file = open('domains.txt')
    lookup_domains = [ x.replace('\n', '') for x in domains_file.readlines()]
    # print(lookup_domains)

    if "hostpinnacle" in selections:
        t = time.process_time()
        label.config(text='Please wait. Searching HOSTPINNACLE')
        print('* * * * HOSTPINNACLE * * * *')
        sh = book.add_sheet('Hostpinnacle')
        row_index = 0
        sh.write(row_index, 0, 'Domain')
        sh.write(row_index, 1, 'Status')
        sh.write(row_index, 2, 'Registration')
        sh.write(row_index, 3, 'Transfer')
        sh.write(row_index, 4, 'Renew')
        row_index += 1

        for domain in lookup_domains:
            results = scrape_hostpinnacle_for_domains(domain)
            for result in results:
                sh.write(row_index, 0, result.get('domainName'))
                sh.write(row_index, 1, 'AVAILABLE' if result.get('isAvailable') else '-')
                sh.write(row_index, 2, result.get('pricing').get('1').get('register'))
                sh.write(row_index, 3, result.get('pricing').get('1').get('transfer'))
                sh.write(row_index, 4, result.get('pricing').get('1').get('renew'))
                row_index += 1

        elapsed_time = time.process_time() - t
        print(f"{elapsed_time} Sec")

    if "kenyawebexperts" in selections:
        t = time.process_time()
        label.config(text='Please wait. Searching KENYA WEB EXPERTS')
        print('* * * * KENYA WEB EXPERTS * * * *')
        sh = book.add_sheet('Kenya Web Experts')
        row_index = 0
        sh.write(row_index, 0, 'Domain')
        sh.write(row_index, 1, 'Status')
        sh.write(row_index, 2, 'Registration')
        sh.write(row_index, 3, 'Transfer')
        sh.write(row_index, 4, 'Renew')
        row_index += 1

        for domain in lookup_domains:
            results = scrape_kenyawebexperts_for_domains(domain)
            for result in results:
                sh.write(row_index, 0, result.get('domainName'))
                sh.write(row_index, 1, 'AVAILABLE' if result.get('isAvailable') else '-')
                sh.write(row_index, 2, result.get('pricing').get('1').get('register'))
                sh.write(row_index, 3, result.get('pricing').get('1').get('transfer'))
                sh.write(row_index, 4, result.get('pricing').get('1').get('renew'))
                row_index += 1

        elapsed_time = time.process_time() - t
        print(f"{elapsed_time} Sec")

    if "truehost" in selections:
        t = time.process_time()
        label.config(text='Please wait. Searching TRUEHOST')
        print('* * * * TRUEHOST * * * *')
        sh = book.add_sheet('Truehost')
        row_index = 0
        sh.write(row_index, 0, 'Domain')
        sh.write(row_index, 1, 'Status')
        sh.write(row_index, 2, 'Registration')
        sh.write(row_index, 3, 'Transfer')
        sh.write(row_index, 4, 'Renew')
        row_index += 1

        for domain in lookup_domains:
            results = scrape_truehost_for_domains(domain)
            for result in results:
                sh.write(row_index, 0, result.get('domainName'))
                sh.write(row_index, 1, 'AVAILABLE' if result.get('isAvailable') else '-')
                sh.write(row_index, 2, result.get('pricing').get('1').get('register'))
                sh.write(row_index, 3, result.get('pricing').get('1').get('transfer'))
                sh.write(row_index, 4, result.get('pricing').get('1').get('renew'))
                row_index += 1

        elapsed_time = time.process_time() - t
        print(f"{elapsed_time} Sec")

    book.save('results/domains.xls')
    label.config(text='Completed. See results/domains.xls for results')
    print('Completed. See results/domains.xls for results')

if __name__ == "__main__":
    build_ui()

# References
# https://pythonbasics.org/tkinter-checkbox/
# https://www.javatpoint.com/simple-registration-form-using-tkinter-in-python (*1)
# https://www.tutorialspoint.com/python/tk_button.htm (*2)
# https://stackoverflow.com/questions/110923/how-do-i-close-a-tkinter-window/15577605#15577605 (*3)
# https://stackoverflow.com/questions/7370801/how-do-i-measure-elapsed-time-in-python/21455138#21455138
# https://realpython.com/intro-to-python-threading/
