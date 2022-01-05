paragraph = "On the night of the 2016 presidential election, I spent a long time deciding what to wear. I’d be staying home to watch the"\
"returns with my partner, but the Comey letter had come out in mid-October and I was convinced Trump was going to win. I’d always"\
"admired the women on the Titanic who reportedly drowned wearing their finest clothing and furs and jewels and the violinists who"\
"kept playing even as the ship sank. I wore a burgundy velvet dress with sheer lace back paneling, a ribbon in my hair, red lipstick,"\
"and a leopard-print faux fur coat over my shoulders. I poured myself a goblet of wine. I understood that night would be my end, but"\
"I would not be ushered to an internment camp in sweatpants. The returns hadn’t finished coming in when my father, who is undocumented,"\
"called me to tell me it was the end times. I threw myself into bed without washing off my makeup, without brushing my teeth. I had a"\
"four a.m. wake-up call."\
# Paragraph of the book: The Undocumented Americans by Karla Cornejo Villavicencio

words_number = 0
previous_character = " "

for character in paragraph:
    if character == ' ' and previous_character != " ":
        words_number += 1
    previous_character = character

if character != ' ':
    words_number += 1

print('Total:', words_number)