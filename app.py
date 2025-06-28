# June 2025 Nicholas Norman
import requests
import tkinter as tk
import api_requests

#This app will show books from the Gutenburg Press and allow for searching and exploring

def run_application():

    #tkinter
    root = tk.Tk()

    popup = creating_loading_popup(root)

    bookResults = api_requests.get_posts(1)

    page = 1

    load_page(root, page, bookResults)

    popup.destroy()

    root.mainloop()

def load_next_page(root, page, bookResults):

    popup = creating_loading_popup(root)

    page += 1

    for widget in root.winfo_children():
        if widget != popup:
            widget.destroy()
    
    bookResults = api_requests.get_next_page(bookResults['next'])

    load_page(root, page, bookResults)

    popup.destroy()

def creating_loading_popup(root):
    #popup
    popup = tk.Toplevel(root)
    popup.title("Loading...")
    popup.geometry("200x100")
    tk.Label(popup, text="loading").pack()
    popup.update()

    return popup

def load_page(root, page, bookResults):
    # labels
    pageNumber = tk.Label(root, text=page)
    bookLabels = []
    for book in bookResults['results']:
        bookLabels.append(tk.Label(root, text=book['title']))

    #buttons
    nextBtn = tk.Button(root, text='Next Page', command=lambda: load_next_page(root, page, bookResults))

    # formatting
    pageNumber.pack()
    for bookLabel in bookLabels:
        bookLabel.pack()
    nextBtn.pack()


if __name__ == "__main__":
    #run main application
    run_application()