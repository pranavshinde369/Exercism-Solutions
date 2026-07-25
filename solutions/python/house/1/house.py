VERSES = [
    ("the house that Jack built.", ""),
    ("the malt", "that lay in "),
    ("the rat", "that ate "),
    ("the cat", "that killed "),
    ("the dog", "that worried "),
    ("the cow with the crumpled horn", "that tossed "),
    ("the maiden all forlorn", "that milked "),
    ("the man all tattered and torn", "that kissed "),
    ("the priest all shaven and shorn", "that married "),
    ("the rooster that crowed in the morn", "that woke "),
    ("the farmer sowing his corn", "that kept "),
    ("the horse and the hound and the horn", "that belonged to "),
]


def recite(start_verse, end_verse):
    result = []

    for verse_num in range(start_verse, end_verse + 1):
        verse = f"This is {VERSES[verse_num - 1][0]}"

        for i in range(verse_num - 1, 0, -1):
            verse += " " + VERSES[i][1] + VERSES[i - 1][0]

        result.append(verse)

    return result