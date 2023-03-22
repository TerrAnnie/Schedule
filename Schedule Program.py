#code by TerrAnnie Scott
import tkinter as tk
#fg=foreground
#bg=background
#in order to use insert you must add insert(index, str)
window = tk.Tk()#create a windo

frm_top = tk.Frame(master = window, bg = "light pink", width = 400, height = 300)
btn_top = tk.Button(master = frm_top, width = 10, height = 5, text = "Add a task", bg = "light pink")

txt_top = tk.Label(master = frm_top, text = "Welcome to your to do list TerrAnnie", fg = "black", bg = "light pink")
frame = tk.Frame(master = window, bg = "pink", width = 400, height = 400)
txt_top.pack()
btn_top.pack()
frm_top.pack(fill = tk.BOTH, expand = True,side = tk.LEFT)
frame.pack(fill = tk.BOTH, expand = True, side = tk.RIGHT)





window.mainloop()


