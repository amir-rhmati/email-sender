import smtplib
from email.mime.text import MIMEText
import random
import time
import os
from colorama import init, Fore, Style

init()

def amir_rahmati():
    os.system('cls' if os.name == 'nt' else 'clear')

def jomjomeg():
    print(f"{Fore.GREEN}")
    print("                              @@@@@@@@@@@@@@@")
    print("  @                         @@@@@@@@     @@@@@@@@                         @")
    print("  @@@                     @@@@@@@@   @@@   @@@@@@@@                     @@@")
    print("   @@@@@@              @@@@@@@@@@  @@   @@  @@@@@@@@@@              @@@@@@")
    print("    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@     @@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("      @@@@@@@@@@@@@@@@@@@@@@@@@@@ @@     @@ @@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("                        @@@@@@@@@@  @@@@@  @@@@@@@@@@")
    print("                         @@@@  @@@@@     @@@@@  @@@@")
    print("                         @@@@    @@@@@@@@@@@    @@@@ Email sender rahmati ")
    print("                        @@@@@      @@@@@@@      @@@@")
    print("                        @@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("                          @@@@@@@@@@@@ @@@@@@@@@@@@    Version 1")
    print("                           @@   @@@@  @  @@@@   @@")
    print("                                @@@@@@@@@@@@@")
    print("                                 @@@@@@@@@@@   Telegram: @amir_Gods")
    print("                                 @@ @@@@@ @@")
    print("                                  @ @@ @@ @")
    print("                                     @ @")
    print(f"{Style.RESET_ALL}")

def send_email(sender_email, sender_password, receiver_email, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        return True, f"Email sent from {sender_email} to {receiver_email}"
    except Exception as e:
        return False, f"Error sending email from {sender_email}: {e}"

def send_emails(email_list, receiver_email, subject, body, total_count):
    if not email_list:
        print(f"{Fore.RED}Email list is empty!{Style.RESET_ALL}")
        return
    results = []
    for i in range(total_count):
        sender_email, sender_password = random.choice(email_list)
        success, message = send_email(sender_email, sender_password, receiver_email, subject, body)
        if success:
            results.append(f"{Fore.GREEN}{message}{Style.RESET_ALL}")
        else:
            results.append(f"{Fore.RED}{message}{Style.RESET_ALL}")
        
        amir_rahmati()
        jomjomeg()
        print(f"{Fore.GREEN}Writer of this source code: Amir Rahmati{Style.RESET_ALL}")
        for result in results:
            print(result)
        
    time.sleep(3)

def rahmati():
    amir_rahmati()
    jomjomeg()
    print(f"{Fore.GREEN}Writer of this source code: Amir Rahmati{Style.RESET_ALL}")
    
    email_list = []
    i = 1
    while True:
        email = input(f"{Fore.WHITE}Enter Email #{i}: {Style.RESET_ALL}")
        password = input(f"{Fore.WHITE}Enter Password for {email}: {Style.RESET_ALL}")
        email_list.append((email, password))
        
        print(f"{Fore.CYAN}Add another email?{Style.RESET_ALL}")
        choice = input(f"{Fore.WHITE}1 for Yes, 2 for No: {Style.RESET_ALL}")
        if choice == "2":
            break
        elif choice != "1":
            print(f"{Fore.RED}Invalid option! Enter 1 or 2.{Style.RESET_ALL}")
            print(f"{Fore.CYAN}Add another email?{Style.RESET_ALL}")
            choice = input(f"{Fore.WHITE}1 for Yes, 2 for No: {Style.RESET_ALL}")
            if choice == "2":
                break
        i += 1
    
    try:
        receiver_email = input(f"{Fore.WHITE}Enter Receiver Email: {Style.RESET_ALL}")
        if not receiver_email:
            raise ValueError("Receiver email cannot be empty!")
        subject = input(f"{Fore.WHITE}Enter Subject: {Style.RESET_ALL}")
        body = input(f"{Fore.WHITE}Enter Body: {Style.RESET_ALL}")
        total_count = int(input(f"{Fore.WHITE}Enter Total Emails to Send: {Style.RESET_ALL}"))
        
        amir_rahmati()
        jomjomeg()
        print(f"{Fore.GREEN}Writer of this source code: Amir Rahmati{Style.RESET_ALL}")
        return email_list, receiver_email, subject, body, total_count
    except ValueError as e:
        print(f"{Fore.RED}Invalid input! {str(e)}. Please try again.{Style.RESET_ALL}")
        return None, None, None, None, None

def menu():
    while True:
        amir_rahmati()
        print(f"\n{Fore.CYAN}================================{Style.RESET_ALL}")
        print(f"{Fore.CYAN}         Amir Rahmati         {Style.RESET_ALL}")
        print(f"{Fore.CYAN}================================{Style.RESET_ALL}")
        print(f"{Fore.WHITE}1. Send Emails                  {Style.RESET_ALL}")
        print(f"{Fore.WHITE}2. Exit                         {Style.RESET_ALL}")
        print(f"{Fore.CYAN}================================{Style.RESET_ALL}")
        choice = input(f"{Fore.WHITE}Enter your choice (1 or 2): {Style.RESET_ALL}")

        if choice == "1":
            email_list, receiver_email, subject, body, total_count = rahmati()
            if email_list:
                send_emails(email_list, receiver_email, subject, body, total_count)
        elif choice == "2":
            print(f"{Fore.GREEN}Exiting. Good luck!{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Invalid option! Enter 1 or 2.{Style.RESET_ALL}")
            time.sleep(2)

if __name__ == "__main__":
    menu()