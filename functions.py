def replacer(word, char1, char2):
    return word.replace(char1, char2)

def dollarizer(word):
    return replacer(word, 's', '$')

def eurizer(word):
    return replacer(word, 'e', '€')

def wonky_text(word):
    replacements = [('s', '$'), ('e', '€'), ('l', '£')]
    for char1, char2 in replacements:
        word = replacer(word, char1, char2)
    return word

def celcius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def age_in_days(age_in_years):
    return age_in_years * 365

def simple_interest(principal, rate, time):
    return principal * rate * time

def plan_finances(principal, rate, time, desired_amount):
    interest = simple_interest(principal, rate, time)
    final_amount = principal + interest
    return final_amount >= desired_amount