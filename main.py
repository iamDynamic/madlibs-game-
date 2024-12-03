import random 

adjective = input("enter a adjective: ")
noun = input("enter a noun: ")
verb = input("enter  verb: ")
adjective2 = input("enter a adjective2: ")
noun2 = input("enter a noun2: ")
object = input("enter a object: ")
verb2 = input("enter a verb2: ")
season = input("enter a season: ")

madlib_template = (
    f"Once upon a time in a {adjective} land, there was a {noun}. It loved to {verb} every day. Everyone called it the {adjective2} {noun2}.",
    f"The brilliant software engineer {noun} meticulously analyzed {verb} the complex algorithm {object} to enhance its efficiency.",
    f"The curious student {noun} studied {verb} the intricate diagrams {object} to understand the concept better.",
    f"The energetic dog {noun} chased {verb} the colorful ball {object} across the park.",
    f"The diligent artist {noun} painted {verb} a breathtaking landscape {object} on the canvas.",
    f"The dedicated chef {noun} prepared {verb} a delicious meal {object} for the guests.",
    f"The experienced pilot {noun} maneuvered {verb} the massive airplane {object} through the storm.",
    f"The adventurous traveler {noun} explored {verb} the remote island {object} to discover hidden treasures.",
    f"The young musician {noun} played {verb} a beautiful melody {object} on the piano.",
    f"The expert programmer {noun} wrote {verb} a sophisticated application {object} for data analysis.",
    f"The {adjective} {noun} wandered through the {adjective2} forest, looking for the {noun2}.",
    f"In the {adjective} city, the {noun} {verb} every morning to stay {adjective2} and {verb2} the day.",
    f"The {adjective} {noun} spent its days {verb} in the {noun2}, creating {adjective2} {object} for everyone to admire.",
    f"At the {adjective} {noun} factory, workers {verb} the {noun2} all day to meet the {adjective2} demand.",
    f"The {adjective} {noun} enjoyed {verb} the {adjective2} {object} during the {season} season.",
    f"In the {adjective} town, the {noun} {verb} every evening under the {adjective2} sky.",
    f"The {adjective} scientist {verb} the mysterious {noun} to unlock its {adjective2} potential.",
    f"The {adjective} knight {verb} the {adjective2} dragon in the {noun} to save the {noun2}.",
    f"In the {adjective} laboratory, the {noun} {verb} {object} for the latest {adjective2} invention.",
    f"The {adjective} gardener {verb} the {noun} to grow the most {adjective2} flowers in the {season} garden."
)

Random = random.choice(madlib_template) 

print(Random)