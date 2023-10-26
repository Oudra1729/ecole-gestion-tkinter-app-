import tkinter as tk
from tkinter import messagebox
from Classes import *
from Functions import *
from datetime import date

# Create a Tkinter window
window = tk.Tk()
window.title("Stagiaire Application")

# Create a list to store the Stagiaire objects
List_Attend = []

# Create the Stagiaire objects
S1 = Stagaire("PA2215", 1, "Ait El Kamel", "Ismael", date(1998, 8, 23), ListFiliere, 11.66)
S2 = Stagaire("PA2245", 1, "Oudra", "Brahim", date(1999, 6, 15), ListFiliere, 11.58)
S3 = Stagaire("PA2875", 2, "Aassab", "Hiba", date(2002, 6, 26), ListFiliere, 14.74)
S4 = Stagaire("PA2645", 1, "Er-Rachedy", "Yassine", date(2000, 10, 16), ListFiliere, 14.98)
S5 = Stagaire("PA2240", 2, "Ait Lhassan", "Ayoub", date(2004, 8, 20), ListFiliere, 14.42)
List_Attend.append(S1)
List_Attend.append(S2)
List_Attend.append(S3)
List_Attend.append(S4)
List_Attend.append(S5)

# File names
file_Drctr = "Directure.csv"
file_Frmtr = "AuthFormateurs.csv"
file_Sstgr = "AuthStagaires.csv"

# Function to handle the "Directeur" button click
def directeur():
    user = entry_user.get()
    password = entry_password.get()

    # Check if the user and password are valid
    if confirmeUtl(user, password, file_Drctr):
        directeur_window = tk.Toplevel(window)
        directeur_window.title("Directeur Menu")
        directeur_label = tk.Label(directeur_window, text="Menu Directeur", font=("Arial", 16, "bold"))
        directeur_label.pack()

        def ajouter_filiere():
            # Implement the logic to add a new filière
            messagebox.showinfo("Ajouter Filière", "Filière ajoutée avec succès!")

        def ajouter_stagiaire():
            # Implement the logic to add a new stagiaire
            messagebox.showinfo("Ajouter Stagiaire", "Stagiaire ajouté avec succès!")

        def ajouter_formateur():
            # Implement the logic to add a new formateur
            messagebox.showinfo("Ajouter Formateur", "Formateur ajouté avec succès!")

        def afficher_stagiaires():
            # Implement the logic to display the list of stagiaires
            messagebox.showinfo("Afficher Stagiaires", "Liste des stagiaires affichée!")

        def afficher_formateurs():
            # Implement the logic to display the list of formateurs
            messagebox.showinfo("Afficher Formateurs", "Liste des formateurs affichée!")

        def supprimer_stagiaire():
            # Implement the logic to delete a stagiaire
            messagebox.showinfo("Supprimer Stagiaire", "Stagiaire supprimé avec succès!")

        def supprimer_formateur():
            # Implement the logic to delete a formateur
            messagebox.showinfo("Supprimer Formateur", "Formateur supprimé avec succès!")

        def afficher_notes():
            # Implement the logic to display the notes
            messagebox.showinfo("Afficher Notes", "Notes affichées!")

        def close_directeur_window():
            directeur_window.destroy()

        ajouter_filiere_button = tk.Button(directeur_window, text="Ajouter Filière", command=ajouter_filiere)
        ajouter_filiere_button.pack()

        ajouter_stagiaire_button = tk.Button(directeur_window, text="Ajouter Stagiaire", command=ajouter_stagiaire)
        ajouter_stagiaire_button.pack()

        ajouter_formateur_button = tk.Button(directeur_window, text="Ajouter Formateur", command=ajouter_formateur)
        ajouter_formateur_button.pack()

        afficher_stagiaires_button = tk.Button(directeur_window, text="Afficher Stagiaires", command=afficher_stagiaires)
        afficher_stagiaires_button.pack()

        afficher_formateurs_button = tk.Button(directeur_window, text="Afficher Formateurs", command=afficher_formateurs)
        afficher_formateurs_button.pack()

        supprimer_stagiaire_button = tk.Button(directeur_window, text="Supprimer Stagiaire", command=supprimer_stagiaire)
        supprimer_stagiaire_button.pack()

        supprimer_formateur_button = tk.Button(directeur_window, text="Supprimer Formateur", command=supprimer_formateur)
        supprimer_formateur_button.pack()

        afficher_notes_button = tk.Button(directeur_window, text="Afficher Notes", command=afficher_notes)
        afficher_notes_button.pack()

        close_directeur_window_button = tk.Button(directeur_window, text="Fermer", command=close_directeur_window)
        close_directeur_window_button.pack()

    else:
        messagebox.showerror("Erreur", "Nom d'utilisateur ou mot de passe invalide!")

# Function to handle the "Stagiaire" button click
def stagiaire():
    cin = entry_cin.get()
    password = entry_password.get()

    # Check if the cin and password are valid
    if confirmeUtl(cin, password, file_Sstgr):
        stagiaire_window = tk.Toplevel(window)
        stagiaire_window.title("Stagiaire Menu")
        stagiaire_label = tk.Label(stagiaire_window, text="Menu Stagiaire", font=("Arial", 16, "bold"))
        stagiaire_label.pack()

        def voir_mes_notes():
            # Implement the logic to display the stagiaire's notes
            messagebox.showinfo("Voir Mes Notes", "Vos notes sont affichées!")

        def close_stagiaire_window():
            stagiaire_window.destroy()

        voir_mes_notes_button = tk.Button(stagiaire_window, text="Voir Mes Notes", command=voir_mes_notes)
        voir_mes_notes_button.pack()

        close_stagiaire_window_button = tk.Button(stagiaire_window, text="Fermer", command=close_stagiaire_window)
        close_stagiaire_window_button.pack()

    else:
        messagebox.showerror("Erreur", "CIN ou mot de passe invalide!")

# Create the labels and entry fields
user_label = tk.Label(window, text="Nom d'utilisateur:")
user_label.pack()
entry_user = tk.Entry(window)
entry_user.pack()

cin_label = tk.Label(window, text="CIN:")
cin_label.pack()
entry_cin = tk.Entry(window)
entry_cin.pack()

password_label = tk.Label(window, text="Mot de passe:")
password_label.pack()
entry_password = tk.Entry(window, show="*")
entry_password.pack()

# Create the buttons
directeur_button = tk.Button(window, text="Directeur", command=directeur)
directeur_button.pack()

stagiaire_button = tk.Button(window, text="Stagiaire", command=stagiaire)
stagiaire_button.pack()

# Run the Tkinter event loop
window.mainloop()
