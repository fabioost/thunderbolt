import re
from django.core.exceptions import ValidationError

def validate_domain_email(value):
	if not "yourdomain.com" in value:
		raise ValidationError("Sorry, the email submited is invalid.")
	return value

def validate_cpf(value):
	return value


def isCpfValid(cpf):
    """ If cpf in the Brazilian format is valid, it returns True, otherwise, it returns False. """

    # Check if type is str
    if not isinstance(cpf,str):
        raise ValidationError("CPF Inválido.")

    # Remove some unwanted characters
    cpf = re.sub("[^0-9]",'',cpf)

    # Checks if string has 11 characters
    if len(cpf) != 11:
        raise ValidationError("CPF Inválido.")

    sum = 0
    weight = 10

    """ Calculating the first cpf check digit. """
    for n in range(9):
        sum = sum + int(cpf[n]) * weight

        # Decrement weight
        weight = weight - 1

    verifyingDigit = 11 -  sum % 11

    if verifyingDigit > 9 :
        firstVerifyingDigit = 0
    else:
        firstVerifyingDigit = verifyingDigit

    """ Calculating the second check digit of cpf. """
    sum = 0
    weight = 11
    for n in range(10):
        sum = sum + int(cpf[n]) * weight

        # Decrement weight
        weight = weight - 1

    verifyingDigit = 11 -  sum % 11

    if verifyingDigit > 9 :
        secondVerifyingDigit = 0
    else:
        secondVerifyingDigit = verifyingDigit

    if cpf[-2:] == "%s%s" % (firstVerifyingDigit,secondVerifyingDigit):
        return cpf
    else:
    	raise ValidationError("CPF Inválido.")
