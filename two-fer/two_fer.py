def two_fer(name="you") -> str:
    if type(name) != str:
        raise Exception("The argument provided must be a string.")

    return "One for {}, one for me.".format(name)
