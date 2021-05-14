

def seperat_line():
    print("--------------------------------------")

class temperature:

    def celsius_fahrenheit(self,value_cf):

        c_to_f = (value_cf * 1.8) + 32
        c_to_f = round(c_to_f,2)
        print(str(c_to_f) + " F")

    def fahrenheit_celsius(self,value_fc):

        f_to_c = (value_fc - 32) * 1.8
        f_to_c = round(f_to_c,2)
        print(str(f_to_c) + " C")

    def celsius_kelvin(self,value_ck):

        c_to_k = value_ck + 273.15
        c_to_k = round(c_to_k,2)
        print(str(c_to_k) + " K")

    def kelvin_celsius(self,value_kc):

        k_to_c = value_kc - 273.15
        k_to_c = round(k_to_c,2)
        print(str(k_to_c) + " C")

    def fahrenheit_kelvin(self,value_fk):

        f_to_k = ((value_fk - 32) * 0.5555 ) + 273.15
        f_to_k = round(f_to_k,2)
        print(str(f_to_k) + " K")

    def kelvin_fahrenheit(self,value_kf):

        k_to_f = ((value_kf - 273.15) * 0.5555 ) +  32
        k_to_f = round(k_to_f,2)
        print(str(k_to_f) + " F")


temp_class = temperature()


class mass():

    def grams_kilograms(self,value_gk):

        g_to_k = round((value_gk / 1000),3)
        print(str(g_to_k) + " KG")

    def kilograms_grams(self,value_kg):

        k_to_g = round((value_kg * 1000),3)
        print(str(k_to_g) + " G")

mass_class = mass()


class length():

    def cm_to_meter(self,value_cm_m):

        cm_to_m = round((value_cm_m / 100),2)
        print(str(cm_to_m) + " METERS")

    def meter_to_cm(self,value_m_cm):

        m_to_cm = round((value_m_cm * 100),2)
        print(str(m_to_cm) + " CM")

length_class = length()



class time():

    def sec_to_min(self,value_sm):

        s_to_m = round((value_sm / 60),2)
        print(str(s_to_m)+" Minutes")


    def min_to_sec(self,value_ms):

        m_to_s = round((value_ms * 60),2)
        print(str(value_ms) + "Seconds")

time_class = time()


class sub_menus():

    def temp_menue(self):

        print("Celcius to Fahrenheit    -----> 1")
        print("Fahrenheit to Celcius    -----> 2")
        print("Celcius to Kelvin        -----> 3")
        print("Kelvin to Celcius        -----> 4")
        print("Kelvin to Fahrenheit     -----> 5")
        print("Fahrenheit to Kelvin     -----> 6")

        global answer_temp_main_menue

        while True:

            answer_temp_main_menue = input("Select Your Preference : ")

            if answer_temp_main_menue not in ["1","2","3","4","5","6"]:
                continue
            else:
                answer_temp_main_menue = int(answer_temp_main_menue)
                break

    def length_menue(self):

        print("Centimeter to Meter    -----> 1")
        print("Meter to Centimeter    -----> 2")

        global answer_length_main_menue

        while True:

            answer_length_main_menue = input("Select Your Preference : ")

            if answer_length_main_menue not in ["1","2"]:
                continue
            else:
                answer_length_main_menue = int(answer_length_main_menue)
                break

    def time_menue(self):

        print("Minute to Hour    -----> 1")
        print("Hour to Minute    -----> 2")

        global answer_time_main_menue

        while True:

            answer_time_main_menue = input("Select Your Preference : ")
            if answer_time_main_menue not in ["1","2"]:
                continue
            else:
                answer_time_main_menue = int(answer_time_main_menue)
                break

    def mass_menue(self):

        print("Gram to Kilogram    -----> 1")
        print("Kilogram to Gram    -----> 2")

        global answer_mass_main_menue

        while True:

            answer_mass_main_menue = input("Select Your Preference : ")
            if answer_mass_main_menue not in ["1","2"]:
                continue
            else:
                answer_mass_main_menue = int(answer_mass_main_menue)
                break


sub_menue_class = sub_menus()

def main_menue():

    print("Mass         -----> 1")
    print("Time         -----> 2")
    print("Length       -----> 3")
    print("Temperature  -----> 4")

    seperat_line()

    global answer

    while True:

        answer = input("Choose a Measurement : ")
        if answer not in ["1","2","3","4"]:
            continue
        else:
            answer = int(answer)
            break



def process():

    main_menue()
    seperat_line()

    if answer == 1:
        sub_menue_class.mass_menue()
        seperat_line()

        if answer_mass_main_menue == 1:
            gk_in = float(input("Enter Gram Value : "))
            mass_class.grams_kilograms(gk_in)

        elif answer_mass_main_menue == 2:
            kg_in = float(input("Enter KiloGram Value : "))
            mass_class.kilograms_grams(kg_in)

    elif answer == 2:
        sub_menue_class.time_menue()
        seperat_line()

        if answer_time_main_menue == 1:

            sm_in = float(input("Enter Seconds Value : "))
            time_class.sec_to_min(sm_in)

        elif answer_time_main_menue == 2:

            ms_in = float(input("Enter Minute Value : "))
            time_class.min_to_sec(ms_in)

    elif answer == 3:
        sub_menue_class.length_menue()
        seperat_line()

        if answer_length_main_menue == 1:

            cm_in = float(input("Enter Centimeter Value : "))
            length_class.cm_to_meter(cm_in)

        elif answer_length_main_menue == 2:

            mc_in = float(input("Enter Meter Value : "))
            length_class.meter_to_cm(mc_in)


    elif answer == 4:

        sub_menue_class.temp_menue()
        seperat_line()

        if answer_temp_main_menue == 1:

            cf_in = float(input("Enter Celcius Value : "))
            temp_class.celsius_fahrenheit(cf_in)

        elif answer_temp_main_menue == 2:

            fc_in = float(input("Enter Fehrenheir Value : "))
            temp_class.fahrenheit_celsius(fc_in)

        elif answer_temp_main_menue == 3:

            ck_in = float(input("Enter Celcius Value : "))
            temp_class.celsius_kelvin(ck_in)

        elif answer_temp_main_menue == 4:

            kc_in = float(input("Enter kelvin Value : "))
            temp_class.kelvin_celsius(kc_in)

        elif answer_temp_main_menue == 5:

            kf_in = float(input("Enter kelvin Value : "))
            temp_class.kelvin_fahrenheit(kf_in)

        elif answer_temp_main_menue == 6:

            fk_in = float(input("Enter Fehrenheir Value : "))
            temp_class.fahrenheit_kelvin(fk_in)



process()














