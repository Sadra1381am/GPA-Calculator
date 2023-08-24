from tabulate import tabulate

# University data
university = {
   "Harvard University": 4.0,
   "Stanford University": 3.95,
   "Massachusetts Institute of Technology (MIT)": 3.9,
   "California Institute of Technology (Caltech)": 3.85,
   "Princeton University": 3.8,
   "Yale University": 3.75,
   "Columbia University": 3.7,
   "University of Chicago": 3.65,
   "University of Oxford": 3.6,
   "University of Cambridge": 3.55,
   "ETH Zurich": 3.5,
   "University of Tokyo": 3.45,
   "National University of Singapore": 3.4,
   "University of Toronto": 3.35,
   "University of Melbourne": 3.3,
   "University of California, Berkeley": 3.25,
   "University of Michigan": 3.2,
   "Peking University": 3.15,
   "University of Washington": 3.1,
   "University of Edinburgh": 3.05,
   "McGill University": 3.0,
   "University of Texas at Austin": 2.95,
   "University of Sydney": 2.9,
   "University of Hong Kong": 2.85,
   "University of Amsterdam": 2.8,
   "Sorbonne University": 2.75,
   "University of São Paulo": 2.7,
   "Moscow State University": 2.65,
   "Seoul National University": 2.6,
   "University of Cape Town": 2.55,
   "University of Buenos Aires": 2.5,
   "University of Delhi": 2.45,
   "University of Nairobi": 2.4,
   "Cairo University": 2.35,
   "University of Dhaka": 2.3,
   "University of Lagos": 2.25,
   "University of Tehran": 2.2,
   "University of Karachi": 2.15,
   "University of Cairo": 2.1,
   "University of Baghdad": 2.05,
   "University of Kabul": 2.0,
   "University of Tripoli": 1.95,
   "University of Mogadishu": 1.9,
   "University of Sana'a": 1.85,
   "University of Kinshasa": 1.8,
   "University of Port-au-Prince": 1.75,
   "University of Timbuktu": 1.7,
   "University of Pyongyang": 1.65,
   "University of Asmara": 1.6,
   "University of Vientiane": 1.55,
   "University of Juba": 1.5,
   "University of N'Djamena": 1.45,
   "University of Ulaanbaatar": 1.4,
   "University of Niamey": 1.35,
   "University of Ouagadougou": 1.3,
   "University of Bujumbura": 1.25,
   "University of Bangui": 1.2,
   "University of Mbabane": 1.15,
   "University of Georgetown": 1.1,
   "University of Roseau": 1.05,
   "University of Basseterre": 1.0,
}

def main():
    list_score = []
    list_credit = []

    while True:
        try:
            get_score(list_score, list_credit)
        except KeyboardInterrupt:
            gpa = calculate_gpa(list_score, list_credit)
            unis = compare(gpa)
            print("\n\n\n\n\n")
            print("––––––––––––––––––")
            print(f"Your GPA is: {gpa:.2f}")
            print("––––––––––––––––––")
            print(tabulate(unis, headers=["University", "GPA"], tablefmt="heavy_grid"))
            break
        except:
            print("Invalid input. Please try again.")

def get_score(list_score, list_credit):
    '''
    This function will get scores and credits.
    '''
    score = float(input("Enter score: "))
    credit = int(input("Enter credit: "))
    if 20 >= score >= 0 and credit > 0:
        list_score.append(score)
        list_credit.append(credit)
    else:
        print("Invalid score or credit. Please try again.")

def calculate_gpa(list_score, list_credit):
    '''
    This function will calculate total GPA.
    '''
    total_weighted_score = 0
    total_credit = sum(list_credit)
    
    for score, credit in zip(list_score, list_credit):
        if score >= 17:
            g = 4
        elif score >= 14:
            g = 3
        elif score >= 12:
            g = 2
        elif score >= 10:
            g = 1
        else:
            g = 0
        weighted_score = credit * g
        total_weighted_score += weighted_score
    
    return total_weighted_score / total_credit

def compare(gpa):
    '''
    This function will compare the GPA to other universities and will predict
    which of them will accept you.
    '''
    uni = []
    for k, v in university.items():
        if (gpa + 0.1 >= v >= gpa - 0.2):
            print(k,v)
            uni.append([k, v])
    return uni

if __name__ == "__main__":
    main()
