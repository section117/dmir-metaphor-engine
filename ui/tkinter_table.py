import tkinter as tk
from tkinter import ttk


def get_search_results_table(rows):
    root = tk.Tk()
    root.title('Search Results')
    table = ttk.Treeview(root, columns=('poem_name', 'poet', 'published_year', 'metaphor_line', 'metaphor_terms',
                                        'source_domain', 'target_domain', 'interpretation'), show='headings', height=50)

    style = ttk.Style()
    style.configure("Treeview", font=('Iskoola Pota', 12))
    style.configure('Treeview', rowheight=30)

    table.heading("#1", text="Poem Name")
    table.heading("#2", text="Poet")
    table.heading("#3", text="Published Year")
    table.heading("#4", text="Metaphor")
    table.heading("#5", text="Metaphorical Terms")
    table.heading("#6", text="Source Domain")
    table.heading("#7", text="Target Domain")
    table.heading("#8", text="Interpretation")

    for row in rows:
        table.insert('', 'end', values=row)

    table.pack()
    # table.column('#3', width=70)
    return root
