def creating_and_viewing_html_files(html_template, console_print=False, browser_view=False):
    # import module 
    import codecs 

    # to open/create a new html file in the write mode 
    f = open('results/GFG.html', 'w', encoding="utf-8") # *1

    # the html code which will go in the file GFG.html 
    # html_template = """ 
    # <html> 
    # <head></head> 
    # <body> 
    # <p>Hello World! </p> 
    
    # </body> 
    # </html> 
    # """

    # writing the code into the file 
    f.write(html_template) 

    # close the file 
    f.close() 

    if console_print:
        # viewing html files 
        # below code creates a  
        # codecs.StreamReaderWriter object 
        file = codecs.open("results/GFG.html", 'r', "utf-8") 
        
        # using .read method to view the html  
        # code from our object 
        print(file.read()) 

    if browser_view:
        # import module 
        import webbrowser

        # open html file 
        webbrowser.open('results/GFG.html')

# + https://chat.openai.com/share/354de6cc-7aa2-4e57-ace3-1118da194d0e
def generate_alphabet_combinations(max_count):
    def generate_combinations_helper(prefix, remaining_count):
        if remaining_count == 0:
            print(prefix)
            return
        for char in range(ord('A'), ord('Z') + 1):
            generate_combinations_helper(prefix + chr(char), remaining_count - 1)
    
    generate_combinations_helper('', max_count)

# Example usage
# generate_alphabet_combinations(4)  # Generates all combinations up to 2 characters

# https://stackoverflow.com/questions/63664067/python-generate-an-alphanumeric-sequence/63664138#63664138
import string
import itertools

# TODO 
def custom_seq(pk, letter=4, digits=3):
    alpha = string.ascii_uppercase
    digit = string.digits
    alpha_list = [alpha]*letter
    digit_list = [digit]*digits
    for i in itertools.product(*alpha_list):
        for j in itertools.product(*digit_list):
            # yield "".join(i + j)
            print("".join(i + j))

# custom_seq(None, 26, 0)

# References          
# https://www.geeksforgeeks.org/creating-and-viewing-html-files-with-python/
# (*1) https://stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters/42495690#42495690