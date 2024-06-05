#Guessing game
import customtkinter
import random



root = customtkinter.CTk()
root.title("Number Guess")
root.geometry("400x300")


def results():
 
  guess = int(guess_entry.get())
  difficulty = options.get()

  if difficulty == "Easy":
        number = random.randint(1, 20)
        max_limit = 20
  elif difficulty == "Medium":
        number = random.randint(1, 50)
        max_limit = 50
  elif difficulty == "Hard":
        number = random.randint(1, 100)
        max_limit = 100

  if guess > max_limit:
        result_label.configure(text="Your guess is above the difficulty level range.")
  elif guess < number:
         result_label.configure(text="Guess Higher")
  elif guess > number:
        result_label.configure(text="Guess Lower")
  else:
        result_label.configure(text="Correct! You guessed the number!")


dificcult_lbl = customtkinter.CTkLabel(root, text="Choose Difficulty")
dificcult_lbl.pack(pady = 10)


options = customtkinter.CTkOptionMenu(master=root, values=["Easy","Medium","Hard"])
options.set("Easy")
options.pack(pady = 10)

wlcm_label = customtkinter.CTkLabel(root, text="Guess Number")
wlcm_label.pack(pady = 10)

guess_entry = customtkinter.CTkEntry(root, placeholder_text="Enter Numer")
guess_entry.pack(pady = 10)

submit_btn = customtkinter.CTkButton(master=root, text= "Submit", command=results)
submit_btn.pack(pady = 10)

result_label = customtkinter.CTkLabel(root, text="")
result_label.pack(pady = 10)

root.mainloop()
