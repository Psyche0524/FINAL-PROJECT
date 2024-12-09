#BIODATA ACTIVITY 04/09/2024

def act3():
      input("Fill up the following information for your biodata. " + "\n\nPress Any Key to Start Filling Out Your E-Biodata... ")

      fullName      = input        ("FULLNAME               : ")
      age           = int(input    ("AGE                    : "))
      gender        = input        ("GENDER                 : ")
      dateBirth     = input        ("BIRTHDATE              : ")
      address       = input        ("ADDRESS                : ")
      religion      = input        ("RELIGION               : ")
      language      = input        ("LANGUAGE KNOWN         : ")
      civilStatus   = input        ("CIVIL STATUS           : ")
      mobileNumber  = int(input    ("MOBILE NUMBER          : "))
      eduAttainment = input        ("EDUCATIONAL ATTAINMENT : ")
      qualification = input        ("QUALIFICATION          : ")
      experience    = input        ("EXPERIENCE             : ")

      print(input("\nPress Any Keys to Preview Your Biodata... ") + 
            "\n------------------------------ BIODATA ------------------------------ \n" + 
            "\n _ _ _ _ _" + 
            "\n|         |" + "\tFULLNAME               : ", fullName,
            "\n|  35x45  |" + "\tAGE                    : ", age,
            "\n|    mm   |" + "\tGENDER                 : ", gender,
            "\n|         |" + "\tBIRTHDATE              : ", dateBirth,
            "\n|         |" + "\tADDRESS                : ", address,
            "\n|_ _ _ _ _|" + "\tRELIGION               : ", religion,
            "\n \t\tLANGUAGE KNOWN         : ", language,
            "\n \t\tCIVIL STATUS           : ", civilStatus,
            "\n \t\tMOBILE NUMBER          : ", mobileNumber,  
            "\n \t\tEDUCATIONAL ATTAINMENT : ", eduAttainment,
            "\n \t\tQUALIFICATION          : ", qualification, 
            "\n \t\tEXPERIENCE             : ", experience,
            "\n\n--------------------------------------------------------------------- \n" + 
            "\n\nYou Successfully Made a E-Biodata, thanks for using the program."
            )