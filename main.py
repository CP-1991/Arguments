# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
# Great Template
def greet(name, greeting_template= 'Hello, <name>!'):
    greeting = greeting_template.replace('<name>', name)
    (f'{greeting_template}{name}')
    return greeting

print(greet('Bob'))
print(greet('Bob', "What's up, <name>!"))

#Force
#How much force to hold an apple with a mass of 0,1kg
def force(mass, body = 'Earth'):
    planet = {"Earth": 9.8, 
            "Sun": 274, 
            "Neptune": 11.2, 
            "Jupiter": 24.9, 
            "Saturn": 10.2, 
            "Uranus": 8.9, 
            "Venus": 8.9, 
            "Mars": 3.7, 
            "Mercury": 3.7, 
            "Moon": 1.6, 
            "Pluto": 0.6}
    gravity = planet.get(body)
    calculated_planet = mass * gravity
    return calculated_planet

print(force(0.1))
print(force(0.1,'Sun'))

#Gravity
def pull(m1, m2, d):
    G = 6.674 * (10 ** -11)
    F = G * ((m1 * m2 ) / d**2)
    return F

print(pull(500, 700, 10))