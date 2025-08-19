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
    print("                @@                                                               @@")  
    print("               @@@@                                                              @@@")  
    print("              @@@@@                                                             @@@@@")  
    print("               @@@@@                                                           @@@@@")  
    print("                @@@@@@                                                       @@@@@@")  
    print("                 @@@@@@                                                     @@@@@@")  
    print("                  @@@@@@                                                   @@@@@@")  
    print("                @@ @@@@                                                     @@@@ @@")  
    print("               @@@@@@@                                                       @@@@@@@")  
    print("             @@@@@@@@                                                         @@@@@@@@")  
    print("            @@@@@@@                                                             @@@@@@@")  
    print("           @@@@@@@@                       Telegram: @amir_Gods                 @@@@@@@@")  
    print("          @@@@@@@@@@                                                           @@@@@@@@@@")  
    print("         @@@@@@@@@@@@ @                       @@@@@@@                       @ @@@@@@@@@@@")  
    print("         @@@@@@@@@@@ @@@@                 @@@@@@@@@@@@@@@                 @@@@ @@@@@@@@@@@")  
    print("         @@@@@@@@@@@@@@@  @@@@    @@@@@@@@@@@@@@@@@    @@@@@@@@@@    @@@@  @@@@@@@@@@@@@@@")  
    print("          @@@@@@@@@@@@@@ @@@@  @@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@  @@@@ @@@@@@@@@@@@@@")  
    print("           @@@@@@@@@@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@      @@@@@@@@@@@@  @@@@@@@@@@@@@@@@@")  
    print("              @@@@@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@      @@@      @@@@@@ @@@@@@@@@@@@@")  
    print("                @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@                  @@@@@@@@@@@@@@@@@")  
    print("                   @@@@@@@@@@@@@@@@@@@@@@@                         @@@@@@@@@@@@@")  
    print("                     @@@@@@@@@@@@@@@@@@@@                        @@@@@@@@@@@@@")  
    print("                        @@@@@@@@@@@@@@@@@@@@@                  @@@@@@@@@@@@")  
    print("                          @@@@@@@@@@@@@@@@@@@                  @@@@@@@@@@")  
    print("                          @@@@@@@@@@@@@@@@@@                  @@@@@@@@@@@")  
    print("                        @@@@@@@@@@@@@@                @@@@@@@@@@@@@@@@@@@@@")  
    print("                          @@@@@@@@@@@@@@@          @@@@@@@@@@@@@@@@@@@@@@")  
    print("                           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")  
    print("                            @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")  
    print("                             @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @")  
    print("                             @ @@@    @@@@@@@@@@@@@@@@@@@@      @@@@")  
    print("                               @@@         @@@@@@@@@@@          @@@@@")  
    print("                          @   @@@@           @@@@@@@@           @@@@@@  @")  
    print("                         @@@@@@@@@@@       @@@@@@@@@@@@@       @@@@@@@@@@@")  
    print("                         @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")  
    print("                          @@@@@@@@@@@@@@@@@@@@@@ @ @@@@@@@@@@@@@@@@@@@@@@")  
    print("                           @@@@@@@@@@@@@@@@@@@@     @@@@@@@@@@@@@@@@@@@@")  
    print("                           @@@@@@@@@@@@@@@@@@@       @@@@@@@@@@@@@@@@@@@")  
    print("                            @@@@@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@@@@@")  
    print("                               @@@@  @@@@@@@@@@@@@ @@@@@@@@@@@  @@@@")  
    print("                                      @@@@@@@@@@@@@@@@@@@@@@@")  
    print("                                     @@@@@@@@@@@@@@@@@@@@@@@@@")  
    print("                                    @@@@@@@@@@@@@@@@@@@@@@@@@@@")  
    print("                                     @@@@@@@@@@@@@@@@@@@@@@@@@")  
    print("                                      @@@@@ @@@@@ @@@@@ @@@@@")  
    print("                                       @@@@  @@@@ @@@@  @@@@")  
    print("                                       @@@@  @@@@ @@@   @@@")  
    print("                                        @@    @@@ @@     @")  
    print("                                         @     @@ @")  
    print("                                                @")  
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

def save_file(results, filename="results.txt"):  
    with open(filename, "a") as f:  
        for line in results:  
            clean_line = line.replace(Fore.RED, "").replace(Fore.GREEN, "").replace(Style.RESET_ALL, "")  
            f.write(clean_line + "\n")  

def send_emails(email_list, receiver_emails, subject, body, total_count):  
    if not email_list:  
        print(f"{Fore.RED}Email list is empty!{Style.RESET_ALL}")  
        return  
    results = []  
    for i in range(total_count):  
        sender_email, sender_password = random.choice(email_list)  
        receiver_email = random.choice(receiver_emails)  
        success, message = send_email(sender_email, sender_password, receiver_email, subject, body)  
        if success:  
            results.append(f"{Fore.GREEN}{message}{Style.RESET_ALL}")  
        else:  
            results.append(f"{Fore.RED}{message}{Style.RESET_ALL}")  
        print(results[-1])  
    save_file(results)  
    print(f"{Fore.CYAN}Results saved to results.txt{Style.RESET_ALL}")  

def get_input(prompt="Paste Body (end with END or Ctrl+D):"):  
    print(prompt)  
    lines = []  
    while True:  
        try:  
            line = input()  
        except EOFError:  
            break  
        if line.strip().upper() == "END":  
            break  
        lines.append(line)  
    return "\n".join(lines)  

def get_inputs():  
    amir_rahmati()  
    jomjomeg()  
    print(f"{Fore.GREEN}Writer of this source code: Amir Rahmati{Style.RESET_ALL}")  
    print(f"{Fore.CYAN}Choose email input method:{Style.RESET_ALL}")  
    print(f"{Fore.WHITE}1. Load from file (emails.txt){Style.RESET_ALL}")  
    print(f"{Fore.WHITE}2. Enter manually{Style.RESET_ALL}")  
    method = input("Enter choice (1 or 2): ")  
    email_list = []  
    if method == "1":  
        filename = input("Enter filename (default: emails.txt): ") or "emails.txt"  
        try:  
            with open(filename, "r") as f:  
                for line in f:  
                    parts = line.strip().split(":")  
                    if len(parts) == 2:  
                        email_list.append((parts[0], parts[1]))  
            print(f"{Fore.GREEN}Loaded {len(email_list)} emails from file.{Style.RESET_ALL}")  
        except FileNotFoundError:  
            print(f"{Fore.RED}File not found!{Style.RESET_ALL}")  
            return None, None, None, None, None  
    else:  
        i = 1  
        while True:  
            email = input(f"{Fore.WHITE}Enter Email #{i}: {Style.RESET_ALL}")  
            password = input(f"{Fore.WHITE}Enter Password for {email}: {Style.RESET_ALL}")  
            email_list.append((email, password))  
            more = input("Add another? (y/n): ")  
            if more.lower() != "y":  
                break  
            i += 1  
    print(f"{Fore.CYAN}Receiver Emails:{Style.RESET_ALL}")  
    print(f"{Fore.WHITE}1. Single email{Style.RESET_ALL}")  
    print(f"{Fore.WHITE}2. Multiple emails from file{Style.RESET_ALL}")  
    choice = input("Enter choice (1 or 2): ")  
    receiver_emails = []  
    if choice == "1":  
        receiver_email = input(f"{Fore.WHITE}Enter Receiver Email: {Style.RESET_ALL}")  
        receiver_emails.append(receiver_email)  
    else:  
        filename = input("Enter receiver filename (default: receivers.txt): ") or "receivers.txt"  
        try:  
            with open(filename, "r") as f:  
                for line in f:  
                    line = line.strip()  
                    if line:  
                        receiver_emails.append(line)  
            print(f"{Fore.GREEN}Loaded {len(receiver_emails)} receiver emails from file.{Style.RESET_ALL}")  
        except FileNotFoundError:  
            print(f"{Fore.RED}File not found!{Style.RESET_ALL}")  
            return None, None, None, None, None  
    try:  
        subject = input(f"{Fore.WHITE}Enter Subject: {Style.RESET_ALL}")  
        body = get_input()  
        total_count = int(input(f"{Fore.WHITE}Enter Total Emails to Send: {Style.RESET_ALL}"))  
        amir_rahmati()  
        jomjomeg()  
        print(f"{Fore.GREEN}Writer of this source code: Amir Rahmati{Style.RESET_ALL}")  
        return email_list, receiver_emails, subject, body, total_count  
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
            email_list, receiver_emails, subject, body, total_count = get_inputs()  
            if email_list:  
                send_emails(email_list, receiver_emails, subject, body, total_count)  
        elif choice == "2":  
            print(f"{Fore.GREEN}Exiting. Good luck!{Style.RESET_ALL}")  
            break  
        else:  
            print(f"{Fore.RED}Invalid option! Enter 1 or 2.{Style.RESET_ALL}")  
            time.sleep(2)  

if __name__ == "__main__":  
    menu()
