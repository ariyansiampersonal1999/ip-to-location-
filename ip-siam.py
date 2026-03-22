import requests
import os
import time
import sys
# Color Codes
R = "\033[91m"
G = "\033[92m"
Y = "\033[93m"
B = "\033[94m"
C = "\033[96m"
W = "\033[0m"

def clear():
    os.system("clear")

def loading():
    print(Y + "\nSearching", end="")
    for i in range(5):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.3)
    print(W)

def banner():
    print(C + """
███████╗██╗ █████╗ ███╗   ███╗
██╔════╝██║██╔══██╗████╗ ████║
███████╗██║███████║██╔████╔██║
╚════██║██║██╔══██║██║╚██╔╝██║
███████║██║██║  ██║██║ ╚═╝ ██║
╚══════╝╚═╝╚═╝  ╚═╝╚═╝     ╚═╝

        SIAM IP TOOL PREMIUM
""" + W)

def lookup_ip(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url, timeout=5)
        data = response.json()

        loading()

        if data.get('status') == 'success':
            print(G + "\n========= IP DETAILS =========" + W)
            print("🌍 Country:", data.get('country'))
            print("🔤 Country Code:", data.get('countryCode'))
            print("🗺 Region:", data.get('regionName'))
            print("🏙 City:", data.get('city'))
            print("📮 ZIP Code:", data.get('zip'))
            print("📍 Latitude:", data.get('lat'))
            print("📍 Longitude:", data.get('lon'))
            print("🕒 Timezone:", data.get('timezone'))
            print("🌐 ISP:", data.get('isp'))
            print("🏢 Organization:", data.get('org'))
            print("🧾 AS Number:", data.get('as'))

            print("\n🗺 Google Maps:")
            print(f"https://www.google.com/maps?q={data.get('lat')},{data.get('lon')}")
        else:
            print(R + "❌ Invalid IP or API Limit Reached" + W)

    except requests.exceptions.RequestException:
        print(R + "❌ Network Error! Check your internet." + W)
    except ValueError:
        print(R + "❌ Failed to decode API response." + W)
    except Exception as e:
        print(R + f"❌ Unexpected Error: {e}" + W)

def get_own_ip():
    try:
        return requests.get("https://api.ipify.org", timeout=5).text
    except:
        return None

def main():
    while True:
        clear()
        banner()
        print(B + "1. Check Your Own IP")
        print("2. Check Any IP")
        print("0. Exit" + W)

        choice = input("\nEnter Option: ")

        if choice == "1":
            ip = get_own_ip()
            if ip:
                print("\nYour Public IP:", ip)
                lookup_ip(ip)
            else:
                print(R + "❌ Could not fetch your IP." + W)
            input("\nPress Enter To Continue...")

        elif choice == "2":
            target_ip = input("Enter Target IP: ")
            if target_ip.strip() == "":
                print(R + "❌ IP cannot be empty!" + W)
            else:
                lookup_ip(target_ip)
            input("\nPress Enter To Continue...")

        elif choice == "0":
            print(Y + "Goodbye SIAM 👑" + W)
            break

        else:
            print(R + "Invalid Option!" + W)
            time.sleep(1)

if __name__ == "__main__":
    main()