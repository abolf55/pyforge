import os
import subprocess
import sys
import requests
os.system("color a")
os.system("cls")
while True:
    print("============(work with cmd)==========")
    print("chose your work you want to do:", "\n",
          "1-ip show", "\n",
          "2-show the information of pc", "\n",
          "3-chek all the library that instaled from pythone", "\n",
          "4-install new library for pythone", "\n",
          "5- ip finder", "\n",
          "6-exchange the (.py) to (.exe)", "\n",
          "0-exit","\n","7- change format")
    print("======================")
    a = int(input("enter the number :"))
    print("======================")
    if a == 0:
        print("Exiting...")
        break
    if a == 1:
        print("which one of the ip that you want ?", "\n", "1- your pc ip", "\t", "2- the ip of diffrent sites")
        print("==================")
        b = int(input("enter the number :"))
        if b == 1:
            os.system("ipconfig")
            print("=====================")
        elif b == 2:
            c = input("enter name of the site like(forexample.com) :")
            os.system("nslookup " + c)
            print("==============================")

    elif a == 2:
        print("your pc information is :")
        os.system("systeminfo")
        print("==================================")

    elif a == 3:
        os.system("pip list")

    elif a == 4:
        e = input("enter name of the library that you want to install :")
        os.system("pip install " + e)

    elif a == 5:
        def public_ip_tracker():
            print("\n--- Global IP Tracker ---")
            target_ip = input("Enter IP to track (or press Enter for your own): ")

            if not target_ip:
                url = "http://ip-api.com/json/"
            else:
                url = f"http://ip-api.com/json/{target_ip}"

            try:
                response = requests.get(url)
                data = response.json()

                if data['status'] == 'fail':
                    print(f"Error: {data['message']}")
                else:
                    print(f"IP: {data['query']}")
                    print(f"Country: {data['country']}")
                    print(f"Region: {data['regionName']}")
                    print(f"City: {data['city']}")
                    print(f"ISP: {data['isp']}")
                    print(f"Lat/Lon: {data['lat']}, {data['lon']}")
                    print(f"Timezone: {data['timezone']}")
            except Exception as e:
                print(f"Connection Error: {e}")

        public_ip_tracker()

    elif a == 6:
        import os
        import subprocess

        print("\n--- Advanced Python to EXE Converter ---")
        file_name = input("Esme file ro vared kon (masalan: myscript.py) : ").strip()
        
        # 1. Location Selection
        print("\nFile kojast?")
        print("1) Desktop")
        print("2) Drive D (D:\\)")
        print("3) Vared kardan masir dasti")
        loc_choice = input("Entekhab kon (1/2/3) : ").strip()

        if loc_choice == "1":
            home = os.path.expanduser("~")
            if os.path.isdir(os.path.join(home, "OneDrive", "Desktop")):
                file_location = os.path.join(home, "OneDrive", "Desktop")
            else:
                file_location = os.path.join(home, "Desktop")
        elif loc_choice == "2":
            file_location = "D:\\"
        else:
            file_location = input("Masire poushe ro vared kon: ").strip('"')

        file_location = os.path.abspath(file_location)
        if not file_name.endswith(".py"):
            file_name += ".py"
        
        full_path = os.path.join(file_location, file_name)

        if not os.path.isfile(full_path):
            print(f"Error: File '{file_name}' nimeye dar in masir!")
        else:
            # --- START ADVANCED SETTINGS ---
            cmd_args = [] # Inja hamye amrha ro jar mi konim
            
            print("\n--- Advanced Settings ---")
            
            # 2. Mode: Onefile or Directory
            mode_choice = input("Mode: 1) One File (Single EXE)  2) One Directory (Folder) -> Choose (1/2): ").strip()
            if mode_choice == "1":
                cmd_args.append("--onefile")
            else:
                cmd_args.append("--onedir")

            # 3. Console Mode
            console_choice = input("Show Console? (1) Yes (Show CMD)  2) No (Hide CMD for GUI) -> Choose (1/2): ").strip()
            if console_choice == "2":
                cmd_args.append("--noconsole")

            # 4. Icon
            add_icon = input("Add Icon? (y/n): ").lower().strip()
            if add_icon == 'y':
                icon_path = input("Masire file icon (.ico) ro vared kon: ").strip('"')
                if os.path.isfile(icon_path):
                    cmd_args.append(f"--icon={icon_path}")
                else:
                    print("Icon nimeye! In amraz bypass shod.")

            # 5. Custom Name
            new_name = input("Change Output Name? (Enter to skip): ").strip()
            if new_name:
                if not new_name.endswith(".exe"):
                    new_name += ".exe"
                # Note: PyInstaller uses the script name, but we can use --name
                cmd_args.append(f"--name={new_name}")

            # 6. Extra Files
            add_extra = input("Add extra files (images, txt, etc)? (y/n): ").lower().strip()
            extra_files_list = []
            if add_extra == 'y':
                print("Masire file ha ro vared kon (be khat khat moshaghebe kon / Finish):")
                while True:
                    f_path = input("Extra file path: ").strip('"')
                    if f_path.lower() == 'finish':
                        break
                    if os.path.isfile(f_path):
                        extra_files_list.append(f_path)
                    else:
                        print("File nimeye! Dobare try kon.")
                
                for ef in extra_files_list:
                    # Format: --add-data "source;destination" (Windows uses ;)
                    cmd_args.append(f"--add-data={ef};.")

            # --- EXECUTION ---
            print("\n[!] In dar hal e convert kardan ast... Lotfan sabr kon...")
            
            # Final Command Construction
            final_command = ["pyinstaller"] + cmd_args + [full_path]

            try:
                subprocess.run(
                    final_command, 
                    check=True, 
                    stdout=subprocess.DEVNULL, 
                    stderr=subprocess.DEVNULL
                )
                print("\n[+] SUCCESS!")
                print(f"[+] File shoma dar poushe 'dist' dar masire {file_location} sakhte shod.")
                
                # Auto Cleanup (Optional but recommended)
                cleanup = input("\nDo you want to delete build files and .spec file? (y/n): ").lower().strip()
                if cleanup == 'y':
                    import shutil
                    # Delete build folder
                    build_dir = os.path.join(file_location, "build")
                    if os.path.exists(build_dir):
                        shutil.rmtree(build_dir)
                    # Delete .spec file
                    spec_file = os.path.join(file_location, file_name.replace(".py", ".spec"))
                    if os.path.exists(spec_file):
                        os.remove(spec_file)
                    print("[+] Cleanup done.")

            except subprocess.CalledProcessError:
                print("\n[-] ERROR: Kari namoshode. Motmaen bash ke pyinstaller nasb ast.")
            except Exception as e:
                print(f"\n[-] An error occurred: {e}")

    elif a == 7:  # فرض می‌کنیم منوی جدید شماره 7 است
        import os
        from PIL import Image

        print("\n--- Professional Image Converter & Resizer ---")
        
        # 1. Location Selection (مشابه بخش قبلی برای یکپارچگی)
        print("\nFiles kojast?")
        print("1) Desktop")
        print("2) Drive D (D:\\)")
        print("3) Vared kardan masir dasti")
        loc_choice = input("Entekhab kon (1/2/3) : ").strip()

        if loc_choice == "1":
            home = os.path.expanduser("~")
            file_location = os.path.join(home, "Desktop") if not os.path.exists(os.path.join(home, "OneDrive", "Desktop")) else os.path.join(home, "OneDrive", "Desktop")
        elif loc_choice == "2":
            file_location = "D:\\"
        else:
            file_location = input("Masire poushe ro vared kon: ").strip('"')

        file_location = os.path.abspath(file_location)

        if not os.path.isdir(file_location):
            print("Error: In masir valid nist!")
        else:
            # 2. Extension Filtering
            current_ext = input("Pasvand-e file-ha hage dar in poushe chist? (masalan: png, jpg, webp): ").strip().lower().replace(".", "")
            target_ext = input("Be che pasvandi konim? (masalan: jpg, webp, png): ").strip().lower().replace(".", "")
            
            # 3. Resize Options
            do_resize = input("Aya mikhay size ro ham taghyir bedi? (y/n): ").lower().strip()
            new_width = 0
            new_height = 0
            if do_resize == 'y':
                new_width = int(input("Width (elam): ").strip())
                new_height = int(input("Height (elam): ").strip())

            # 4. Process Files
            # پیدا کردن تمام فایل‌هایی که پسوند مورد نظر رو دارن
            files_to_process = [f for f in os.listdir(file_location) if f.lower().endswith(f".{current_ext}")]

            if not files_to_process:
                print(f"Hich fileyi ba pasvand .{current_ext} peyda nashod dar in masir!")
            else:
                print(f"\n[!] {len(files_to_process)} file peyda shod. Dar hal e pardazesh...")
                
                # ساخت یک پوشه برای خروجی‌ها تا فایل‌های اصلی بهم نریزن
                output_folder = os.path.join(file_location, f"Converted_{target_ext}_files")
                if not os.path.exists(output_folder):
                    os.makedirs(output_folder)

                success_count = 0
                error_count = 0

                for filename in files_to_process:
                    try:
                        # مسیر کامل فایل ورودی
                        img_path = os.path.join(file_location, filename)
                        img = Image.open(img_path)

                        # مدیریت رنگ (تبدیل RGBA به RGB برای جلوگیری از خطا در تبدیل به JPG)
                        if target_ext in ['jpg', 'jpeg'] and img.mode in ('RGBA', 'P'):
                            img = img.convert('RGB')
                        elif img.mode != 'RGB' and target_ext != 'png':
                            img = img.convert('RGB')

                        # اعمال تغییر سایز اگر درخواست شده بود
                        if do_resize == 'y':
                            img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

                        # ساخت اسم جدید فایل
                        name_without_ext = os.path.splitext(filename)[0]
                        new_filename = f"{name_without_ext}.{target_ext}"
                        save_path = os.path.join(output_folder, new_filename)

                        # ذخیره فایل
                        img.save(save_path, target_ext.upper())
                        success_count += 1
                    except Exception as e:
                        print(f"Error converting {filename}: {e}")
                        error_count += 1

                print("\n--- Process Finished ---")
                print(f"[+] Success: {success_count}")
                print(f"[-] Failed: {error_count}")
                print(f"[+] Files saved in: {output_folder}")
