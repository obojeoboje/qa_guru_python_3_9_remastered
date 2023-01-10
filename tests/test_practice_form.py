from demoqa_tests.model.pages import practice_form


def test_filled_form():
    practice_form.open_page()

    # INPUT DATA

    practice_form.input_info(name='Aleksandr',
                             surname='Privalov',
                             email='obojealexander@gmail.com',
                             mobile='1234567890',
                             address='Saint Petersburg'
                             )

    practice_form.select_gender('Male')

    practice_form.select_birthday(day='27', month='4', year='1999')

    practice_form.input_subject('Computer Science')

    practice_form.select_hobbies('Music', 'Sports')

    practice_form.upload_picture('resources/picture.jpg')

    practice_form.select_state('NCR')
    practice_form.select_city('Delhi')

    practice_form.submit()

    # ASSERT

    practice_form.assert_of_registered_user(
        'Aleksandr Privalov',
        'obojealexander@gmail.com',
        'Male',
        '1234567890',
        '27 May,1999',
        'Computer Science',
        'Music, Sports',
        'picture.jpg',
        'Saint Petersburg',
        'NCR Delhi'
    )
