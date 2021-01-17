def recite(start_verse: int, end_verse: int) -> list:
    days = [
        "first",
        "second",
        "third",
        "fourth",
        "fifth",
        "sixth",
        "seventh",
        "eighth",
        "ninth",
        "tenth",
        "eleventh",
        "twelfth",
    ]

    gifts = [
        "a Partridge in a Pear Tree",
        "two Turtle Doves",
        "three French Hens",
        "four Calling Birds",
        "five Gold Rings",
        "six Geese-a-Laying",
        "seven Swans-a-Swimming",
        "eight Maids-a-Milking",
        "nine Ladies Dancing",
        "ten Lords-a-Leaping",
        "eleven Pipers Piping",
        "twelve Drummers Drumming",
    ]

    if start_verse == end_verse:
        twelve_days= ""
        twelve_days += "On the " + days[end_verse - 1] + " day of Christmas my true love gave to me: "

        if end_verse == 1:
            twelve_days += gifts[0] + "."
        else:
            recited_gifts = []

            for index in range(end_verse):
                recited_gifts.append(gifts[index])

            recited_gifts.reverse()

            for verse in range(end_verse):
                if verse == end_verse - 1:
                    twelve_days += "and " + recited_gifts[verse] + "."
                else:
                    twelve_days += recited_gifts[verse] + ", "
        return [twelve_days]
    else:
        recited_verses = []

        for verse in range(start_verse, end_verse + 1):
            recited_verses.append(recite(verse,verse)[0])

        return recited_verses    

    
