def response(hey_bob):
    remark = hey_bob.strip()

    if not remark:
        return "Fine. Be that way!"

    is_question = remark.endswith("?")

    has_letters = any(c.isalpha() for c in remark)
    is_yelling = has_letters and remark.upper() == remark

    # Yelled question
    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"

    # Yelling
    if is_yelling:
        return "Whoa, chill out!"

    # Question
    if is_question:
        return "Sure."

    # Anything else
    return "Whatever."
