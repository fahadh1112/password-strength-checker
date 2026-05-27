import re
import math
import customtkinter as ctk


# APP SETTINGS

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


# CREATE WINDOW
app = ctk.CTk()

app.geometry("700x700")

app.title("Password Strength Checker")

app.resizable(False, False)


# TITLE

title_label = ctk.CTkLabel(
    app,
    text="🔐 Password Strength Checker",
    font=("Arial", 30, "bold")
)

title_label.pack(pady=(30, 10))

subtitle_label = ctk.CTkLabel(
    app,
    text="Analyze password security strength",
    font=("Arial", 15),
    text_color="gray"
)

subtitle_label.pack(pady=(0, 20))

# INPUT FRAME

input_frame = ctk.CTkFrame(
    app,
    width=500,
    corner_radius=15
)

input_frame.pack(pady=20)

# PASSWORD ENTRY

password_entry = ctk.CTkEntry(
    input_frame,
    width=400,
    height=50,
    placeholder_text="Enter your password",
    show="*",
    font=("Arial", 16),
    corner_radius=10
)

password_entry.pack(pady=(25, 15))

# SHOW / HIDE PASSWORD


show_password = False


def toggle_password():

    global show_password

    if show_password:
        password_entry.configure(show="*")
        show_password = False
        show_button.configure(text="👁 Show Password")

    else:
        password_entry.configure(show="")
        show_password = True
        show_button.configure(text="🙈 Hide Password")


show_button = ctk.CTkButton(
    input_frame,
    text="👁 Show Password",
    command=toggle_password,
    width=180,
    height=40,
    corner_radius=10
)

show_button.pack(pady=(0, 20))


# PROGRESS BAR


progress = ctk.CTkProgressBar(
    app,
    width=450,
    height=22,
    corner_radius=20
)

progress.pack(pady=(20, 10))

progress.set(0)


# STRENGTH LABEL


strength_label = ctk.CTkLabel(
    app,
    text="Password Strength: 0%",
    font=("Arial", 18, "bold")
)

strength_label.pack(pady=5)


# RESULT LABEL


result_label = ctk.CTkLabel(
    app,
    text="",
    font=("Arial", 16),
    justify="left"
)

result_label.pack(pady=20)


# PASSWORD CHECK FUNCTION


def check_password():

    password = password_entry.get()

    score = 0

    messages = []

    # LENGTH CHECK

    if len(password) >= 8:
        score += 1
    else:
        messages.append("❌ Minimum 8 characters")

    # UPPERCASE CHECK

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        messages.append("❌ Add uppercase letter")

    # LOWERCASE CHECK

    if re.search(r"[a-z]", password):
        score += 1
    else:
        messages.append("❌ Add lowercase letter")

    # NUMBER CHECK

    if re.search(r"\d", password):
        score += 1
    else:
        messages.append("❌ Add number")

    # SPECIAL CHARACTER CHECK

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        messages.append("❌ Add special character")

    # COMMON PASSWORD CHECk

    try:
        with open("common_passwords.txt", "r") as file:
            common_passwords = file.read().splitlines()

        if password.lower() in common_passwords:
            messages.append("❌ Common password detected")

    except FileNotFoundError:
        messages.append("⚠ common_passwords.txt not found")

    # PASSWORD ENTROPY

    charset_size = 0

    if re.search(r"[a-z]", password):
        charset_size += 26

    if re.search(r"[A-Z]", password):
        charset_size += 26

    if re.search(r"\d", password):
        charset_size += 10

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset_size += 32

    if charset_size > 0:
        entropy = len(password) * math.log2(charset_size)
    else:
        entropy = 0

    # UPDATE PROGRESS BAR

    progress.set(score / 5)

    percentage = int((score / 5) * 100)

    # COLOR CHANGING BAR

    if score == 0:
        color = "#5c0000"
        result = "Very Weak Password"

    elif score == 1:
        color = "#8B0000"
        result = "Weak Password"

    elif score == 2:
        color = "#ff3b30"
        result = "Poor Password"

    elif score == 3:
        color = "#ff9500"
        result = "Medium Password"

    elif score == 4:
        color = "#9acd32"
        result = "Good Password"

    else:
        color = "#00c853"
        result = "Strong Password"

    # UPDATE UI

    progress.configure(progress_color=color)

    strength_label.configure(
        text=f"Password Strength: {percentage}%",
        text_color=color
    )

    result_label.configure(
        text=
        result +
        f"\n\nEntropy: {entropy:.2f} bits\n\n" +
        "\n".join(messages),

        text_color=color
    )

# CHECK BUTTON

check_button = ctk.CTkButton(
    app,
    text="Check Password",
    command=check_password,
    width=250,
    height=50,
    corner_radius=12,
    font=("Arial", 18, "bold"),
    fg_color="#1f6aa5",
    hover_color="#144870"
)

check_button.pack(pady=20)

# REQUIREMENTS FRAME

requirements_frame = ctk.CTkFrame(
    app,
    width=500,
    corner_radius=15
)

requirements_frame.pack(pady=10)

requirements_title = ctk.CTkLabel(
    requirements_frame,
    text="Password Requirements",
    font=("Arial", 18, "bold")
)

requirements_title.pack(pady=(15, 10))

requirements_text = ctk.CTkLabel(
    requirements_frame,
    text="""
• Minimum 8 characters
• Uppercase letter (A-Z)
• Lowercase letter (a-z)
• Number (0-9)
• Special character (!@#$%^&*)
""",
    justify="left",
    font=("Arial", 14),
    text_color="gray"
)

requirements_text.pack(pady=(0, 15))

# FOOTER

footer_label = ctk.CTkLabel(
    app,
    text="Built with Python + Cybersecurity Concepts",
    font=("Arial", 12),
    text_color="gray"
)

footer_label.pack(side="bottom", pady=15)

# RUN APP

app.mainloop()