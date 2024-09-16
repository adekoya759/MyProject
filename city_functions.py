
def address(city, country, population=None):

    if population:
        full_address = f"{city} {country}- population {population}"

    else:
        full_address = f"{city} {country}"
    return full_address.title()