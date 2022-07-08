from objects import Girl, Boy, Location

# چون ایرانیا پر غصه ان گفتیم یک دو سه بیخیال غصه
iran = Location(1, 2, 3)

# چون ترکیه ای ها شیطان پرستن 666
turkey = Location(6, 6, 6)

# صاحب توییت
tweet_owner = Girl(
    dna={
        'fibula_bone': 'AAGGCCT',
        'tibia_bone': 'AAGGCCT',
        'femur_bone': 'AAGGCCT',
        'vagina': 'AAGGCCT',
        'leg_muscle': 'GGGTT',
        'cords_mucosal': 'GTAC',
        'epiglottis': 'CCGGTA'
    },
    location=iran
)

# دوست پسر صاحب توییت
tweet_owners_bf = Boy(
    dna={
        'fibula_bone': 'AAGGCCT',
        'tibia_bone': 'CCGGTA',
        'femur_bone': 'GTAC',
        'penis': 'GTAC',
        'leg_muscle': 'GGGTT',
        'cords_mucosal': 'GTAC',
        'epiglottis': 'CCGGTA'
    },
    location=iran
)
# برادر دوست پسر صاحب توییت
tweet_owners_bfs_brother = Boy(
    dna={
        'fibula_bone': 'TTAAC',
        'tibia_bone': 'GGGTT',
        'femur_bone': 'CCGGTA',
        'penis': 'AAGGCCT',
        'leg_muscle': 'GGGTT',
        'cords_mucosal': 'GTAC',
        'epiglottis': 'CCGGTA'
    },
    location=iran
)
# دوست دختر 8 ساله برادر دوست پسرش
tweet_owners_bfs_brother.partner.append(
    Girl(dna={
        'fibula_bone': 'TTAAC',
        'tibia_bone': 'GGGTT',
        'femur_bone': 'CCGGTA',
        'vagina': 'AAGGCCT',
        'leg_muscle': 'GGGTT',
        'cords_mucosal': 'GTAC',
        'epiglottis': 'CCGGTA'
}, location=iran)
)
# یه دختر دیگه(همکار اکسش)
tweet_owners_exs_colleague = Girl(
    dna={
        'fibula_bone': 'TTAAC',
        'tibia_bone': 'GGGTT',
        'femur_bone': 'CCGGTA',
        'vagina': 'AAGGCCT',
        'leg_muscle': 'GGGTT',
        'cords_mucosal': 'GTAC',
        'epiglottis': 'CCGGTA'
    },
    location=iran
)

# انگ زدن خیانت
tweet_owners_exs_colleague.talk('این دختره خیانت میکنه', 'high')

# مخ زدن همکار اکسش و سکس
tweet_owners_exs_colleague.tempting_other_boys([tweet_owners_bfs_brother])
tweet_owners_exs_colleague.partner.append(tweet_owners_exs_colleague)
tweet_owners_exs_colleague.sex()

# سفر به ترکیه
tweet_owners_bf.location = turkey
tweet_owners_exs_colleague.location = turkey
tweet_owners_bfs_brother.location = turkey

# نشان دهنده جندگی همکار اکسش
print(tweet_owners_exs_colleague.slut)
