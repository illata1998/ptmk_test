def validate_full_name(full_name_arg):
    if not full_name_arg:
        raise ValueError("'Full Name' argument must be provided.")
    return full_name_arg


def validate_sex(sex_arg):
    if not sex_arg:
        raise ValueError("'Sex' argument must be provided.")
    if sex_arg not in ['Male', 'Female']:
        raise ValueError("'Sex' argument must be either 'Male' or 'Female'")
    return sex_arg


def validate_dob(dob_arg):
    if not dob_arg:
        raise ValueError("'Date of Birth' argument must be provided.")
    return dob_arg
