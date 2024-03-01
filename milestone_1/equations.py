new_eq1 = 'x^2 -x = 0'  # (1, -1, 0) D=1 x1 = 0 x2 = 1

terms = new_eq1.replace('(','').replace(')','').replace(' ','').replace('+-','-').replace('-+','-')


def parse_quadratic_terms(terms):
    a,b,c = '','',''

    for i, term in enumerate(terms):
        match term:
            case "^":
                for str in reversed(terms[:i-1]):
                    a = str + a
                    if not (str.isdigit() ^ str.isalpha()):
                        break
                a = -1 if a == '-' and len(a) == 1 else (1 if a == '+' and len(a) == 1 else (int(a) if a != '' else 1))

            case "x":
                if i+1 < len(terms) and terms[i+1] != '^':
                    for str in reversed(terms[:i]):
                        b = str + b
                        if not (str.isdigit() ^ str.isalpha()):
                            break
                    b = -1 if b == '-' and len(b) == 1 else (1 if b == '+' and len(b) == 1 else (int(b) if b != '' else 1))
            case _:
                if i < len(terms) - 1 and term.isdigit():
                    if i > 0 and not (terms[i+1].isdigit() ^ terms[i+1].isalpha()) and terms[i-1] != "^":
                        for str in reversed(terms[:i+1]):
                            c = str + c
                            if not (str.isdigit() ^ str.isalpha()):
                                break
    c = int(c) if c != '' else 0
    return a, b, c

a, b, c = parse_quadratic_terms(terms)


def calculate_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c

    match discriminant:
        case _ if discriminant > 0:
            x1 = (-b + discriminant**0.5) / (2*a)
            x2 = (-b - discriminant**0.5) / (2*a)
            return round(x1, 2), round(x2, 2)

        case 0:
            x1 = -b / (2*a)
            return round(x1, 2)

        case _:
            print('The equation has no real solutions since the discriminant is negative.')


result = calculate_quadratic(a,b,c)
print(result)

# Test cases

new_eq1 = 'x^2 -x = 0'  # (1, -1, 0) D=1 x1 = 0 x2 = 1
new_eq2 = '(-3)x^2 + (-12)x + (-3) = 0'  # (-3, -12, -3) x1=-0.26795 x2=3.7321
new_eq3 = '-3x^2 - 12x - 3 = 0'  # (-3, -12, -3) x1=-0.26795 x2=3.7321
new_eq4 = 'x^2+(-12)x-3 = 0'  # (1, -12, -3) D=156 x1=-0.24500 x2=12.245
new_eq5 = '-x^2 + x + 10 = 0'  # (-1, 1, 10) D=41 x1=3.7016 x2=-2.7016
new_eq6 = '-x^2 - x + 3 = 0'  # (-1, -1, 3) D=13 x1=1.3028 x2=2.3028
new_eq7 = 'x^2 - x - 3 = 0'  # (1, -1, -3) D= 13 x1=1.3028 x2=2.3028
new_eq8 = '2x^2 - x + 3 = 0'  # (2, -1, 3) 'The equation has no real solutions since the discriminant is negative.'
