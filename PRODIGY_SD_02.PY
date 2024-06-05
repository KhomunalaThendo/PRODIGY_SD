#Guessing game
import customtkinter
import random



root = customtkinter.CTk()
root.title("Number Guess")
root.geometry("400x300")

number = random.randint(1,100)


def results():
 
 guess = int(guess_entry.get())

 if guess < number:
        result_label.configure(text="Guess Higher")
 elif guess > number:
        result_label.configure(text="Guess Lower")
 else:
        result_label.configure(text="Correct! You guessed the number!")

wlcm_label = customtkinter.CTkLabel(root, text="Guess Number")
wlcm_label.pack(pady = 10)

guess_entry = customtkinter.CTkEntry(root, placeholder_text="Enter Numer")
guess_entry.pack(pady = 10)

submit_btn = customtkinter.CTkButton(master=root, text= "Submit", command=results)
submit_btn.pack(pady = 10)

result_label = customtkinter.CTkLabel(root, text="")
result_label.pack(pady = 10)

root.mainloop()