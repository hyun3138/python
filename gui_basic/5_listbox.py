from tkinter import *

root = Tk()
root.title("GUI")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "apple")
listbox.insert(1, "strawberry")
listbox.insert(2, "banana")
listbox.insert(END, "watermelon")
listbox.insert(END, "grape")
listbox.pack()

def btncmd():
    # 삭제
    # listbox.delete(0) # 맨 앞 항목을 삭제

    # 갯수 확인
    # print("list : {0}".format(listbox.size()))

    # 항목 확인 (시작 idx, 끝 idx)
    print("1~3 : {0}".format(listbox.get(0, 2)))

    # 선택된 항목 확인 (위치로 반환 (ex) (1, 2, 3)) 
    print("selected : {0}".format(listbox.curselection()))

btn = Button(root, text="click", command=btncmd)
btn.pack()

root.mainloop()